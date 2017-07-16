'import time'
print ("Hello! I need some information")
'import time'
print ("This is a test that will let you know whether you are diabetic or not")
'import time'
Name = input ("Name: ")
Age = input ("Age: ")
Sex = input ("Sex: ")
CivilStatus = input ("Civil Status: ")
Address = input ("Address: ")                 
Height = input ("Height: ")
Weight = input ("Weight: ")
print ("Is your Fasting Blood Sugar result greater than 126 mg/dl?")
ans = input ("Type yes or no: ")
if ans == "yes":
    print("You have diabetes. You should consult your doctor for proper diagnosis and treatment")
    print ("END OF QUIZ")
else:
    print ("You do not have diabetes, but you should have yourself checked by a doctor every year starting age 50 years old")
    print ("END OF QUIZ")



    
