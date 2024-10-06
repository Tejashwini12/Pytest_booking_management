import logging
from test_Booking.scr.Utils.RestDrivers.Response import Response

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Assertion:

    @staticmethod
    def assert_equal(actual, expected, msg=""):
        if actual != expected:
            logger.error(msg or f"Assertion failed: Expected {expected}, but got {actual}")
            assert False, msg or f"Expected {expected} but got {actual}"
        else:
            logger.info(f"Assertion passed: Expected {expected}, and got {actual}")

    @staticmethod
    def _assert_common(func, **kwargs):

        exp_value = kwargs.get("exp_value")
        if exp_value is None:
            exp_value = kwargs.get("instance") or kwargs.get("exp_value_for_logger")

        actual_value = kwargs.get("actual_value")
        if actual_value is None:
            actual_value = kwargs.get("object") or kwargs.get("item")

        # Log details before performing the assertion
        logger.info(f"Performing assertion: actual_value={actual_value}, exp_value={exp_value}")

        # Perform the assertion and log details
        if kwargs.get("exp_value_for_logger") is not None:
            logger.info(f"Comparing actual value: {actual_value} with expected value: {exp_value}")
            func(actual_value, exp_value, msg=kwargs.get("msg"))
        elif kwargs.get("object") is not None and kwargs.get("instance") is not None:
            logger.info(f"Comparing actual object: {actual_value} with expected instance: {exp_value}")
            func(actual_value, exp_value, msg=kwargs.get("msg"))
        elif kwargs.get("item") is not None and kwargs.get("container") is not None:
            logger.info(f"Comparing actual item: {actual_value} with expected container: {exp_value}")
            func(actual_value, exp_value, msg=kwargs.get("msg"))
        else:
            logger.info(f"Comparing expected value: {exp_value} with actual value: {actual_value}")
            func(actual_value, exp_value, msg=kwargs.get("msg"))

    @staticmethod
    def response_status_should_be_equal(actual_status, exp_status, response, continue_on_failure=False):

        exp_status = Response.StatusCode.adjust_exp_status_if_custom(actual_status=actual_status, exp_status=exp_status)

        # Log the status codes being compared
        logger.info(f"Comparing actual status {actual_status} with expected status {exp_status}")

        # Perform the assertion
        Assertion._assert_common(
            func=Assertion.assert_equal,
            actual_value=actual_status,
            exp_value=exp_status,
            msg=f"Expected status {exp_status} but got {actual_status}"
        )

