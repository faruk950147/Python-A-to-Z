def simpleInterest(principal, rate, time):
    # principal is the amount of money
    # rate is the interest rate
    # time is the time in years
    return (principal * rate * time) / 100

print(simpleInterest(100, 10, 1))
