import logging
from behave import when 
from test_Booking.scr.Utils.RestDrivers.Response import Response

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@when('I delete the booking details')
def step_when_delete_booking(context):
    """Step definition for deleting booking details."""
    
    # Get the booking ID from the context
    booking_id = context.booking_id 

    logger.info("Attempting to delete booking with ID: %s", booking_id)
    
    # Call the delete booking method
    response = context.booking_management.delete_booking_data(
        base_url=context.base_url,   # Base URL for the API
        booking_id=booking_id,       # Booking ID to delete
        token=context.token           # Authorization token
    )
    
    # Ensure a response was received
    assert response is not None, "Delete request returned no response."
    
    # Store the response in the context for later use
    context.response_holder = response
    logger.info("Booking deletion response received: %s", response)
