import pytest
import requests
from test_Booking.src.booking_management import BookingManagement


@pytest.fixture(scope='module')
def base_url():
    """Fixture to provide the base URL for API calls."""
    return 'https://restful-booker.herokuapp.com'  

@pytest.fixture(scope='module')
def invalid_base_url():
    """Fixture to provide the base URL for API calls."""
    return 'https:/restful.herokuapp.co'  

@pytest.fixture(scope='module')
def booking_management():
    """Fixture to initialize BookingManagement."""
    session = requests.Session()  # Create a session instance
    management = BookingManagement(session)  # Pass the session to the constructor
    yield management
    session.close()  # Clean up the session after tests

@pytest.fixture(scope='module')
def authorized_session(booking_management, base_url):
    """Fixture to authorize the session and return the token."""
    token = booking_management.authorize_token(base_url=base_url)
    assert token, "Failed to authorize and obtain token."
    return token

@pytest.fixture(scope='module')
def booking_data(authorized_session, booking_management, base_url):
    """Fixture to create a booking and return the full response body."""
    status, response_body, error = booking_management.create_booking_data(base_url, token=authorized_session)

    if error:
        raise Exception(f"Error creating booking: {error}")

    return response_body 

@pytest.fixture(scope='module')
def get_valid_booking_id(booking_data):
    """Extract and return the booking ID from the response body."""
    booking_id = booking_data.get('bookingid')
    assert booking_id is not None, "Failed to retrieve booking ID from the response."
    return booking_id