import sys
import unittest

from tester.week5_selenium.selenium_login_tests import LoginTests


def main():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(LoginTests)
    result = unittest.TextTestRunner(verbosity=2).run(suite)

    print("\nRegression summary")
    print(f"Run:      {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors:   {len(result.errors)}")

    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    sys.exit(main())
