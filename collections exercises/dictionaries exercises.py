#dictionariy order , changable, do not allow duplication

my_dic = {
    "name": "khalid",
    "age" : 31,
    "hope" : ["football","swimmmig","poemer","reader"],   
}

print(my_dic)
print(len(my_dic))
print(type(my_dic))

#accessing item
print(my_dic["name"])
print(my_dic["age"])
print(my_dic["hope"])


my_dic = {
    "name": "khalid",
    "age" : 30,
    "hope" : ["football","swimmmig","poemer","reader"], 
}
print(my_dic)

my_dic["name"]= "waleed"
print(my_dic)

my_dic.update({ "name": "ali","age" : 30,"hope" : ["football","swimmmig","poemer","reader"],})
print(my_dic)

my_dic.update({"hope": ["football","swimmmig","poemer","writer"]})
print(my_dic)

my_dic.update({"city": "abudhabi"})
print(my_dic)

my_dic.pop("age")
print(my_dic)

del my_dic["name"]
print(my_dic)

my_dic.clear()
print(my_dic)