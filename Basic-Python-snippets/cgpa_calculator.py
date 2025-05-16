print("****Welcome to the CGPA Calculator****\n")

name=input("Enter your name: ")
print(f"\nHello {name}\n")

n=int(input("Enter the number of subjects :\n"))
subs=[]
credits=[]
marks=[]
for i in range(n):
    sub=input(f"Enter the name of subject {i+1}:")
    subs.append(sub)
    credit=int(input(f"Enter the credit of subject {i+1}:"))
    credits.append(credit)
    mark=int(input(f"Enter the marks of subject {i+1}:"))
    marks.append(mark)
    print("\n")

print("**** Your subject marks along with credits are ****")
for i in range(n):
    print(f"Subject {i+1} : {subs[i]} \t Marks : {marks[i]} \t Credits : {credits[i]}")
  

print("****Your CGPA is calculating****\n")
total_credits=0
total_marks=0
for i in range(n):
    total_marks+=marks[i]*credits[i]
    total_credits+=credits[i]
cgpa=total_marks/total_credits
print(f"Your CGPA is : {cgpa:.2f}\n")
if cgpa>=9:
    print("Very Good!,Keep it up\n")
elif cgpa>=8:
    print("Good!,Keep it up\n")
elif cgpa>=7:
    print("Better luck next time ,prepare well\n")
