n=[2,5,3,6,7]
print('Creating  a bar chart ')
print(f"{'index':<5} {'value':<5} {'bar':<10}")
for index, value in enumerate(n):
    print(f"{ index:<5} {value:<5} {'*'*value:<10}")
