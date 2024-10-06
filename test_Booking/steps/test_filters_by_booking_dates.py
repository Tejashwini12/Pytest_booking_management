import logging
from behave import given, when, then  # type: ignore

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@given('I have the check-in date "{checkin}" and check-out date "{checkout}"')
def set_checkin_checkout_dates(context, checkin, checkout):
    """Create a booking and store the check-in and check-out dates."""
    # Create booking data using the provided check-in and check-out dates
    status, response_body, error = context.booking_management.create_booking_data(
        context.base_url,
        context.token
    )

    # Raise an exception if there was an error creating the booking
    if error:
        raise Exception(f"Error creating booking: {error}")

    # Extract booking data from the response
    booking_data = response_body.get('booking')
    if not booking_data:
        raise Exception("Failed to retrieve booking data.")

    # Retrieve and store the check-in and check-out dates
    booking_dates = booking_data.get('bookingdates', {})
    context.checkin = booking_dates.get('checkin')
    context.checkout = booking_dates.get('checkout')

    logger.info("Booking created with check-in: %s and check-out: %s", context.checkin, context.checkout)

@when('I request booking IDs filtered by check-in and check-out dates')
def request_booking_ids(context):
    """Request booking IDs based on check-in and check-out dates."""
    # Prepare the filter criteria using the stored check-in and check-out dates
    context.filters = {'checkin': context.checkin, 'checkout': context.checkout}
    logger.info("Requesting booking IDs with filters: %s", context.filters)

    # Call the filter method to get booking IDs based on the criteria
    response_code, response_body, error = context.booking_management.filter(
        base_url=context.base_url,
        filters=context.filters
    )

    # Raise an exception if there was an error while filtering booking IDs
    if error:
        raise Exception("Error while filtering booking IDs.")

    # Store the response code and body for further verification
    context.status_code = response_code
    context.response_body = response_body

    logger.info("Received response code: %s", context.status_code)  # Log the received status code
