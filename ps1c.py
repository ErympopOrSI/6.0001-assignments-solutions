
def house_hunting(annual_salary):

    monthly_salary = annual_salary / 12
    semi_annual_raise = 0.07
    portion_down_payment = 0.25 * 1000000

    current_savings = 0
    low = 0
    high = 10000

    guess = (low + high) / 2
    difference = 250000 # the initial difference is obviously 250k, [ portion_down_payment - current_savings ]
    step = 0

    while difference > 100:
        step += 1
        for month in range(1, 37):
            current_savings += current_savings * 0.04 / 12
            current_savings += (guess / 100) * monthly_salary

            if month % 6 == 0:
                monthly_salary += (monthly_salary * semi_annual_raise)

        difference = current_savings - portion_down_payment

        if difference > 100:
            high = guess
        if difference < 0:
            low = guess
        
        difference = abs(difference)

        guess = (low + high) / 2
        current_savings = 0
        monthly_salary = annual_salary / 12

    if guess/100 > 1:
        print("It is not possible to pay the down payment in three years.")
        return
    print(guess/100)
    print(step)
        
annual_salary = float(input("Enter your annual salary: "))

house_hunting(annual_salary)