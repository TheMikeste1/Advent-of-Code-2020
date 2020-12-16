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
    return tuple(int(val) for val in ticket_string.split(',') if val)


def parse_tickets(tickets_string):
    fields, other = tickets_string.split("\n\nyour ticket:\n")
    your_ticket, nearby_tickets = other.split("\n\nnearby tickets:\n")
    fields = [parse_field(field) for field in fields.split('\n')]
    your_ticket = parse_ticket(your_ticket)
    nearby_tickets = [
        parse_ticket(tick) for tick in nearby_tickets.split('\n') if tick
    ]

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


def find_invalid_tickets(info):
    tickets = info["nearby_tickets"]
    fields = info["fields"]

    invalid_tickets = []
    for ticket in tickets:
        if find_invalid_values_in_ticket(ticket, fields):
            invalid_tickets.append(ticket)

    return invalid_tickets


def find_valid_fields(ticket, fields):
    valid_fields = []
    for val in ticket:
        valids = []
        for field in fields:
            for min, max in field["ranges"]:
                if min <= val <= max:
                    valids.append(field["field"])
                    break
        valid_fields.append(valids)
    return valid_fields


def determine_field_ordering(info):
    # Generate the possibilities
    possibles = [name['field'] for name in info["fields"]]
    possibles = [possibles for _ in range(len(info["fields"]))]
    ordering = [None] * len(info["fields"])

    # Parse all ticket and values to determine which fields could be what
    for ticket in info["nearby_tickets"]:
        valid_fields = find_valid_fields(ticket, info["fields"])
        # Remove invalid fields from ordering
        for field_id, possibilities in enumerate(possibles):
            possibles[field_id] = [
                name for name in possibilities if name in valid_fields[field_id]
            ]

    # If there is only one possibility left for some field, remove it
    # from all others. Keep going until we're done.
    temp = None
    while temp != ordering:
        temp = [val for val in ordering]  # Make a copy
        for field_id, possibilities in enumerate(possibles):
            if len(possibilities) == 1:
                field = possibles[field_id][0]
                ordering[field_id] = field
                for possibilities in possibles:
                    if field in possibilities:
                        possibilities.remove(field)

    return ordering


def get_answer(ticket, ordering):
    total = 1
    for i, field in enumerate(ordering):
        if "departure" in field:
            total *= ticket[i]
    return total if total != 1 else None


with open('tickets.txt', 'r') as file:
    in_str = file.read()

ticket_info = parse_tickets(in_str)
invalid_tickets = find_invalid_tickets(ticket_info)
for ticket in invalid_tickets:
    ticket_info["nearby_tickets"].remove(ticket)

field_ordering = determine_field_ordering(ticket_info)
answer = get_answer(ticket_info["your_ticket"], field_ordering)
print(answer)

exit(0)
