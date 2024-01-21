""" Price of a house is $1M. If buyer has good credit,
they need to put down 10%
otherwise they need to put down 20%
print the down payment"""
gd_crd= True
if gd_crd:
    print(f"Down Payment: ${float(1000000*0.1)}")
else:
    print(f"Down Payment: ${float(1000000*0.2)}")
