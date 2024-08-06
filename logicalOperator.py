# if applicant has high income AND good credit , eligible for loan

has_good_income = True
has_good_creditScore = True

if has_good_income and has_good_creditScore:
    print("Eligible for loan")
else:
    print("Not Eligible for loan")

# if applicant has high income AND good credit , eligible for loan

has_good_income = False
has_good_creditScore = False

if has_good_income or has_good_creditScore:
    print("Eligible for loan")
else:
    print("Not Eligible for loan")

# if applicant has good credit score AND  Not Criminal record , eligible for loan

has_criminal_record = True
has_good_creditScore = True

if has_good_creditScore and not has_criminal_record:
    print("Eligible for loan")
else:
    print("Not Eligible for loan")