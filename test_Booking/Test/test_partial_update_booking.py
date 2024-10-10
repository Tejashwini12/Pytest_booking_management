import pytest
import logging
from test_Booking.src.Response import Response

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)    

@pytest.mark.parametrize("booking_id, payload", [
    (23,{"firstname": "Jane", "lastname": "Doe"}), 
    (13,{"totalprice":"111"}),
    (16,{"depositpaid": True})
])
def test_partial_update_booking(base_url, booking_management, authorized_session, payload, booking_id):
    """Verify the status code and data for the partial booking update."""
    status_code, response_dict, error = booking_management.partial_update_booking_data(base_url=base_url, booking_id=booking_id, payload=payload, token=authorized_session)
    
    logger.info(f"Received status code:{status_code}")

    # Verify the status code
    expected_status_code = Response.StatusCode.HTTP_OK
    assert status_code == expected_status_code, f"Expected status code {expected_status_code}, but got {status_code}. Response: {response_dict}"

    # Validate expected fields in the response
    if status_code == expected_status_code:
        expected_keys = ['firstname', 'lastname', 'totalprice', 'depositpaid', 'bookingdates', 'additionalneeds']
        
        for key in expected_keys:
            assert key in response_dict, f"Expected key '{key}' not found in the response after update."
            logger.info("Verified key '%s' is present in the response.", key)
    else:
        logger.info(f"Validation skipped for status code: {status_code}. Expected: {expected_status_code}. Response: {response_dict}")
