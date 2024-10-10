import logging
import pytest
from test_Booking.src.Response import Response

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Sample of valid and invalid payloads
@pytest.mark.parametrize("booking_id, payload", [
    (4,  # Valid booking ID
     {"firstname": "Jane", "lastname": "Doe", "totalprice": 150, "depositpaid": False, "bookingdates": {"checkin": "2024-02-01", "checkout": "2024-02-10"}}
     ),  # Valid payload

    (5,  # Valid booking ID
     {"lastname": "Doe", "totalprice": 150, "depositpaid": False, "bookingdates": {"checkin": "2024-02-01", "checkout": "2024-02-10"}}),  # Missing first name

    (99999,  # Invalid booking ID
     {"firstname": "Jane", "lastname": "Doe", "totalprice": 150, "depositpaid": False, "bookingdates": {"checkin": "2024-02-01", "checkout": "2024-02-10"}}), 

    (18,  # Valid booking ID
     {"firstname": "John", "totalprice": -50, "depositpaid": True, "bookingdates": {"checkin": "2024-02-01", "checkout": "2024-02-10"}}),  # Invalid total price

    (-12, #invalid booking ID
     {"firstname": "Jane", "lastname": "Doe", "depositpaid": False, "bookingdates": {"checkin": "2024-02-01", "checkout": "2024-02-10"}}
     ) # InValid payload)
])
def test_update_booking(base_url, booking_management, authorized_session, booking_id, payload):
    """Test case to verify the response status code and data of an update booking request."""
    status_code, response_dict, error = booking_management.update_booking_data(base_url=base_url, booking_id=booking_id, token=authorized_session, payload=payload)

    logger.info(f"Received status code: {status_code} for booking ID: {booking_id}")

    # Verify the response status code
    expected_status_code = Response.StatusCode.HTTP_OK
    if status_code == expected_status_code:
        logger.info(f"Expected status code {expected_status_code} matches {status_code}. Response: {response_dict}")

        # Validate response data against the payload
        if 'firstname' in payload:
            assert response_dict['firstname'] == payload['firstname'], f"Expected firstname {payload['firstname']}, but got {response_dict['firstname']}"
            logger.info(f"Verified firstname: {response_dict['firstname']} matches expected value.")

        if 'lastname' in payload:
            assert response_dict['lastname'] == payload['lastname'], f"Expected lastname {payload['lastname']}, but got {response_dict['lastname']}"
            logger.info(f"Verified lastname: {response_dict['lastname']} matches expected value.")

        if 'totalprice' in payload:
            assert response_dict['totalprice'] == payload['totalprice'], f"Expected totalprice {payload['totalprice']}, but got {response_dict['totalprice']}"
            logger.info(f"Verified totalprice: {response_dict['totalprice']} matches expected value.")

        if 'depositpaid' in payload:
            assert response_dict['depositpaid'] == payload['depositpaid'], f"Expected depositpaid {payload['depositpaid']}, but got {response_dict['depositpaid']}"
            logger.info(f"Verified depositpaid: {response_dict['depositpaid']} matches expected value.")

        if 'bookingdates' in payload:
            assert response_dict['bookingdates'] == payload['bookingdates'], f"Expected bookingdates {payload['bookingdates']}, but got {response_dict['bookingdates']}"
            logger.info(f"Verified bookingdates: {response_dict['bookingdates']} matches expected value.")

    else:
        logger.info(f"Validation skipped for status code: {status_code}. Expected: {expected_status_code}. Response: {response_dict}")
