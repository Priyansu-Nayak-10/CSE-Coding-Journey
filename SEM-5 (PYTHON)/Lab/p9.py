passes=0
failures=0
for x in range(10):
    r=int(input("Enter the label: "))
    while (r!=1 and r!=2):
        print("This is not a valid input.")
        r=int(input("Enter the label: "))

    if r==1:
        passes+=1
    elif r==2:
        failures+=1
if passes<=8:
    print(f"only {passes} students have passed the exam. ")
else:
    print("Bonus to the instructor")