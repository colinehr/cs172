# Project: Segregation Simulation
This is a programming project. You may work with another person, but you should submit your own code. Please specify any additional people you work with upon submission.

## Overview
Implement Schelling's model of segregation, as described in [Frank McCown's assignment](http://nifty.stanford.edu/2014/mccown-schelling-model-segregation/).

Your program should behave like the example embedded in the web page above. Use a smaller grid size (e.g., 20×20) but otherwise use the same default parameters (similarity at 30%, red/blue ratio at 50%, and empty/total ratio at 10%). At the end of the simulation, please print the number of rounds it took to get to 100% satisfaction to the terminal.

At each step, you should find all of the unsatisfied agents and then move each unsatisfied agent to a random unoccupied cell. Agents are allowed to move to cells that became vacant in the same round.

Clarification: an agent with no neighbors is satisfied.

You don't have to provide buttons or sliders, and you don’t need to implement the ability to stop or start; it should just start when the window opens. I should be able to change each parameter by changing it in one place in your program.

You don't have to implement any variants, just the basic version.

As with all projects, you have the opportunity to break your logic up into functions. You should not have one large main function. Try to make your code readable, using appropriate variable and function names to communicate their purpose. Use test-driven development to create each function.

## Rubric

- **Excellent (E):** The work exceeds the expectations of the assignment. Deep understanding of the concepts is evident. There are no nontrivial errors. Your code is readable, well-structured, and well-written. Code is cleanly divided into appropriately named functions, and input and output types for functions are given. Each function has a docstring written for it, and other more complicated parts of the code are explained with comments. For each function, enough tests have been written to ensure functionality (including corner cases), and all tests pass. This work could be used as an in-class example.
- **Meets Expectations (M):** Understanding of the concepts is evident. Code is correct and understandable. The logic of the code is broken up into functions, and each function has tests, but some revision or expansion is needed. No additional instruction is needed.
- **Revision Needed (R):** Program appears to be functional, but little to no tests have been written. There may be some bugs still left in the code. The logic of the code is difficult to follow; there either aren't enough functions or the functions are not breaking up the code in a logical way. The code shows only partial understanding of concepts and needs further work or more review.
- **Not Assessable (N):** The code does not work or does not satisfy the program specification. There is not enough to accurately assess understanding of concepts and code writing ability. Or, there are simply too many mistakes to justify correcting each one separately.

## What To Hand In

Hand in your main program `segregation.py` and your test class `segregation_test.py`.

Include your name and any other people you worked with in the `__author__` variable at the top of your code. For example, if I worked with Alain, the first line of my code would be
```python
__author__ = "Colin Ehr and Alain Kägi"
```
