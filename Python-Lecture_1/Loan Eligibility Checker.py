# Loan Eligibility Checker
# Given monthly_income = 45000, credit_score = 720, existing_emi = 8000, loan_amount = 300000. 
# The person is eligible only if credit score is at least 700 and existing EMI is less than 40% of income 
# and loan amount is not more than 10 times monthly income. Print each condition as True/False, then the final eligibility.

monthly_income = 45000
credit_score = 720
existing_emi = 8000
loan_amt = 300000


print("eligibility_on_credit_score : ", credit_score >= 700)
print("eligibility_on_EMI : ", existing_emi < 40/100 * monthly_income )
print("eligibility_on_income : ", loan_amt <= 10 * monthly_income)
print("Final_eligibility : ", credit_score >= 700 and existing_emi < 40/100 * monthly_income and loan_amt <= 10 * monthly_income)


