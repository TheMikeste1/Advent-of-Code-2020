from crt_solver import crt_solver

with open("departure_notes.txt", 'r') as file:
    bus_ids = file.read().split('\n')[1].split(',')

# The position in the incoming array is the remainder for the number.
# Therefore, we subtract the remainder from the incoming ID in order to find
# what the actual remainder is. This is the time the bus would need to leave prior
# to the number in order to be there on time.
bus_ids = [(int(id_), int(id_) - i) for i, id_ in enumerate(bus_ids) if id_.isnumeric()]
value = crt_solver(*bus_ids)

print(value)

exit(0)
