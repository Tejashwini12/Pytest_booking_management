import logging
from behave import given, when, then  # type: ignore
from test_Booking.scr.Management.booking_management import BookingManagement
from test_Booking.scr.Utils.RestDrivers.Response import Response
from test_Booking.scr.Utils.Assertion.assertion import Assertion

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@when('I request the list of booking IDs')
def step_when_get_booking_ids(context):
    """Request the list of booking IDs."""
    logger.info("Requesting the list of booking IDs from %s", context.base_url)
    response = context.booking_management.get_booking_ids_data(base_url=context.base_url, token=context.token)
    context.response_holder = response

@then('I should receive all the booking IDs')
def step_then_receive_booking_ids(context):
    """Verify that the response contains all the booking IDs."""
    response = context.response_holder

    if response is None:
        raise Exception("No response received from booking IDs request.")

    status_code, response_dict, error = response
    expected_status = Response.StatusCode.HTTP_OK

    # Log the received status code
    logger.info("Received status code: %d", status_code)

    # Assert the response status code
    Assertion.response_status_should_be_equal(
        actual_status=status_code,
        exp_status=expected_status,
        response=response_dict
    )

    # Check if booking IDs are present in the response
    if isinstance(response_dict, list) and response_dict:
        booking_ids = [booking['bookingid'] for booking in response_dict if 'bookingid' in booking]
        if not booking_ids:
            raise Exception("No booking IDs found in the response.")
    else:
        raise Exception("No booking IDs found in the response or response format is incorrect.")

    # Log the booking IDs
    logger.info("Booking IDs found: %s", booking_ids)
