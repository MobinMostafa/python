
day = input("Enter a number for day : ");

match int(day):
    case 1:
        print("Today is Saturday")
    case 2:
        print("Today is Sunday")
    case 3:
        print("Today is Monday")
    case 4: 
        print("Today is Tuesday")
    case 5:
        print("Today is Wednesday")
    case 6:
        print("Today is Thursday")
    case 7:
        print("Today is Friday")
    case _:
        print("You typed invalid number")