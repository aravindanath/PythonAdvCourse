list1 = ["Nagamani","Arvind","Rahul","Kumar"]
list2 = ["Java","Python","Selenium","Appium"]
list3 = []
for x in list1:
    for y in list2:
        list3.append(x)
        list3.append(y)

print(list3)
for x,y in zip(list3,list2):
    print(x,"----",y)
