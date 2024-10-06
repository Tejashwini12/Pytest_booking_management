import logging
from behave import given, when, then
from test_Booking.scr.Utils.RestDrivers.Response import Response

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@given('I have the first name "{first_name}" and last name "{last_name}"')
def step_given_first_last_name(context, first_name, last_name):
    """Create a booking and store the first and last names."""
    
    # Create booking data
    status, response_body, error = context.booking_management.create_booking_data(
        context.base_url,
        context.token
    )

    if error:
        raise Exception(f"Error creating booking: {error}")

    # Retrieve booking data
    booking_data = response_body.get('booking')
    if not booking_data:
        raise Exception("Failed to retrieve booking data.")

    # Set context variables for first and last names
    context.first_name = booking_data.get('firstname')
    context.last_name = booking_data.get('lastname')

    # Log successful booking creation
    logger.info("Successfully created booking for: %s %s", context.first_name, context.last_name)


@when('I request booking IDs filtered by first name and last name')
def step_when_filter_by_name(context):
    context.filters = {'firstname': context.first_name, 'lastname': context.last_name}
    logger.info("Requesting booking IDs with filters: %s", context.filters)

    response_code, response_body, error = context.booking_management.filter(
        base_url=context.base_url,
        filters=context.filters
    )
    
    context.status_code = response_code
    context.response_body = response_body
    context.error = error

    if context.error:
        raise Exception("Error while filtering booking IDs.")

    logger.info("Response Code: %s", context.status_code)


@then('I should receive booking ID')
def step_then_receive_booking_ids(context):
    assert context.status_code == Response.StatusCode.HTTP_OK, f"Expected status code 200 but got {context.status_code}"
    
    response_dict = context.response_body
    if not response_dict:
        raise Exception("Response body is empty.")

    booking_ids = [booking.get('bookingid') for booking in response_dict if 'bookingid' in booking]
    if not booking_ids:
        raise Exception("No booking IDs found.")

    logger.info("Booking IDs found: %s", booking_ids)
