# CodingBat: Programming Exercises for Python

This folder contains the CodingBat exercises for CS172 in Python. These exercises are very heavily based on the [CodingBat](https://codingbat.com/) exercises by Nick Parlante of Stanford.

Each exercise is given in the form of a Python function with a given "signature" that gives the names and types of associated variables as well as the type of the output. Your goal is to complete the function using the description attached to it, and give back the answer using the `return` command.

For example, consider the following problem:
```python
# Return True if both a and b are False, otherwise return False.
def ab_false(a: bool, b: bool) -> bool:
    pass
```
The signature tells us that we have two variables, `a` and `b`, which will each be `bool`s, and that we need to create and return another `bool` which is only True when both `a` and `b` are False. (Note: the `pass` keyword is only there so that the Python interpreter doesn't give an error: it is a keyword that does nothing, so we use it as a placeholder.) One possible solution is given by
```python
# Return True if both a and b are False, otherwise return False.
def ab_false(a: bool, b: bool) -> bool:
    return not a and not b
```

## Editing and running code

To complete a Codingbat assignment in VS Code, go to File > Open Folder and open this folder (`cs172/assignments/codingbat`). This will ensure that VS Code sees the relevant settings and configure itself automatically. Then go to the `codingbat` folder and open the relevant Python file. For example, if you're completing Warmup 1, you'll open the `warmup1.py` file and edit it directly (do not copy it into somewhere else!).

## Testing

These exercises also come with prepared *tests* to see if your code functions the way it should. To run a test using VS Code, go to the "Testing" tab on the left-hand side (the one that looks like a test tube). Then find the appropriate `test` folder (for example, if you're working through `warmup1`, the folder will be called `test_warmup1`) and run the tests associated with the problem by hitting the "play" button next to it. If we wanted to test our solution to `ab_false`, we would run the `test_ab_false` series of tests. If a test passes, it will appear with a green checkmark; if one fails, it will appear with a red X. The output of the test will give helpful infomation about why our test failed, and can be useful to understand how to fix our code.

## Turning in

To turn in a Codingbat assignment, first run all relevant tests to make sure everything is correct; then upload the relevant Python file to the given Google Classroom assignment. (For example, if you're completing Warmup 1, you will upload your `warmup1.py` file to the "CodingBat: Warmup 1" assignment and hit Submit.)