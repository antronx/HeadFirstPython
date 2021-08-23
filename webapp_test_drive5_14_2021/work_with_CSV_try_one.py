import os

import csv

import pprint


def convert2ampm(time24: str) -> str:
    return datetime.strptime(time24, '%H:%M').strftime('%I:%M%p')


from datetime import datetime

os.chdir('C:\dev\Python\HeadFirstTasks')

with open('csv_flight.csv') as data:
    ignore = data.readline()
    flights = {}
    for line in data:
        k, v = line.strip().split(',')
        flights[k] = v

pprint.pprint(flights)
print()

flights2 = {}

for k, v in flights.items():
    flights2[convert2ampm(k)] = v.title()

pprint.pprint(flights2)

more_dests = [dest.title() for dest in flights.values()]

print()

more_flights = {convert2ampm(k): v.title()
                for k, v in flights.items()
                if v.strip() == 'FREEPORT'}
pprint.pprint(more_flights)

'''Generator that transforms keys and values'''
