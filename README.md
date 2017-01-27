# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver

# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?  
A: The naked twins problem is a specialization of the more general
naked tuples problem, which is what was implemented for this
assignment. This represents the constraint that if N boxes in a unit
share the same list of N possible values, then none of the other boxes
in that unit can possibly take on any of the N possibilities. This is
easily implemented in the function naked_tuples which identifies the
tuples and eliminates the appropriate values from the rest of the
unit. This represents another constraint similar to the 'only choice'
and 'eliminate' strategies implemented previously.  This means that it
can be applied along with the other constraint propagation strategies,
during the iterative reduction step in 'reduce_puzzle'. This
repeatedly applies the constraints until no more changes are observed.

# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?  
A: The diagonal sudoku problem is a simple extension of the regular
sudoku problem where two new units corresponding to the two diagonals
are introduced. By adding these units to the complete list of units
the code naturally applies all contraints to the new units. No other
code needs to be modified to support this.

### Install

This project requires **Python 3**.

We recommend students install [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project. 
Please try using the environment we provided in the Anaconda lesson of the Nanodegree.

##### Optional: Pygame

Optionally, you can also install pygame if you want to see your visualization. If you've followed our instructions for setting up our conda environment, you should be all set.

If not, please see how to download pygame [here](http://www.pygame.org/download.shtml).

### Code

* `solutions.py` - You'll fill this in as part of your solution.
* `solution_test.py` - Do not modify this. You can test your solution by running `python solution_test.py`.
* `PySudoku.py` - Do not modify this. This is code for visualizing your solution.
* `visualize.py` - Do not modify this. This is code for visualizing your solution.

### Visualizing

To visualize your solution, please only assign values to the values_dict using the ```assign_values``` function provided in solution.py

### Data

The data consists of a text file of diagonal sudokus for you to solve.