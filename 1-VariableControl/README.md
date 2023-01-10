# Hyperion-Capstone-1-FinancialCalculator

A simple command-line multi-use calculator that can be used to calculate the money gained on an investment or the amount you would have to pay back on a house loan. This was the first capstone project during my Hyperion Development Data Science Bootcamp.

## Features

### Investment calculator

This mode can calculate the total amount of money in the users back after a specified number of years given a fixed interest rate.
There are two types of interest that can be used in the calculation:

Type|Description|Equation
---|---|---
Simple|Intrest is added by only taking into account the initial investment|$B = P(1+I)t$
Compound|Interest is added using the running total within the account|$B = P(1+I)^t$

**Note:** $B$ is the balance after a given number of years, $t$, at an interest rate of $I$

### Bonds

This mode can calculate the amount that will need to be paid back on a house loan of a fixed interest rate and an estimated time for payback to be complete.
Type|Description|Equation
---|---|---
Bond|The compound interest rate on a loan|$B = PI(1+I)^t$

**Note:** $B$ is the total amount that will need to be paid in $t$ months, at an interest rate of $I$ for a house that cost £$P$

## Usage

Run the program via the terminal using:

```sh
python finance_calculators.py
```

Once the program is run, you will be given a menu to decide which calculator you want to use.

```console
Investment: Used to calculate the amount you'll earn on your investment
Bond:       Used to calculate the amount you'll have to pay on your home loan
Selection: 
```

### Investment

The user can input `investment` to select the investment mode, which then brings up the next set of user inputs, asking to specify:

```console
Initial investment (£): 
Interest rate (%):
Number of years of investment: 
```

After inputting these values, the user will be asked to pick between simple or compound interest.

```console
Please select either 'simple' or 'compound' interest
Simple:     Interest is calculated using initial investment amount.
Compound:   Interest is calculated every year using the accumulated amount.
Selection:
```

The user can then choose between `simple` or `compound` to get the desired output.

### Bond

The user can input `ibond` to select the bond mode, which brings up the next set of user inputs, asking to specify:

```console
House value (£):
Interest rate (%):
Number of months to pay off: 
```

Once the user has entered these values, the total amount that will need to be paid back will be displayed.
