from behave import given, when, then 
from test_Booking.scr.Management.booking_management import BookingManagement
from test_Booking.scr.Utils.RestDrivers.Response import Response
from test_Booking.scr.Utils.Assertion.assertion import Assertion

import logging 

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@given('I have created a booking')
def step_given_create_booking(context):
    # Call the method to create a booking and handle the response
    status, response_body, error = context.booking_management.create_booking_data(context.base_url, context.token)

    # Raise an exception if there was an error creating the booking
    if error:
        raise Exception(f"Error creating booking: {error}")

    # Extract the booking ID from the response body
    context.booking_id = response_body.get('bookingid')

    # Check if the booking ID was retrieved successfully
    if context.booking_id is None:
        raise Exception("Failed to retrieve booking ID from the response.")

    logger.info("Created booking with ID: %s", context.booking_id)

@when('I request the booking details for the created booking')
def step_when_get_booking_details(context):
    # Retrieve the booking ID from the context
    booking_id = context.booking_id
    logger.info("Requesting booking details for ID: %s", booking_id)
    
    # Request the booking details using the booking ID
    response = context.booking_management.get_booking_by_id_data(base_url=context.base_url, booking_id=booking_id, token=context.token)
    context.response_holder = response  

@then('I should receive the booking details for the created booking')
def step_then_receive_booking_details(context):
    # Retrieve the booking ID and response from the context
    booking_id = context.booking_id
    response = context.response_holder

    # Check if the response is valid
    if response is None:
        raise Exception(f"No valid response received for booking ID {booking_id}")

    # Unpack the response into status code, response dictionary, and error
    status_code, response_dict, error = response
    expected_status = Response.StatusCode.HTTP_OK  

    # Assert the response status code matches the expected status
    Assertion.response_status_should_be_equal(
        actual_status=status_code,
        exp_status=expected_status,
        response=response_dict
    )

    # Validate other expected fields in the response
    expected_fields = ['firstname', 'lastname', 'totalprice', 'depositpaid', 'bookingdates']  # Add any other expected fields
    for field in expected_fields:
        if field not in response_dict:
            raise Exception(f"Missing expected field in response: {field}")

    logger.info("Successfully validated booking details for ID: %s", booking_id)
