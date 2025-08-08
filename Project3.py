print("Select you ride")
print("1. Bike")
print("2. Car")

choice = int(input("Enter your choice "))

if(choice == 1): 
    print("What type of bike")
    print("1. scooty\n")
    print("2. scooter\n")

    choice2 = int(input("Enter your choice"))
    if choice2==1:
     print("you have selected scooty")
    else:
       print("you hav selected scooter")

elif(choice == 2):
   print ("What type of car")
   print("1. Sudan")
   print("2. XUV")
   choice3 = int(input("Enter your choice "))
   
   if choice3==1:
     print("you have selected sudan")
   else:
       print("you hav selected XUV")

