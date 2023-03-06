def optimal_precast_pieces(manhole_height, precast_pieces):
    # Sort precast pieces in descending order
    precast_pieces.sort(reverse=True)

    # Create a list to store the counts of each precast piece used in the solution
    counts = [0] * len(precast_pieces)

    # Calculate the optimal solution
    for i in range(len(precast_pieces)):
        while manhole_height >= precast_pieces[i]:
            manhole_height -= precast_pieces[i]
            counts[i] += 1

    # Return the optimal solution as a list of tuples of (precast piece, count)
    optimal_pieces = []
    for i in range(len(precast_pieces)):
        if counts[i] > 0:
            optimal_pieces.append((precast_pieces[i], counts[i]))

    return optimal_pieces


manhole_height = 235
precast_pieces = [100, 50, 35, 10]

optimal_pieces = optimal_precast_pieces(manhole_height, precast_pieces)

print(optimal_pieces)
