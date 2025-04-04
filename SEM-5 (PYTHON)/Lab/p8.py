total=0
grade_counter = 0
grade=int(input("Enter a grade ,-1 to end "))
while grade!=-1:
    total=total+grade
    grade_counter+=1
    grade=int(input("Enter a grade ,-1 to end "))

if grade_counter == 0:
   print("no grade were entered")
else:
   print(f"average = {total/grade_counter}")