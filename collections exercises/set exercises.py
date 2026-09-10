#set un ordered , unchangeable, no duplication 

set1= {1,2,3,5,6,8,9,9,10}
print(type(set1))
print(len(set1))
print(set1)

set1.add(7)# add new item
print(set1)

fruit_set= {'banana','apple','orange','mango','kiwi'}#adding set to set
set1.update(fruit_set)
print(set1)


fruit_set.remove("kiwi") #remove item
print(fruit_set)

fruit_set.remove("grape")
print(f" remove result: {fruit_set}")

fruit_set.discard("grape")
print(f" discrad result {fruit_set}")# does not raise any error 

fruit_set.pop()
print(fruit_set)



