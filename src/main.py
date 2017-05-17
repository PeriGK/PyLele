from sys import argv
from datetime import datetime
from time import strptime


def getopts(argv):
    """Populates a dictionary with the names and values of the command line options"""
    assert (len(argv) % 2) != 0, "Please provide arguments in the format --arg value"
    opts = {}  # Empty dictionary to store key-value pairs.
    while argv:  # While there are arguments left to parse...
        if argv[0][0] == '-':  # Found a "-name value" pair.
            opts[argv[0]] = argv[1]  # Add key and value to the dictionary.
        argv = argv[1:]  # Reduce the argument list by copying it starting from index 1.
    return opts


def apply_defaults(cmd_options):
    """Apply default values in case no value has been passed"""
    if '--duration' not in cmd_options:
        # By default, use 9 months as duration
        cmd_options['--duration'] = 9
    else:
        cmd_options['--duration'] = int(cmd_options['--duration'])
    if '--start' not in cmd_options:
        # By default, use today as start date
        cmd_options['--start'] = datetime.today()
    return cmd_options


def normalise_cmd_input(cmd_options):
    """We are expecting values of type string, but we might need to convert them to pythonic date types"""
    if '--start' in cmd_options:
        # If the value is already of type datetime.datetime, there is no need to normalise it
        if str(type(cmd_options['--start'])) != "<class 'datetime.datetime'>":
            cmd_options['--start'] = datetime.strptime(cmd_options['--start'], '%d-%m-%Y')
    return cmd_options


def apply_input_checks(cmd_options):
    """Check if the parameters passed from the command line are in the expected format"""
    is_valid_input = True
    if '--duration' in cmd_options:
        is_valid_input = is_valid_input and cmd_options['--duration'].isnumeric()
    if '--start' in cmd_options:
        try:
            strptime(cmd_options['--start'], '%d-%m-%Y')
            is_valid_input = is_valid_input and True
        except:
            is_valid_input = is_valid_input and False
    return is_valid_input

def main():
    cmd_options = getopts(argv)

    if not apply_input_checks(cmd_options):
        assert(apply_input_checks(cmd_options)), "Not valid arguments were passed"

    cmd_options = apply_defaults(cmd_options)
    cmd_options = normalise_cmd_input(cmd_options)

    today = datetime.now()
    start_month = cmd_options['--start'].month
    start_date = cmd_options['--start']

    # The modulo division will return an integer representing a month index.
    # If the result is 0, this means it is December(12 % 12 =0)
    # If it is 1, then it is November and so on.
    # dismissal_month = 12 - ((start_month + cmd_options['--duration']) % 12)
    dismissal_month = (start_month + cmd_options['--duration'])
    if dismissal_month > 12:
        dismissal_month %= 12
    end_date = cmd_options['--start'].replace(month=dismissal_month)

    if dismissal_month < start_month:
        # Dismissal will happen next year
        current_year = cmd_options['--start'].year
        end_date = end_date.replace(year=current_year + 1)

    total_days_duty = end_date - start_date
    remaining_days = end_date - today

    # The string will be returned in a format XYZ days, hours:minutes:seconds
    # Make sure you only print and handle the days part
    total_days_duty = str(total_days_duty).split(",")[0]
    remaining_days = str(remaining_days).split(",")[0]
    remaining_days = remaining_days.split(" ")[0]

    print("*********************")
    print("Total days of duty will be: {}. {} days, plus today, remaining to get dismissed from the army".format(total_days_duty, remaining_days))
    print("*********************")

if __name__ == "__main__":
    main()
