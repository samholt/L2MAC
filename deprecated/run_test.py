import unittest
from test_suite.system_design_tests import TestSystemDesign

if __name__ == "__main__":
    # Load the test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSystemDesign)

    # Run the tests
    unittest.TextTestRunner().run(suite)