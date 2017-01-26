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

    # Find all instances of naked twins
    # Eliminate the naked twins as possibilities for their peers

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
    pass

def only_choice(values):
    pass

def reduce_puzzle(values):
    pass

def search(values):
    pass

def solve(grid):
    """
    Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.
    """
    board = grid_values(grid)
    display(board)
    pass

if __name__ == '__main__':
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(solve(diag_sudoku_grid))

    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
