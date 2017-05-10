import unittest
from main import apply_input_checks, getopts
class PyLeleTest(unittest.TestCase):

    self.cmd_options = getopts(argv)

    def setUp(self):
        self.cmd_options = {'--duration': 15, '--start': '10-01-2017'}

    def apply_input_checks_test(self):
        assert(apply_input_checks(self.cmd_options)), "Correct cmd options failed to pass validation"

        self.cmd_options['--duration'] = "test"
        assert(apply_input_checks(self.cmd_options) == False), "Passed invalid duration, sanity checks failed to catch it"