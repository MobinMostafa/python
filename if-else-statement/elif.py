mark = input("Enter your number : ")

if(int(mark) >= 80 and int(mark) <=100):
    print("You got A+")
elif (int(mark) >= 70 and int(mark) < 80):
    print("You got A")
elif (int(mark) >= 60 and int(mark) < 70):
    print("you got A-")
elif (int(mark) >= 0 and int(mark) <60 ) :
    print("You are failed")
else :
    print("You typed invalid number")