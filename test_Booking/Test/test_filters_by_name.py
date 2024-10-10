import logging
from test_Booking.src.Response import Response

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def test_get_first_name_and_last_name(booking_data):
    """Extract and return the first name and last name from the booking data."""
    booking_data = booking_data.get('booking')
    if not booking_data:
        raise Exception("Failed to retrieve booking data.")
    
    first_name = booking_data.get('firstname')
    last_name = booking_data.get('lastname')

    assert first_name is not None, "First name is missing."
    assert last_name is not None, "Last name is missing."

    logger.info(f"successfully fetched firstname:{first_name} and lastname:{last_name} data")
    return first_name, last_name

def test_filter_booking_ids_by_name(base_url, booking_management,booking_data):
    """Test requesting booking IDs filtered by name."""
    first_name, last_name = test_get_first_name_and_last_name(booking_data)
    filters = {'firstname': first_name, 'lastname': last_name}
    status_code, response_dict, error = booking_management.filter(base_url=base_url, filters= filters)
    expected_status_code = Response.StatusCode.HTTP_OK

    logger.info(f"Received status code:{status_code}")

    # Verify the response status code
    assert status_code == expected_status_code, (
        f"Expected status code {expected_status_code}, but got {status_code}. "
        f"Response: {response_dict}"
    )
    logger.info(f"Response status code: {status_code} matches expected status code: {expected_status_code}")

    # Verify the response data
    booking_ids_list = [booking.get('bookingid') for booking in response_dict if 'bookingid' in booking]
    assert booking_ids_list, "No booking IDs found."

    logger.info(f"Booking IDs found: {booking_ids_list}")
