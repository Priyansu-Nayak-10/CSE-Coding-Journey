students={'X':[10,20,30,40],
          'Y':[50,60,70,80],
          'Z':[90,100,80,70]
}
tg,gc=0,0
for k, v in students.items():
    print(f"student {k} has received avg: {sum(v)/len(v):.2f}")
    tg+=sum(v)
    gc+=len(v)
print(f"class avg is : {tg/gc:.2f}")

         
