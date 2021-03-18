import try_module
import importlib

a=int(input("give a number"))
b=int(input("give a number"))

print("addition = ",try_module.praxi(a,b))
#change try_module.py before this call
importlib.reload(try_module)

a=int(input("give a number"))
b=int(input("give a number"))

print("division = ",try_module.praxi(a,b))

print(importlib.find_loader("try_module"    ))