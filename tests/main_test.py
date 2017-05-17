import unittest
from main import apply_input_checks, normalise_cmd_input, apply_defaults
from datetime import datetime


class PyLeleTest(unittest.TestCase):

    def test_apply_input_checks_legitimate_input(self):
        cmd_options = {'--duration': '15', '--start': '10-01-2017'}
        self.assertTrue(apply_input_checks(cmd_options), msg='Failed to assert legitimate input')

    def test_apply_input_checks_faulty_input(self):
        cmd_options = {'--duration': 'abc', '--start': '10-01-2017'}
        self.assertFalse(apply_input_checks(cmd_options), msg='Didnt fail on faulty input')

    def test_apply_input_checks_only_correct_date(self):
        cmd_options = {'--start': '10-01-2017'}
        self.assertTrue(apply_input_checks(cmd_options), msg='Failed to assert provided correct date')

    def test_apply_input_checks_bad_duration(self):
        cmd_options = {'--duration': 'abc'}
        self.assertFalse(apply_input_checks(cmd_options), msg='Didnt fail with wrong duration provided')

    def test_normalise_cmd_input_date_provided(self):
        cmd_options = {'--duration': '5', '--start': '10-10-2009'}
        cmd_options = normalise_cmd_input(cmd_options)
        self.assertTrue(cmd_options['--start'] == datetime(2009, 10, 10, 0, 0), msg='The date normalisation didnt '
                                                                                       'happen correctly.')
    def test_normalise_cmd_input_no_date_provided(self):
        cmd_options = {'--duration': '5'}
        cmd_options = normalise_cmd_input(cmd_options)
        date_exists = ('--start' in cmd_options)
        self.assertFalse(date_exists, msg='Date exists even though we didnt provide it')

    def test_apply_defaults_no_args_provided(self):
        cmd_options = {}
        cmd_options = apply_defaults(cmd_options)

        # We need to check default date datetime.today, with a small fault tolerance,
        # as the returned value is current and running.
        # Even a deviation of a nanosecond will make the program fail.
        # So we will check till the seconds match. Though, there is still an unlikely
        # case that this will fail, because the 2 commands might be apart, time-wise,
        # only a negligible time(like a few nanoseconds) but the latter command might execute in the next minute
        self.assertTrue(('--start' in cmd_options) and cmd_options['--start'].strftime('%d-%m-%Y %H:%M:%S') == datetime.today().strftime('%d-%m-%Y %H:%M:%S'),
                        msg='Failed to provide a default datetime')

    def test_apply_defaults_only_duration_provided(self):
        cmd_options = {'--duration': 9}
        cmd_options = apply_defaults(cmd_options)

        self.assertTrue(('--start' in cmd_options) and cmd_options['--start'].strftime('%d-%m-%Y %H:%M:%S') == datetime.today().strftime('%d-%m-%Y %H:%M:%S'),
                        msg='Failed to provide a default datetime having duration')