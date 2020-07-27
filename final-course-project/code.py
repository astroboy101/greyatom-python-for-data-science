# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading the file
data=pd.read_csv(path)

#Code starts here
# Step 1 
#Reading the file

loan_status=data["Loan_Status"].value_counts()
print(loan_status)
loan_status.plot(kind='bar')
#Creating a new variable to store the value counts


#Plotting bar plot



# Step 2
#Plotting an unstacked bar plot
property_and_loan=data.groupby(['Property_Area','Loan_Status']).size().unstack()
property_and_loan.plot(kind='bar',stacked=True)
plt.xlabel('Property Area')
plt.xticks(rotation=45)
plt.ylabel('Loan Status')
print(property_and_loan['N'][1])


#Changing the x-axis label


#Changing the y-axis label


#Rotating the ticks of X-axis


# Step 3
#Plotting a stacked bar plot
education_and_loan=data.groupby(['Education','Loan_Status']).size().unstack()
education_and_loan.plot(kind='bar',stacked=True)
plt.xlabel('Education Status')
plt.ylabel('Loan Status')
plt.yticks(rotation=45)
#Changing the x-axis label


#Changing the y-axis label


#Rotating the ticks of X-axis


# Step 4 
#Subsetting the dataframe based on 'Education' column
graduate=data[data['Education']=='Graduate']
not_graduate=data[data['Education']=='Not Graduate']
graduate['LoanAmount'].plot(kind='density',label="have fuck")
not_graduate['LoanAmount'].plot(kind='density',label="have fun")

#Subsetting the dataframe based on 'Education' column


#Plotting density plot for 'Graduate'


#Plotting density plot for 'Graduate'


#For automatic legend display


# Step 5
#Setting up the subplots
fig,(ax_1,ax_2,ax_3)=plt.subplots(3,1)

#Plotting scatter plot
ax_1.scatter(data['ApplicantIncome'],data['LoanAmount'])
ax_1.set_title('ApplicantIncome')
ax_2.scatter(data['CoapplicantIncome'],data['LoanAmount'])
ax_2.set_title('Coapplicant Income')
#Setting the subplot axis title
data['TotalIncome']=data['ApplicantIncome']+data['CoapplicantIncome']
ax_3.scatter(data['TotalIncome'],data['LoanAmount'])
ax_3.set_title('Total Income')
print(data['TotalIncome'])

#Plotting scatter plot


#Setting the subplot axis title


#Creating a new column 'TotalIncome'


#Plotting scatter plot



#Setting the subplot axis title



