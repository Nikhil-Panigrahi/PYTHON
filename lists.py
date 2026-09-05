items = ["Nikhil" , 12 , "Blue Haired Girl" , True]

print("TV Girl" in items)
print("True" in items)
print(True in items)

print(items[2])
items[3] = "Yena"
print(items)
print(len(items))
items.append("Mom")
items.extend(["fried rice" , "fun" , "catch"]) #can alos use items += [__]
print(len(items))
print(items)
items.remove("catch")
print(len(items))


#items.pop() ---> will remove the last one from the list

items.insert(2,"peter") #inserts an item at the said index without removing anything it just shifts elements after the said index by 1
print(items)


#items.(sort)--->sorts the list {p.s.}---->>> for a combination of integers and string error is shown
integers = [2,1,-2,55.5,123433,57]
print((integers.sort())) # now this shows None as output in the terminal as the function .sort() returns nothing
# to fix this do either of the below
integers.sort()
print(items)

#orr
print(sorted(integers))

names =["Nikhil" , "Amartya" , "alok" , "jhon" , "CAt"]
names.sort()
print(names) #now this is not the result we need as alok in first position
#to fix ts do 
names.sort(key=str.lower)
print(names)
# we can also use sorted(names , key=str.lower)