from pprint import pprint

fts ={'09:35': 'FREEPORT',
	  '17:00': 'FREEPORT',
	  '09:55': 'WEST END',
	  '19:00': 'WEST END',
	 '10:45': 'TREASURE CAY',
	 '12:00': 'TREASURE CAY',
	 '11:45': 'ROCK SOUND',
	 '17:55': 'ROCK SOUND',}


dests = set(fts.values())

dests_of_flights = []
#for destination in dests:
#    dests_of_flights(destination) = []
for k, v in fts.items():
    if v == 'WEST END':
        dests_of_flights.append(k)

print(dests_of_flights)

dests_of_flights_1 = [k for k,v in fts.items() if v == 'WEST END']

print(dests_of_flights_1)


unique_dest_n_time = {}
for dest in dests:
    unique_dest_n_time[dest] = [k for k,v in fts.items() if v == dest]

pprint(unique_dest_n_time)

'''Generator of dictionaries with nested lists generator'''
unique_dest_n_time_2 = {dest: [k for k,v in fts.items() if v == dest] for dest in set(fts.values())}

pprint(unique_dest_n_time_2)
