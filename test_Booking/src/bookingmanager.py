import json
import os
from test_Booking.src.Request import Request

class BookingManager:
    def __init__(self, session):
        """Initialize BookingManager with session and set up URLs."""
        self.session = session
        self.booking_url = "/booking" 
        self.auth_url = "/auth"
        self.ping_url = "/ping"

    def ping(self, base_url: str):
        """Ping the server to check if it's reachable."""
        url = f"{base_url}{self.ping_url}"
        return Request.execute(Request.Operation.OPERATION_GET, url)

    def authorize(self, base_url: str):
        """Authorize a user and obtain a token."""
        url = f"{base_url}{self.auth_url}"
        payload = self._load_json_file('auth_payload.json')
        if payload is None:
            return None
        return Request.execute(Request.Operation.OPERATION_POST, url, payload=payload)

    def create_booking(self, base_url: str, token=None):
        """Create a new booking."""
        url = f"{base_url}{self.booking_url}"
        payload = self._load_json_file('booking_payload.json')
        if payload is None:
            return None
        return Request.execute(Request.Operation.OPERATION_POST, url, payload=payload, token=token)

    def update_booking(self, base_url: str,booking_id: str, payload, token=None):
        """Update an existing booking identified by booking_id."""
        url = f"{base_url}{self.booking_url}/{booking_id}"
        payload = payload
        if payload is None:
            return None
        return Request.execute(Request.Operation.OPERATION_PUT, url, payload=payload, token=token)

    def partial_update_booking(self, base_url: str,  booking_id: str, payload, token=None):
        """Partially update an existing booking identified by booking_id."""
        url = f"{base_url}{self.booking_url}/{booking_id}"
        payload = payload
        if payload is None:
            return None
        return Request.execute(Request.Operation.OPERATION_PATCH, url, payload=payload, token=token)

    def get_booking_ids(self, base_url: str, token=None):
        """Retrieve a list of booking IDs."""
        url = f"{base_url}{self.booking_url}"
        return Request.execute(Request.Operation.OPERATION_GET, url, token=token)

    def get_booking_by_id(self, base_url: str, booking_id: str, token=None):
        """Retrieve booking details by booking_id."""
        url = f"{base_url}{self.booking_url}/{booking_id}"
        return Request.execute(Request.Operation.OPERATION_GET, url, token=token)

    def filter_bookings(self, base_url: str, filters: dict, token=None):
        """Filter bookings based on the provided criteria."""
        query_string = Request.construct_param_filters(filters)
        url = f"{base_url}{self.booking_url}{query_string}"
        return Request.execute(Request.Operation.OPERATION_GET, url, token=token)

    def delete_booking(self, base_url: str, booking_id: str, token=None):
        """Delete a booking identified by booking_id."""
        url = f"{base_url}{self.booking_url}/{booking_id}"
        return Request.execute(Request.Operation.OPERATION_DELETE, url, token=token)

    def _load_json_file(self, file_path: str):
        """Load a JSON file from the specified path."""
        full_path = os.path.join('/Users', 'tn', 'Downloads', 'Pytest_framework-main', 'test_Booking', 'data_files', file_path)
        try:
            with open(full_path, 'r') as json_file:
                return json.load(json_file)
        except (FileNotFoundError, json.JSONDecodeError):
            return None 
