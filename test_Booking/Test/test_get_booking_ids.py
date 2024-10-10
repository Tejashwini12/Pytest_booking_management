import logging
from test_Booking.src.Response import Response

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def test_get_booking_ids(base_url, booking_management, authorized_session):
    """Test to verify the status code and booking IDs when requesting booking IDs."""
    # Unpack the response into status code, response dictionary, and error
    status_code, response_dict, error = booking_management.get_booking_ids_data(base_url=base_url, token=authorized_session)
    expected_status_code = Response.StatusCode.HTTP_OK

    # Verify the status code
    logger.info("Received status code: %d", status_code)
    assert status_code == expected_status_code, (
        f"Expected status code {expected_status_code}, but got {status_code}. "
        f"Response: {response_dict}"
    )
    logger.info(f"Response status code: {status_code} matches expected status code: {expected_status_code}")

    # Validate booking IDs in the response
    booking_ids_list = [booking.get('bookingid') for booking in response_dict if 'bookingid' in booking]
    assert booking_ids_list, "No booking IDs found."
    
    logger.info(f"Booking IDs found: {booking_ids_list}")
