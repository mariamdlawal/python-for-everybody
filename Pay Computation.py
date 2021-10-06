# create new function to calculate pay
def computepay(hours, rate):
    if hours > 40:
        print((40 * rate) + ((hours - 40) * (1.5 * rate)))
    else:
        print(hours * rate)


# check to assure user enters valid input
while True:
    try:
        x = int(input('Enter the number of hours you worked this week: '))
        y = int(input('Enter your hourly pay: '))
        break
    except ValueError:
        print('Please enter numbers only.')

computepay(x, y)
