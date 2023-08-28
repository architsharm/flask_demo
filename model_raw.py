import pickle 
model_pickle = open("./classifier.pkl", 'rb')
clf = pickle.load(model_pickle)

def prediction(loan_req):
    if loan_req['Gender'] == "Male":
        Gender = 0
    else:
        Gender = 1
 
    if loan_req['Married'] == "Unmarried":
        Married = 0
    else:
        Married = 1
 
    if loan_req['Credit_History'] == "Unclear Debts":
        Credit_History = 0
    else:
        Credit_History = 1  
 
    ApplicantIncome = loan_req['ApplicantIncome']
    LoanAmount = loan_req['LoanAmount'] / 1000
    
    # Making predictions 


    prediction = clf.predict( 
        [[Gender, Married, ApplicantIncome, LoanAmount, Credit_History]])
     
    if prediction == 0:
        pred = 'Rejected'
    else:
        pred = 'Approved'
    return pred

loan_application = {
    'Gender': "Male",
    'Married': "Unmarried",
    'ApplicantIncome': 50000,
    'Credit_History': "Cleared Debts",
    'LoanAmount': 500000
}

print(prediction(loan_application))
