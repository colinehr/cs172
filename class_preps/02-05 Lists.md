# Class Prep for Monday, February 4th

## Reading

- [Pythonorama &mdash; Arrays](https://github.com/alainkaegi/pythonorama/blob/main/data_structures/arrays.md)
- [Sedgewick and Wayne &mdash; 1.4: Arrays](https://introcs.cs.princeton.edu/python/14array/)

## Assignment

Change the code to your `distance` function we wrote in class to take two lists of floats that have the same length and compute the distance between them, thinking of each list as a point in $n$ dimensions. The formula for the distance between two $n$-dimensional points $x$ and $y$ is
$$ d = \sqrt{(y_1 - x_1) + (y_2 - x_2) + \dots + (y_n - x_n)} $$
where $x_1, \dots, x_n$ are the coordinates of the point $x$, and $y_1, \dots, y_n$ are the coordinates of the point $y$. 

**Extra challenge:** Allow the user to input each point as numbers separated by spaces, and print a message to the user if the inputs have different lengths. For example, the terminal after running the program might look like:
```
What is the first point? 0 0 0
What is the second point? 1 1 1
1.7320508075688772
```

## Turning in

Upload your `.py` file to the corresponding Google Classroom assignment.