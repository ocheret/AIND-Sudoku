assignments = []

def cross(major, minor):
    """Cross product of elements in A and elements in B.
    Args:
        major(string) - string of labels for major axis
        minor(string) - string of labels for minor axis
    Returns:
        list of strings for every combination of major and minor labels
    """
    return [a + b for a in major for b in minor]

def chunks(l, n):
    """Partition l into n-sized chunks."""
    return [l[i:i+n] for i in range(0, len(l), n)]

# Column labels
column_labels =  '123456789'

# Row labels
row_labels = 'ABCDEFGHI'

# Valid digits
digits = '123456789'

# Lables for all boxes in the puzzle
boxes = cross(row_labels, column_labels)

# All row units
row_units = [cross(row, column_labels) for row in row_labels]

# All column units
column_units = [cross(row_labels, col) for col in column_labels]

# All box units
box_units = [cross(a, b) for a in chunks(row_labels, 3) for b in chunks(column_labels, 3)]

# All diagonal units
diagonal_units = [[a+b for a,b in zip(row_labels, column_labels)],
                  [a+b for a,b in zip(row_labels, column_labels[::-1])]]

# All units
all_units = row_units + column_units + box_units + diagonal_units

# Mapping from boxes to units
units = dict((box, [unit for unit in all_units if box in unit]) for box in boxes)

# Mapping from boxes to peers
peers = dict((box, set(sum(units[box], [])) - set([box])) for box in boxes)

def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    """
    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values



def naked_twins(values):
    """Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """
    for unit in all_units:
        # Find all instances of naked twins
        pairs = [values[box] for box in unit if len(values[box]) == 2]  # Find all 2 characer values
        twins = [pair for pair in set(pairs) if pairs.count(pair) == 2] # Find all twins

        # Eliminate the naked twins as possibilities for their peers
        for twin in twins:
            for box in unit:
                if values[box] != twin:
                    assign_value(values, box, values[box].replace(twin[0], '').replace(twin[1], ''))
    return values

def grid_values(grid):
    """
    Convert grid into a dict of {square: char} with '123456789' for empties.
    Args:
        grid(string) - A grid in string form.
    Returns:
        A grid in dictionary form
            Keys: The boxes, e.g., 'A1'
            Values: The value in each box, e.g., '8'. If the box has no value, then the value will be '123456789'.
    """
    return dict(zip(boxes, [(lambda x: x if x in digits else digits)(c) for c in grid ]))

def display(values):
    """
    Display the values as a 2-D grid.
    Args:
        values(dict): The sudoku in dictionary form
    """
    # Figure out the max width of each column
    widths = list(map(max, [[1 + len(values[b])for b in c] for c in column_units]))
    horizontal_line = '+'.join(map(lambda width: '-' * (width + 1), map(sum, chunks(widths, 3))))
    horizontal_line = horizontal_line[1:-1]
    for r in row_labels:
        print(''.join([values[r + str(c + 1)].center(widths[c]) + ('| ' if c in [2, 5] else '') for c in range(9)]))
        if r in ['C', 'F']:
            print(horizontal_line)

def eliminate(values):
    # Write a function that will take as an input, the sudoku in dictionary form,
    # run through all the boxes, applying the eliminate technique,
    # and return the resulting sudoku in dictionary form.
    for s, v in values.items():
        if (len(v) == 1):
            for p in peers[s]:
                assign_value(values, p, values[p].replace(v, ''))
    return values

def only_choice(values):
    # Write a function that will take as an input, the sudoku in dictionary form,
    # run through all the units, applying the only choice techniqnue,
    # and return the resulting sudoku in dictionary form.
    digits = list(str(x) for x in range(10))
    for u in all_units:
        for d in digits:
            occurrences = [b for b in u if d in values[b]]
            if len(occurrences) == 1:
                assign_value(values, occurrences[0], d)
    return values

def reduce_puzzle(values):
    solved_values = [box for box in values.keys() if len(values[box]) == 1]
    stalled = False
    while not stalled:
        # Check how many boxes have a determined value
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])
        # Your code here: Use the Only Choice Strategy
        values = only_choice(values)
        values = eliminate(values)
        values = naked_twins(values)
        # Check how many boxes have a determined value, to compare
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        # If no new values were added, stop the loop.
        stalled = solved_values_before == solved_values_after
        # Sanity check, return False if there is a box with zero available values:
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values

def search(values):
    "Using depth-first search and propagation, create a search tree and solve the sudoku."
    # First, reduce the puzzle using the previous function
    values = reduce_puzzle(values)
    if values is False:
        return False
    if all(len(values[x]) == 1 for x in boxes):
        return values

    # Chose one of the unfilled square s with the fewest possibilities
    size_list = [(b, len(v)) for b, v in values.items() if len(v) > 1]
    fewest_box = ''
    fewest_nums = 10
    for box, nums in size_list:
        if nums < fewest_nums:
            fewest_box = box
            fewest_nums = nums

    # Now use recursion to solve each one of the resulting sudokus, and if one returns a value (not False), return that answer!
    for c in values[fewest_box]:
        values_copy = values.copy()
        assign_value(values_copy, fewest_box, c)
        result = search(values_copy)
        if result is not False:
            return result

    return False

def solve(grid):
    """
    Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.
    """
    values = grid_values(grid)
    display(values)
    search(values)
    return values

if __name__ == '__main__':
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(solve(diag_sudoku_grid))

    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
