weight= input("Weight:")
typ=input('(L)bs or (k)g:')
if typ.upper()=="L":
    weight_kg=float(weight)*0.45
    m=f'You are {weight} kg'
    print(m)
elif typ.upper()=="K":
    weight_lb=float(weight)/0.45
    m=f'You are {weight_lb} lbs'
    print(m)