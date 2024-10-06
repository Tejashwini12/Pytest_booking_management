import logging
from behave import given, when, then  # type: ignore
from test_Booking.scr.Management.booking_management import BookingManagement
from test_Booking.scr.Utils.RestDrivers.Response import Response
from test_Booking.scr.Utils.Assertion.assertion import Assertion

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@given('I have authorized the session')
def authorize_session(context):
    """Authorize the session and store the token."""
    # Call the method to authorize and get the token
    context.token = context.booking_management.authorize_token(base_url=context.base_url)
    if not context.token:
        raise Exception("Failed to authorize and obtain token.")

@when('I create a new booking')
def create_new_booking(context):
    """Create a new booking."""
    logger.info("Creating a new booking.")
    # Call the method to create a booking and store the response
    context.response_holder = context.booking_management.create_booking_data(base_url=context.base_url, token=context.token)
    logger.info("Booking creation response: %s", context.response_holder)

@then('I should receive a success response')
def verify_success_response(context):
    """Verify that the response indicates success."""
    response = context.response_holder
    if response is None:
        raise Exception("No response received from booking.")

    # Unpack the response into status code, response dictionary, and error
    status_code, response_dict, error = response
    expected_status = Response.StatusCode.HTTP_OK  

    logger.info("Received status code: %d", status_code)

    # Assert the response status code matches the expected status
    Assertion.response_status_should_be_equal(
        actual_status=status_code,
        exp_status=expected_status,
        response=response_dict
    )

    logger.info("Response received: %s", response_dict)  # Log the response details
