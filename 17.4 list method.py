number=[5,2,5,1,7,4]
number.append(20) #append add a number to a list at the end
print(number)
number.insert(0,10) #insert add a number somewhere in the list. here(0) is the position of the included numebr
print(number)
number.remove(20) #this method just remove the item in the list
print(number)
number.pop() #this method will remove the last item of the list
print(number)
print(number.index(5)) #it will print the indext of a item
print(40 in number) #it will give the answer if it is true or false
print(7 in number)
print(number.count(5)) #how many 5 are in the list
number.sort() #it will print the list in order small to big
print(number)
number.reverse() #reverse the list
print(number)
num=number.copy() #it is a copy. If we add or remove something from the list this copy will stay the same
number.append(100)
print(num)
number.clear() #it will empty the list.This method doesn't take any values
print(number)

