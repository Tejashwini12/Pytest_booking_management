import logging
import pytest
from test_Booking.src.Response import Response

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


import logging
import pytest
from test_Booking.src.Response import Response

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@pytest.mark.parametrize("url_fixture", [
    "base_url",    # Valid URL fixture
    "invalid_base_url"  # Invalid URL fixture
])
def test_health_check(request, url_fixture, booking_management):
    """Test to verify the status code and response data of the health check endpoint with valid and invalid url."""
    
    # Get the actual URL from the fixture
    url = request.getfixturevalue(url_fixture)

    # Call the health check endpoint
    status_code, response_body, error = booking_management.ping_data(base_url=url)

    if url_fixture == "base_url":
        expected_status_code = Response.StatusCode.HTTP_CREATED  # Use the correct expected status for a valid URL
        assert status_code == expected_status_code, (
            f"Expected status code {expected_status_code}, but got {status_code}. "
            f"Response: {response_body}"
        )
        logger.info(f"Response status code: {status_code} matches expected status code: {expected_status_code}")

        
        logger.info("Validating response body: %s", response_body)
        assert response_body == "Created", (
            f'Expected response body to indicate "Created", but got {response_body}'
        )
        logger.info(f"Response data verified successfully: {response_body}")

    else:  # For the invalid URL case
        expected_status_code = Response.StatusCode.HTTP_CREATED
        assert status_code != expected_status_code, (
            f"Expected a non-200 status code for invalid URL, but got {status_code}. "
            f"Response: {response_body}"
        )
        logger.info(f"Invalid URL correctly returned non-200 status code for URL: {url}")

