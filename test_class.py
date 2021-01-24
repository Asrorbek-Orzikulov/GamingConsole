"""Testing class for the Gaming Console."""


class TestSuite:
    """Create a suite of tests similar to unittest."""

    def __init__(self):
        """Create a test suite object."""
        self._total_tests = 0
        self._failures = 0

    def run_test(self, computed, expected, message=""):
        """Compare computed and expected.

        If not equal, print message, computed, expected.
        """
        self._total_tests += 1
        if computed != expected:
            msg = message + " Computed: " + str(computed)
            msg += " Expected: " + str(expected)
            print(msg)
            self._failures += 1

    def report_results(self):
        """Report back summary of successes and failures from run_test()."""
        msg = "Ran " + str(self._total_tests) + " tests. "
        msg += str(self._failures) + " failures."
        print(msg)
