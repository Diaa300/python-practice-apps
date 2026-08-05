# ------------------------------
# --- My First Logic Project ---
# ------------------------------

import sys
import time

print('*' * 100)
print(" Hello Evrey Body Welcome To Smart Portal & Exam Grading System ".center(100, '*'))
print('*' * 100+ "\n")

# Data Sanitization

Your_Name = input("Write Your Full Name Name Please. ").strip().title()
Your_Email = input("Write Your Email Please. ").strip().lower()

print("\nVerifying Data...")
time.sleep(1.5)

if "@" in Your_Email and "." in Your_Email:
    print("Valid Email!")
    
    at_index = Your_Email.index("@")
    Username = Your_Email[:at_index]
    Domain = Your_Email[at_index + 1:]

else:
    print("Not Valid Email!") 
    sys.exit()

Student = input("Are You Student? (Yes, No) ")
Course_Name = input("Choose Your Course: HTML, JavaScript, Css, Python; Please. ").strip().title()
Course_Price = 100
Country = input("What's Your Country? ")

if  Student == "Yes" and Course_Name in ["Html", "Javascript", "Css", "Python"]:
    print(f"Hello {Your_Name} Because You From {Country} And Student")
    print(f"\"{Course_Name}-Course\" Price Is: ${Course_Price - 90}")

else :
    print("Sorry This is For Students")
    sys.exit()

Age = int (input ('What\'s Your Age? ').strip())
Score = float (input('Please Inter Your Score. ').strip())

if Score >= 90:
    Grade = "Excellent (A+)"
elif Score >= 80:
    Grade = "Very Good (B)"
elif Score >= 70:
    Grade = "Good (C)"
elif Score >= 50:
    Grade = "Pass (D)"        
else:
    Grade = "Failed (F)"    


if Score >= 50  and  Age >= 15 :
    Status = "Accepted"

else:
    Score < 50 
    Status = "Rejected"


if Grade == "Excellent (A+)" :
    Scholarship = "Discount 100%"

else :
    Scholarship = "No Discount"



print("\nAnlayzing Data...")
Student_ID = f'{Your_Name[0:2].upper()}-{Country[-2:].upper()}-{len(Your_Name)}'  
time.sleep(2.5)


print("=" * 50)
print("STUDENT FINAL PROFILE & REPORT".center(50))
print("=" * 50)
print(f"Student ID : {Student_ID}")
print(f"Name       : {Your_Name}")
print(f"Email      : {Your_Email}")
print(f"Username   : {Username}")
print(f"Domain     : {Domain}")
print(f"Country    : {Country}")
print(f"Age        : {Age}")
print("-" * 50)
print(f"Score      : {Score}%")
print(f"Grade      : {Grade}")
print(f"Status     : {Status}")
print(f"Scholarship: {Scholarship}")
print("=" * 50)