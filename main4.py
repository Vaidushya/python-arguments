def emply_nm(name):
    print(name)

def salery(exp):
 if exp>=5:
    return 3000000
 elif exp>=3:
    return 1000000
 else:
    return 500000
 
emply_nm("Ram")

a = salery(15)
print("The salary of the employee is ",a)
