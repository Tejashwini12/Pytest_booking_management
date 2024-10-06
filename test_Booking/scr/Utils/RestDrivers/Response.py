import requests


class Response:
    class StatusCode:
        HTTP_OK = 200
        HTTP_NOT_FOUND = 404
        HTTP_INTERNAL_ERROR = 500
        HTTP_CREATED =201

        # Add other status codes as needed

        @staticmethod
        def adjust_exp_status_if_custom(actual_status, exp_status):

            if exp_status == 'CUSTOM':
                return actual_status
            return exp_status

    def __init__(self, session):
        self.session = session

    def get(self, url, **kwargs):

        try:
            response = self.session.get(url, **kwargs)
            return self._process_response(response)
        except requests.RequestException as e:
            # Handle exceptions from the request
            return self._create_error_response(str(e))

    @staticmethod
    def _process_response(self, response):

        try:
            status = response.status_code
            error = response.json().get('error', None) if response.status_code != Response.StatusCode.HTTP_OK else None
            return status, response, error
        except ValueError as e:
            # Handle JSON decoding error
            return response.status_code, response, str(e)

    @staticmethod
    def _create_error_response(self, error_message):

        return None, None, error_message
