#if I input 1234 the output will be "One Two Three Four"
phone=input("Phone: ")
numbers_dict = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine"
}
output=""
for i in phone:
     output+=numbers_dict.get(i, "!")+" "
print(output)