# Daily Temperature Log Analyzer

**Language:** Python · **Size:** Small · **Mode:** Practice the basics

A small weather station has an operator who types in temperature readings by hand throughout the day, one reading per line, finishing with the word "done". Sometimes the operator makes a typo and types something that isn't a number. The station wants a simple tool that tallies the valid readings, ignores the bad ones, and prints a quick summary so nobody has to do the math by hand.

**Goal:** Read temperature readings typed one per line until a "done" sentinel or end of input, skip bad entries without crashing, classify each valid reading, and print a summary report.

## Skills practiced

- Decisions and conditional logic
- Basic exception handling
- Functions and scope
- Input and type conversion
- Lists and sequence basics
- Loops and basic algorithms
- Operators and expressions
- Values, variables, output and types
- String processing

## Requirements

- Read lines from standard input one at a time, stopping as soon as a line equal to "done" (ignoring case and surrounding whitespace) is read, or stopping when there is no more input.
- Attempt to convert every other line into a floating-point temperature in Celsius; a line that cannot be converted must be counted as an invalid entry and skipped, without stopping the program.
- Classify each valid temperature into exactly one category: "Cold" for temperatures below 10, "Mild" for temperatures from 10 to 25 inclusive, and "Hot" for temperatures above 25, keeping a running count for each category.
- After input ends, print a summary report containing the count of valid readings, the count of invalid entries skipped, the average/minimum/maximum temperature (each formatted to one decimal place followed by the letter C), and the three category counts; if there were zero valid readings, print only a single message stating that no valid temperature readings were recorded.

## Deliverables

- The completed solution.py script
- The exact summary report printed to stdout for the given input

## Input

Standard input contains zero or more lines. Each line is either a number (integer or decimal, possibly negative, representing a Celsius temperature), some other text that is not a valid number, or the word "done" in any mix of upper/lower case with optional surrounding whitespace, which signals the end of the readings. Input may also simply end (no "done" line) to signal the end of readings.

## Output

If at least one valid reading was recorded, print exactly these eight lines, in this order:
Valid readings: <count>
Invalid entries skipped: <count>
Average temperature: <avg>C
Minimum temperature: <min>C
Maximum temperature: <max>C
Cold (<10C): <count>
Mild (10-25C): <count>
Hot (>25C): <count>
where <avg>, <min>, and <max> are formatted with exactly one digit after the decimal point.
If there were zero valid readings, print only:
No valid temperature readings were recorded.

## Constraints

- Use only the standard library; no file access, dictionaries, sets, comprehensions, regular expressions, classes, or datetime features.
- The program must not crash regardless of what text appears on a line; invalid lines are simply skipped.
- Do not print anything besides the specified report lines (or the single no-data message).
- Temperatures may be negative, zero, integers, or decimals.

## Example

**Input**
```
5
15
30
abc
22.5
10
25
done
```
**Output**
```
Valid readings: 6
Invalid entries skipped: 1
Average temperature: 17.9C
Minimum temperature: 5.0C
Maximum temperature: 30.0C
Cold (<10C): 1
Mild (10-25C): 4
Hot (>25C): 1
```

## Running it

```sh
python solution.py < input.txt
```

---
Built on [TrakCode](https://trakcode.com): passed every test, including hidden ones.
