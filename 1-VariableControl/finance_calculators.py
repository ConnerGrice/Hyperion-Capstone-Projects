"""
A finance calculator that can do investment calculations or bond calculations

User selects which type of calculator they want
    -Investment
    -Bond

if investment
    - Input principle amount
    - input interest rate
    - input years of investment
    - Select either simple or compound interest types
    if simple
        - Calculate total amount in account
        - Use principle * yearsof investment * (1 + interest rate)
    if compound
        - Calculate total amount in account
        - Use principle*(1 + interest rate)^years
if bond
    - Input house value
    - Input interest rate
    - Input months to repay

    - Calculate total amount to repay
    - Use (interest rate*house value)/(1 - (1 + interest rate)^(-months))
"""

#A function that will convert a string into all caps and remove any trailing "." or spaces
def clean(word):
    #Convert to uppercase
    word = word.upper()

    #Strip trailing spaces or "."
    word = word.strip(". ")

    return word


#Gets user selection for the type of calculator that is wanted and cleans it
print("Please select and investment type: ")
print("Investment:\tUsed to calculate the amount you'll earn on your investment ")
print("Bond:\t\tUsed to calculate the amount you'll have to pay on your home loan")
calType = input("Selection: ")
calType = clean(calType)

#Checks the users selection
#Investment calculator
if calType == "INVESTMENT":

    #Gets initial investment
    principle = float(input("Initial investment (£): "))

    #Gets interest rate as a percentage and converts it into a decimal
    rate = float(input("Interest rate (%): "))
    rate = rate/100

    #Gets time the user wants to invest
    time = float(input("Number of years of investment: "))

    #Gets interest type selection
    print()
    print("Please select either 'simple' or 'compound' interest")
    print("Simple:\t\t Interest is calculated using initial investment amount.")
    print("Compound:\t Interest is calculated every year using the accumulated amount.")
    interest = input("Selection: ")
    interest = clean(interest)
    print()

    #Checks which type was selected
    #Simple interest
    if interest == "SIMPLE":

        #Calculates final amount as simple interest
        amount = round(principle*(1+rate)*time,2)
        print(f"Initial investment: £{principle}\nTime of investment: {time} years\nInterest rate: {rate*100}%\nTotal at the end: £{amount}")

    #Compound interest
    elif interest == "COMPOUND":

        #Calculates final amount as compound interest
        amount = round(principle*(1+rate)**time,2)
        print(f"Initial investment: £{principle}\nTime of investment: {time} years\nInterest rate: {rate*100}%\nTotal at the end: £{amount}")
    
    #Wrong input format
    else:
        print("Please enter only 'simple' or 'compound' when choosing a type.")

#Bond calculator
elif calType == "BOND":

    #Gets value of the home
    principle = float(input("House value (£): "))

    #Gets interest rate and converts it into a decimal
    rate = float(input("Interest rate (%): "))
    rate = rate/100

    #Gets time for user to pay back bond
    time = float(input("Number of months to pay off: "))

    #Calculates total amount to be payed after given timeframe
    num = rate*principle
    den = 1 - (1+rate)**(-time)
    amount = round(num/den,2)
    print(f"Initial house price: £{principle}\nTime to pay off bond: {time} months\nInterest rate: {rate*100}%\n Total amount to pay: £{amount}")

#Wrong input format
else:
    print("Please enter either 'investment' or 'bond'")

