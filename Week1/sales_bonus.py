def main():
    sales = float(input("Enter sales: $"))
    if sales < 0:
        print("Invalid")
        main()
    elif sales < 999:
        bonus = sales*0.1
        print("Bonus: $" + str(bonus))
        main()
    elif sales >= 1000:
        bonus = sales*0.15
        print("Bonus: $" + str(bonus))
        main()

main()
