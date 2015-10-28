import requests
from geolocation.exceptions import ApiClientException


class ResponseValidator(object):
    """Response's validator for Google API statuses and request's standard statuses."""
    STATUS_OK = 'OK'
    STATUS_ZERO_RESULTS = 'ZERO_RESULTS'
    STATUS_OVER_QUERY_LIMIT = 'OVER_QUERY_LIMIT'
    STATUS_REQUEST_DENIED = 'REQUEST_DENIED'
    STATUS_INVALID_REQUEST = 'INVALID_REQUEST'
    STATUS_UNKNOWN_ERROR = 'UNKNOWN_ERROR'

    STATUS_CODES = (
        (STATUS_OK, 'Successfully parsed.'),
        (STATUS_ZERO_RESULTS, 'Successful parsed but returned no results.'),
        (STATUS_OVER_QUERY_LIMIT, 'Over your quota.'),
        (STATUS_REQUEST_DENIED, 'Request was denied.'),
        (STATUS_INVALID_REQUEST, 'Query is missing.'),
        (STATUS_UNKNOWN_ERROR, 'Request could not be processed due to a server'
                               'error. Try again.'),
    )

    status_code = None

    def __init__(self, response):
        """Method calls main validation."""
        self.validation(response)

    def __repr__(self):
        return '<ResponseValidator: %s>' % self.status_code

    def validate_response_status(self, response):
        """Method validates only request's response status."""
        self.status_code = response.status_code
        if self.status_code != requests.codes.ok:
            message = '%s %s' % (self.status_code, response.reason)
            raise ApiClientException(message)
        return self.status_code

    def validate_google_status(self, response):
        """Method validates only google's status."""
        self.status_code = response.json()['status']
        if self.status_code != self.STATUS_OK:
            message = '%s' % dict(self.STATUS_CODES).get(self.status_code)
            raise ApiClientException(message)
        return self.status_code

    def validation(self, response):
        """
        Method validates response. Validates request's statuses as first call.
        Next call is responsible for google's internal statuses.
        """
        self.validate_response_status(response)
        self.validate_google_status(response)
