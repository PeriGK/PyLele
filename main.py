# Parse the options: --duration, --start
# Sanity checks: Valid dates, start, UT
from sys import argv
from datetime import datetime

def getopts(argv):
    opts = {}  # Empty dictionary to store key-value pairs.
    while argv:  # While there are arguments left to parse...
        if argv[0][0] == '-':  # Found a "-name value" pair.
            opts[argv[0]] = argv[1]  # Add key and value to the dictionary.
        argv = argv[1:]  # Reduce the argument list by copying it starting from index 1.
    return opts


def apply_defaults(cmd_options):
    if '--duration' not in cmd_options:
        # By default, use 9 months as duration
        cmd_options['--duration'] = 9
    if '--start' not in cmd_options:
        # By default, use today as start date
        cmd_options['--start'] = datetime.today()
    return cmd_options


def normalise_input(cmd_options):
    if '--start' in cmd_options:
        cmd_options['--start'] = datetime(cmd_options['--start'], '%Y-%m-%d')
    return cmd_options


def usage():
    pass



cmd_options = getopts(argv)

if '--help' in cmd_options:
    usage()

cmd_options = apply_defaults(cmd_options)
cmd_options = normalise_input(cmd_options)

start_month = cmd_options['--start'].month
start_date = cmd_options['--start']

dismissal_month = (start_month + cmd_options['--duration']) % 12


end_date = cmd_options['--start'].replace(month=dismissal_month)

if dismissal_month < start_month:
    # Dismissal will happen next year
    current_year = cmd_options['--start'].year
    end_date = end_date.replace(year=current_year + 1)

diff = (end_date - start_date)


str_diff = str(diff).split(",")[0]
days = str_diff.split(" ")[0]

days = int(days) - 1

print("*********************")

print(str(days) + " days, plus today, remaining to get dismissed from the army")

print("*********************")


