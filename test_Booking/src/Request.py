import requests

class Request:
    class Operation:
        OPERATION_GET = 'GET'
        OPERATION_POST = 'POST'
        OPERATION_PATCH = 'PATCH'
        OPERATION_DELETE = 'DELETE'
        OPERATION_PUT = 'PUT'

    @staticmethod
    def execute(operation, url, payload=None, token=None):
        """Executes an HTTP request based on the operation type."""

    
        headers = {
            "User-Agent": "PostmanRuntime/7.41.2",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive"
        }
        if token:
            headers["Cookie"] = f"token={token}"

        try:
            # Execute the appropriate HTTP request based on the operation type
            if operation == Request.Operation.OPERATION_GET:
                response = requests.get(url, headers=headers, json=payload, verify=False)
            elif operation == Request.Operation.OPERATION_POST:
                response = requests.post(url, headers=headers, json=payload, verify=False)
            elif operation == Request.Operation.OPERATION_PATCH:
                response = requests.patch(url, headers=headers, json=payload, verify=False)
            elif operation == Request.Operation.OPERATION_DELETE:
                response = requests.delete(url, headers=headers, json=payload, verify=False)
            elif operation == Request.Operation.OPERATION_PUT:
                response = requests.put(url, headers=headers, json=payload, verify=False)
            else:
                raise ValueError(f"Unsupported operation: {operation}")

            response.raise_for_status()  # Raise an exception for HTTP errors

            # Handle responses based on content type
            content_type = response.headers.get("Content-Type", "")
            if "text/plain" in content_type:
                return response.status_code, response.text.strip(), None
            elif "application/json" in content_type:
                return response.status_code, response.json(), None
            else:
                return response.status_code, response.content, None 

        except requests.exceptions.RequestException as e:
            # Handle request exceptions and return None, None, error message
            return None, None, str(e)

    @staticmethod
    def construct_param_filters(filters):
        """Constructs a query string from the provided filters."""
        query_params = []

        # Filter by first name and last name
        if 'firstname' in filters and 'lastname' in filters:
            query_params.append(f"firstname={filters['firstname']}&lastname={filters['lastname']}")

        # Filter by check-in and check-out dates
        if 'checkin' in filters and 'checkout' in filters:
            query_params.append(f"checkin={filters['checkin']}&checkout={filters['checkout']}")

        # Join the parameters with '&' and return the final query string
        return '?' + '&'.join(query_params) if query_params else ''
