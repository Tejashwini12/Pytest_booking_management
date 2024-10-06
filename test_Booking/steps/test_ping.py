import logging
from behave import given, when, then
from test_Booking.scr.Utils.RestDrivers.Response import Response
from test_Booking.scr.Utils.Assertion.assertion import Assertion

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@when('I send a GET request to the health check endpoint')
def step_when_send_get_request(context):
    """Step to send a GET request to the health check endpoint."""
    logger.info("Requesting the ping API")  
    response = context.booking_management.ping_data(context.base_url)  
    context.response_holder = response  

@then('I should receive a "created" response with 201 status code')
def step_verify_response(context):
    """Step to verify the response from the health check endpoint."""
    response = context.response_holder  

    # Assert that a response was received
    assert response is not None, "No response was recorded in context."
    
    # Unpack the response into status code, body, and error
    status_code, response_body, error = response

    # Check if the status code is None and log an error if it is
    if status_code is None:
        logger.error("Failed to get a valid response. Error: %s", error)
        assert False, f"Expected status code 201 but got None. Error: {error}"

    logger.info("Validating response status code: %d", status_code)  # Log the status code for verification
    
    expected_status = Response.StatusCode.HTTP_CREATED

    # Assert that the status code is 201
    Assertion.response_status_should_be_equal(
        actual_status=status_code,
        exp_status=expected_status,
        response=response_body
    )
    
    logger.info("Validating response body: %s", response_body)  # Log the response body for verification
    
    # Assert that the response body indicates "created"
    assert response_body == "Created", f'Expected response body to indicate "created", but got {response_body}'
