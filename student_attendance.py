classesheld=int(input("Enter the total classes held: "))
classattended=int(input("Enter the total classes attended: "))
attendance=(classattended/classesheld)*100
medical_cause=input("Do you have a medical cause: ")
if attendance>=75 and medical_cause=="no":
    print("Allowed to appear")
else:
    print("not allowed")
