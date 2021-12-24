print("Hi I'm here to help plan when you can fire!")
print("sheeeeeesh")
retirement_ex = float(input("How much money do you wanna spend during your retirement per year?\n>"))
current_income = float(input("How much do you earn per year?\n>"))
income_increment = float(input("Expected % increase in income per annually.\n>").strip("%")) / 100
stock_growth = float(input("Per year growth of assets.\n>").strip("%")) / 100
savings_rate = float(input("how much percent of ur income u save per year.\n>").strip("%")) / 100
inflation_rate = float(input("% inflation rate?\n>").strip("%")) / 100
withdrawal_rate = float(input("Withdrawal rate.\n>").strip('%')) / 100
age = int(input("Age?\n>"))
while True:
    print("DCA? Monthly? Yes/No only")
    DCAM = input('> ')

    if DCAM == 'yes':
        break
    elif DCAM == 'no':
        print("Yearly?")
        DCAY = input('> ')
        if DCAY == "yes":
            break
        else:
            continue
    else:
        print("CB can read or not hongkan")
        continue

retirement_sum = retirement_ex / withdrawal_rate
savings_peryear = current_income * savings_rate
i=0
savings = float(input("Current savings?\n"))
real_growth = 1 + stock_growth - inflation_rate

while  True:
    savings = savings * real_growth
    if savings < retirement_sum:
        savings += savings_peryear
        savings_peryear = current_income * savings_rate + current_income * income_increment *savings_rate
        i += 1
        continue
    else:
        break



print("Real growth= " + str(real_growth))
print("Years left =" + str(i) + " years")
print("Retirement age = " + str(age + i))
print("Your retirement sum = " +str(round(retirement_sum, 2)))
