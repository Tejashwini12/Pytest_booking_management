import logging
from behave import given, when, then  # type: ignore
from test_Booking.scr.Utils.Assertion.assertion import Assertion
from test_Booking.scr.Utils.RestDrivers.Response import Response

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@when('I update the booking details')
def step_when_update_booking(context):
    """Update the booking with provided details."""
    booking_id = context.booking_id 
    
    logger.info("Requesting booking details for ID: %s", booking_id)
    response = context.booking_management.update_booking_data(base_url=context.base_url, booking_id=booking_id, token=context.token)
    context.response_holder = response


@then('the booking details should be updated')
def step_then_verify_booking_updated(context):
    """Verify that the booking details were updated successfully."""
    response = context.response_holder
    
    if response is None or response[0] is None:
        logger.error("No valid response received for booking update.")
        raise Exception("No valid response received for booking update.")
    
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

    # Check for expected keys in the response
    expected_keys = ['firstname', 'lastname', 'totalprice', 'depositpaid', 'bookingdates', 'additionalneeds']
    for key in expected_keys:
        if key not in response_dict:
            logger.error("Expected key '%s' not found in the response after update.", key)
            raise Exception(f"Expected key '{key}' not found in the response after update.")
    
    logger.info("Booking updated successfully with details: %s", response_dict)
