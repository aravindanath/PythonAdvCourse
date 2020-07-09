def student():
    print("Students")

def studentDetails(name,roll):
    print(name)
    print(roll)

def students(*args,**kwargs):
    print(type(args),args)
    print(type(kwargs),kwargs)

s = students("arvind","Ravi","Nagamani","Mani",Name="Arvind",City="Bangalore",Subject="Python")
