import logging
import pytest
from test_Booking.src.Response import Response

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def test_create_booking(base_url,booking_management,authorized_session):
    """Test case to verify the response status code and data of a booking creation."""
    status_code, response_dict, error = booking_management.create_booking_data(base_url=base_url, token=authorized_session)
    expected_status_code = Response.StatusCode.HTTP_OK 

    logger.info(f"Received status code: {status_code}")

    # Verify the response status code
    assert status_code == expected_status_code, (
        f"Expected status code {expected_status_code}, but got {status_code}. "
        f"Response: {response_dict}"
    )
    logger.info(f"Response status code: {status_code} matches expected status code: {expected_status_code}")

    # Verify the response data
    assert response_dict is not None, "No response received from booking."
    
    assert "bookingid" in response_dict, "Booking ID not found in response."
    assert response_dict["bookingid"] > 0, "Booking ID should be a positive integer."

    # Verify required fields in the booking
    booking_data = response_dict.get("booking", {})
    assert "firstname" in booking_data, "Firstname not found in response."
    assert "lastname" in booking_data, "Lastname not found in response."
    assert "totalprice" in booking_data, "Total price not found in response."
    assert "depositpaid" in booking_data, "Deposit paid status not found in response."
    assert "bookingdates" in booking_data, "Booking dates not found in response."
    
    logger.info(f"Response data verified successfully: {response_dict}")


