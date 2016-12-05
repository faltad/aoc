def substract_lowest(values, f_direction, s_direction):
    if values[f_direction] > values[s_direction]:
        return f_direction, values[f_direction] - values[s_direction]
    return s_direction, values[s_direction] - values[f_direction]


def calc_distance(d, starting_position="north"):
    #first get a clean input: remove commas/spaces and add everyhting in a list
    data = [s.strip() for s in d.split(",")]

    #create a list with the 4 directions
    #beware, the order is important and respects the orientation
    directions = ["north", "east", "south", "west"]

    #then create a dict with the same directions and set them to 0
    dict_directions = {"north": 0, "east": 0, "south": 0, "west": 0 }

    current_position = starting_position
    #assume the input is always two characters at least: direction and number
    for step in data:
        direction = step[:1]
        number = int(step[1:])

        #find current position
        i = directions.index(current_position)

        #apply the rotation (remember the directions list is in order)
        if direction == "R":
            i += 1
        else:
            i -= 1
        current_position = directions[i if i < len(directions) else 0]

        dict_directions[current_position] += number

    #now that the loop is over, make the final calculations:
    #find the highest betweeen east and west, and subtract the lowest
    #to the highest to get the distance moved.
    #do the same for north/south.
    w_e_position, w_e_pos_value = substract_lowest(dict_directions, "west", "east")
    n_s_position, n_s_pos_value = substract_lowest(dict_directions, "north", "south")

    print ("For the data: %s" % (d))
    print ("%d to the %s" % (w_e_pos_value, w_e_position))
    print ("%d to the %s" % (n_s_pos_value, n_s_position))
    print ("Which gives us a result of %d" % (n_s_pos_value + w_e_pos_value))


test_data = [
    "R2, L3",
    "R2, R2, R2",
    "R5, L5, R5, R3",
    "R1, L3, R5, R5, R5, L4, R5, R1, R2, L1, L1, R5, R1, L3, L5, L2, R4, L1, R4, R5, L3, R5, L1, R3, L5, R1, L2, R1, L5, L1, R1, R4, R1, L1, L3, R3, R5, L3, R4, L4, R5, L5, L1, L2, R4, R3, R3, L185, R3, R4, L5, L4, R48, R1, R2, L1, R1, L4, L4, R77, R5, L2, R192, R2, R5, L4, L5, L3, R2, L4, R1, L5, R5, R4, R1, R2, L3, R4, R4, L2, L4, L3, R5, R4, L2, L1, L3, R1, R5, R5, R2, L5, L2, L3, L4, R2, R1, L4, L1, R1, R5, R3, R3, R4, L1, L4, R1, L2, R3, L3, L2, L1, L2, L2, L1, L2, R3, R1, L4, R1, L1, L4, R1, L2, L5, R3, L5, L2, L2, L3, R1, L4, R1, R1, R2, L1, L4, L4, R2, R2, R2, R2, R5, R1, L1, L4, L5, R2, R4, L3, L5, R2, R3, L4, L1, R2, R3, R5, L2, L3, R3, R1, R3"
]

for data in test_data:
    calc_distance(data)
