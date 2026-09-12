my_list=[1,2,3,4,4,5]
print(type(my_list))
print(my_list[0])#access the first element 
print(len(my_list))

#add item to the list 
my_list.append(10)
print(my_list)

fruit_list= ['banana','apple','orange','mango','kiwi']
fruit_list.append("strawbarry")
print(fruit_list)


#remove item to the list 
my_list.remove(4) #remove based on value
print(my_list)

fruit_list.remove("apple") #remove based on value
print(fruit_list)

fruit_list.pop(1) #delete last if empty and delete based on the index 
print(fruit_list)

del my_list[0]
print(my_list) #delete based on the index 

##my_list.clear() # clear the list
##print(my_list)


my_list.extend(fruit_list)#add the two list together staring from the first list 
print(my_list)

# lsit comprehesion
new_list= []

for x in fruit_list:
    if 'a' in x:
        new_list.append(x)
print(new_list)


new_list =[x.capitalize() for x in fruit_list if 'a' in x]
print(new_list)


for x in range(10):
 print(x)

ranging_list=[x for x in range(10)]
print(ranging_list)

print(ranging_list[1:5]) #list slicing
print(ranging_list[6:])
print(ranging_list[:])
print(ranging_list[-10:-1])

