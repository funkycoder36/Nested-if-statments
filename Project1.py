medical_cause = input("do u have a medical cause Y or N: ")
atten = int(input("Enter the attendance of the student: "))

if medical_cause == 'Y': 
    print("You are allowed")
else:
    if atten>=75: 
      print("Allowed")
    else:
       print("Not allowed")
       