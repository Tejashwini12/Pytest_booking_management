import pytest
import logging
from test_Booking.src.Response import Response

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def test_get_booking_details(base_url, booking_management, authorized_session, get_valid_booking_id):
    """Test to verify the status code and data when fetching booking details."""
    # Unpack the response into status code, response dictionary, and error
    booking_id = get_valid_booking_id
    status_code, response_dict, error = booking_management.get_booking_by_id_data(base_url=base_url, booking_id=booking_id, token= authorized_session)
    expected_status_code = Response.StatusCode.HTTP_OK  

    # Verify the status code
    assert status_code == expected_status_code, (
        f"Expected status code {expected_status_code}, but got {status_code}. Response: {response_dict}"
    )
    logger.info(f"Response status code: {status_code} matches expected status code: {expected_status_code}")

    # Validate expected fields in the response
    expected_fields = ['firstname', 'lastname', 'totalprice', 'depositpaid', 'bookingdates']
    for field in expected_fields:
        assert field in response_dict, f"Missing expected field in response: {field}"

    logger.info(f"Successful_ly validated booking data: {response_dict}")
