## This code is to write a program to convert the data type of a variable in Python. basically a code to convert a string to an integer by input since we take input in string always
## inspired to write this to test the conversion of data types
inp = input("Enter a  age number: ")
inp=int(inp)
if type(inp)==float:
    print("please type a complete number")
    inp = input("Enter a  age number: ")
    inp=int(inp)
elif type(inp)==str:
    print("please type a number not a string")
    inp = input("Enter a  age number: ")
    inp=int(inp)
else:    print("the number you entered is ",inp)

if inp in range(105):
    print("you are still human stay in your limits")

if inp>=106:
    print("are you sure you want to be in this world?")
    choice = input("Enter your choice (yes/no): ")
    if choice == "yes" or choice == "yeah" or choice == "ok" or choice == "sure" or choice == "thankyou":
        print("your wish human you have still not advanced your monkey brain stay here this is what you deserve")
    elif choice == "no":
        print("wow you are a human with a brain you have made the right choice congrats on actually trancending after a somewhat small life of yours")
    else:    print("yWTF are you playing with me you dumb human just type yes or no and stop wasting my time you are punished to suffer for the next generations unable to achive nirvana until you repent and earn the meaning of time and learn to never\
    disrespect me. learn to respect gods and others time you dumbass")     