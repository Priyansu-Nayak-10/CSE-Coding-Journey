gallon=float(input("Enter the gallons used (-1 to end) : "))
total=0
m=0
while gallon!=-1:
    miles=float(input("Enter the miles driven : "))
    mg=miles/gallon
    print("the miles/gallon for this tank was : ",mg)
    total+=mg
    m+=miles
    gallon=float(input("Enter the gallons used (-1 to end) : "))    
print("The overall average miles/gallon was ",total/m)
