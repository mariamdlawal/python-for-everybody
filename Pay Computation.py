# create new function to calculate pay
def computepay(hours, rate):
    if hours > 40:
        pay = (40 * rate) + ((hours - 40) * (1.5 * rate))
        print(pay)
    else:
        pay = hours * rate
        print(pay)


# check to assure user enters valid input
while True:
    try:
        x = int(input('Enter the number of hours you worked this week: '))
        y = int(input('Enter your hourly pay: '))
        break
    except ValueError:
        print('Please enter numbers only.')

computepay(x, y)


# future ideas
# 1. take in a list of hours and rates and print out pays for each one
# 2. print out monthly and salaried pay based on the input
