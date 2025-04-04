from string import punctuation
text="""Bhubaneswar is an ancient city in India’s eastern state
 of Odisha, formerly Orissa. Many temples built from
 sandstone are dotted around Bindu Sagar Lake in the old city,
including the 11th-century Hindu Lingaraja Temple."""
f_t=''.join(filter(lambda ch: ch.isalnum() or ch.isspace(),text))
print(f_t)

lw=f_t.lower().split()
print(lw)
n=[]
for i in lw:
    if(i not in n):
        n.append(i)
print(n)

