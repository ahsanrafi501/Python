"""If a applicant has good credit and doesn't have criminal record the he
is eligible for loan"""
has_good_credit=input("Input:")
has_criminal_record= input("Input:")
if has_good_credit and not has_criminal_record:
    print("Eligible for loan")
else:
    print("You are poor get lost")