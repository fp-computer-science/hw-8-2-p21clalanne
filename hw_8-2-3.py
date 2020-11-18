# Author CL 11/17/2020

userlist = list(input("Input a list of 6 numbers or words, separated by spaces: "))

userchoice = input("Do you want the middle or the end of the list? ")

if userchoice == "ends":
    print(userlist[0])
    print(userlist[10])
elif userchoice == "middle":
    print(userlist[1:10])
