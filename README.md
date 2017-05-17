# PyLele
Simple script to calculate the days remaining till the dismissal from the Greek army. A must for Greek soldiers who just cant help it and counting their remaining days :)

The name of the app comes from the words "Py" which implies the script is written in Python and "Lele" which is a military Greek slang word to say "I am dismissed".

You can use it as follows:


```
git clone git@github.com:PeriGK/PyLele.git
cd PyLele/src
python3 main.py [--start: date joined the army] [--duration: number of months]
```

# Example:
python3 main/py --start 10-01-2015 --duration 12
This means that we joined the army in January 10th, 2015 and our duty is supposed to last for 15 months


# Notes:
Works and tested only with python3
Both parameters are optional. Their default values are:
--start:    today's date
--duration: 9(months)
