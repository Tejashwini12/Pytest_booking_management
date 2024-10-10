import logging
from test_Booking.src.Response import Response

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



def test_delete_booking(base_url, booking_management, authorized_session, get_valid_booking_id):
    """Test to verify the status code and response data after deleting the booking."""
    booking_id = get_valid_booking_id
    print(booking_id)
    status_code, response_body, error = booking_management.delete_booking_data(base_url=base_url, booking_id=booking_id, token= authorized_session)
    expected_status_code = Response.StatusCode.HTTP_CREATED

    logger.info(f"Received status code: {status_code}")

    # Verify the status code
    assert status_code == expected_status_code, (
        f"Expected status code {expected_status_code}, but got {status_code}. "
        f"Response: {response_body}"
    )
    logger.info(f"Response status code: {status_code} matches expected status code: {expected_status_code}")

    # Verify the response data
    logger.info("Validating response body: %s", response_body)
    assert response_body == "Created", (
        f'Expected response body to indicate "Created", but got {response_body}'
    )
    logger.info(f"Response data verified successfully: {response_body}")
