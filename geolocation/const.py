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

NOT_IMPLEMENTED = 'Method is not implemented.'
