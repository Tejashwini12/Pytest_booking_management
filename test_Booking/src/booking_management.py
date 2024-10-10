from test_Booking.src.Response import Response
from test_Booking.src.bookingmanager import BookingManager

class BookingManagement:
    def __init__(self, session):
        self.session = session
        self.token = None 

    def ping_data(self, base_url: str):
        """Ping the given base URL to check connectivity."""
        booking_manager = BookingManager(self.session)
        return booking_manager.ping(base_url)

    def _get_actual_token(self, token: str = None):
        """Retrieve the actual token to use for API requests."""
        return token if token else self.token

    def authorize_token(self, base_url: str, exp_status=Response.StatusCode.HTTP_OK):
        """Authorize and retrieve a token from the API."""
        booking_manager = BookingManager(self.session)
        status_code, response_body, error = booking_manager.authorize(base_url)

        if error or status_code != exp_status:
            return None

        self.token = response_body.get('token')
        if not self.token:
            return None
        
        return self.token

    def create_booking_data(self, base_url: str, token: str = None, exp_status=Response.StatusCode.HTTP_OK):
        """Create a booking with the given data."""
        actual_token = self._get_actual_token(token)
        if not actual_token:
            return None
        
        booking_manager = BookingManager(self.session)
        status_code, response_body, error = booking_manager.create_booking(base_url, token=actual_token)

        if error or status_code != exp_status:
            return None, error
        
        return status_code, response_body, None

    def update_booking_data(self, base_url: str, booking_id: int, payload,token: str = None):
        """Update an existing booking."""
        actual_token = self._get_actual_token(token)
        if not actual_token:
            return None

        booking_manager = BookingManager(self.session)
        return booking_manager.update_booking(base_url, booking_id, payload, token=actual_token)

    def partial_update_booking_data(self, base_url: str, booking_id: int, payload,token: str = None):
        """Partially update an existing booking."""
        actual_token = self._get_actual_token(token)
        if not actual_token:
            return None

        booking_manager = BookingManager(self.session)
        return booking_manager.partial_update_booking(base_url, booking_id, payload, token=actual_token)

    def get_booking_ids_data(self, base_url: str, token: str = None):
        """Retrieve booking IDs from the API."""
        actual_token = self._get_actual_token(token)
        if not actual_token:
            return None

        booking_manager = BookingManager(self.session)
        return booking_manager.get_booking_ids(base_url, token=actual_token)

    def get_booking_by_id_data(self, base_url: str, booking_id: int, token: str = None):
        """Get booking details by ID."""
        actual_token = self._get_actual_token(token)
        if not actual_token:
            return None

        booking_manager = BookingManager(self.session)
        return booking_manager.get_booking_by_id(base_url, booking_id, token=actual_token)

    def filter(self, base_url: str, filters: dict):
        """Filter bookings based on provided criteria."""
        booking_manager = BookingManager(self.session)
        return booking_manager.filter_bookings(base_url, filters)

    def delete_booking_data(self, base_url: str, booking_id: int, token: str = None, exp_status=Response.StatusCode.HTTP_CREATED):
        """Delete a booking by ID."""
        actual_token = self._get_actual_token(token)
        if not actual_token:
            return None

        booking_manager = BookingManager(self.session)
        status_code, response_body, error = booking_manager.delete_booking(base_url, booking_id, token=actual_token)
        
        if error or status_code != exp_status:
            return None, error
        return status_code, response_body, None
