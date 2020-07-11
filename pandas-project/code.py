# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
bank = pd.read_csv(path)


#Code starts here
categorical_var=bank.select_dtypes(include='object')
numerical_var=bank.select_dtypes(include='number')
banks=bank.drop(['Loan_ID'],axis=1)
bank_mode=banks.mode()
ind=banks.columns
for i in ind:
    banks[i]=banks[i].fillna(bank_mode.loc[0,i])
print(banks.isnull().sum().values.sum())
#step3
avg_loan_amount=pd.pivot_table(banks,index=['Gender', 'Married', 'Self_Employed'],values='LoanAmount',aggfunc='mean')
loan_approved_se= banks[(banks['Self_Employed']=='Yes') & (banks['Loan_Status']=='Y')]
loan_approved_nse= banks[(banks['Self_Employed']=='No') & (banks['Loan_Status']=='Y')]
percentage_se=round((len(loan_approved_se)*100)/614,2)
percentage_nse=round((len(loan_approved_nse)*100)/614,2)
print(percentage_se,percentage_nse)
#step 5
loan_term=banks['Loan_Amount_Term'].apply(lambda x:x/12)
big_loan_term=banks[banks['Loan_Amount_Term']>=25*12]
print(len(big_loan_term))
loan_groupby=banks.groupby(['Loan_Status'])
loan_groupby=loan_groupby[['ApplicantIncome', 'Credit_History']]
mean_values=loan_groupby.mean()
print(mean_values)



