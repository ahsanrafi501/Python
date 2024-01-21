#{} this brackets must be used in dictionary
customer={
    "name":"Jannatul Nihal",
    "age": 21,
   #"age": 40 each key should be unique. So one age key can be there and the other one I've comment it out
    "Is_verified": True
}
print(customer["name"])
print(customer["age"])
print(customer["Is_verified"])
#if you miss the actual key name then the output will be error. To avoid error and get "none we have to use a .get function"
print(customer.get("beautiful","she is the most beautiful")) #in .get we have to use () this bracket
#here if the key is empty then "she is most beautiful" will be printed
customer["birthdate"]="Jan 1,2002" #here I updated the customer information
print(customer["birthdate"])