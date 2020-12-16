def parse_field(field_string):
    name, ranges = field_string.split(": ")
    ranges = ranges.split(" or ")
    ranges = tuple(
        tuple(
            int(val) for val in range_.split('-')
        )
        for range_ in ranges
    )

    return {
        "field" : name,
        "ranges": ranges
    }


def parse_ticket(ticket_string):
    return tuple(int(val) for val in ticket_string.split(','))


def parse_tickets(tickets_string):
    fields, other = tickets_string.split("\n\nyour ticket:\n")
    your_ticket, nearby_tickets = other.split("\n\nnearby tickets:\n")
    fields = [parse_field(field) for field in fields.split('\n')]
    your_ticket = parse_ticket(your_ticket)
    nearby_tickets = [parse_ticket(tick) for tick in nearby_tickets.split('\n')]

    return {
        'your_ticket'   : your_ticket,
        'fields'        : fields,
        'nearby_tickets': nearby_tickets
    }


def find_invalid_values_in_ticket(ticket, fields):
    vals = []
    for val in ticket:
        invalid = True
        for field in fields:
            for min, max in field["ranges"]:
                if min <= val <= max:
                    invalid = False
                    break
            if not invalid:
                break
        if invalid:
            vals.append(val)

    return vals


def find_invalid_values(info):
    tickets = info["nearby_tickets"]
    fields = info["fields"]

    invalid_vals = []
    for ticket in tickets:
        vals = find_invalid_values_in_ticket(ticket, fields)
        invalid_vals.extend(vals)

    return invalid_vals


with open('tickets.txt', 'r') as file:
    in_str = file.read()

ticket_info = parse_tickets(in_str)
invalid_values = find_invalid_values(ticket_info)
print(sum(invalid_values))

exit(0)
