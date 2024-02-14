# Assignment: Powerball

## Assignment Description

Write a program which will let the user input a Powerball ticket and return some statistics about how much money would be made if the lottery was played 10000 times with that ticket.

## Inputs and Outputs

The user should be able to input a ticket in the terminal. Here is an example of what the terminal could look like after input:
```
Choose 5 numbers from 1 to 69: 1 54 31 7 46
Choose 1 number from 1 to 26: 23
```
As you can see, the prompt should be on two lines, one which takes the regular numbers and one which takes the powerball. Assume numbers are separated by a single space.

If the user gives not enough or too many numbers, or if any numbers are outside the specified ranges (1-69 for regulars, 1-26 for powerball), print an informative error message.

The program should print the amount of total money made after simulating 10000 random draws as well as the average amount of money made per draw. An example of this might be:
```
Total earnings: $8764
Average earnings per draw: $0.88
```

## Prize Table

| Regular matches | Powerball match | Earnings     |
|-----------------|-----------------|--------------|
| 5               | yes             | $285 million |
| 5               | no              | $1 million   |
| 4               | yes             | $50,000      |
| 4               | no              | $100         |
| 3               | yes             | $100         |
| 3               | no              | $7           |
| 2               | yes             | $7           |
| 1               | yes             | $4           |
| 0               | yes             | $4           |

If a result occurs and isn't on this list, you win $0.

## Submission

Upload your `powerball.py` file to the Google Classroom.