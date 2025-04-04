pi=0
d=1
sign=1
c=1
ap_314 = None
print("Terms \t\t pi")
while c<=200:
    term=4*sign/d
    pi+=term
    print(F"{c} \t\t {pi}")
    if ap_314==None and f"{pi:.2f}"=='3.14':
        ap_314 = float(f"{pi:.2f}")
        print(F"we require {c} no of terms to get {'3.14'} for the first time.")
    sign*=-1
    d+=2
    c+=1
    
    
