import logging
from behave import given, when, then  # type: ignore
from test_Booking.scr.Utils.Assertion.assertion import Assertion
from test_Booking.scr.Utils.RestDrivers.Response import Response

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@when('I update the booking details partially')
def step_when_update_booking(context):
    """Update the booking with provided details."""
    
    # Retrieve the booking ID from the context
    booking_id = context.booking_id 
    
    logger.info("Requesting partial update for booking ID: %s", booking_id)
    
    # Call the method to partially update the booking details
    response = context.booking_management.partial_update_booking_data(
        base_url=context.base_url,
        booking_id=booking_id,
        token=context.token
    )
    
    # Store the response for further validation
    context.response_holder = response
