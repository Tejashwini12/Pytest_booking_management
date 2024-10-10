import logging
from test_Booking.src.Response import Response

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def test_get_checkin_and_checkout(booking_data):
    """Extract and return the check-in and check-out dates from the booking data."""
    booking_data = booking_data.get('booking')
    if not booking_data:
        raise Exception("Failed to retrieve booking data.")
    
    booking_dates = booking_data.get('bookingdates', {})
    checkin = booking_dates.get('checkin')
    checkout = booking_dates.get('checkout')

    assert checkin is not None, "Check-in date is missing."
    assert checkout is not None, "Check-out date is missing."

    logger.info(f"successfully fetched checkin_date:{checkin} and checkout_date:{checkout} data")

    return checkin, checkout

def test_filter_booking_ids_by_dates(base_url, booking_management, booking_data):
    """Test requesting booking IDs filtered by check-in and check-out dates."""
    checkin, checkout = test_get_checkin_and_checkout(booking_data)
    filters = {'checkin': checkin, 'checkout': checkout}
    status_code, response_dict, error = booking_management.filter(base_url=base_url, filters=filters)
    expected_status_code = Response.StatusCode.HTTP_OK
     
    logger.info(f"Received status code: {status_code}")

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
