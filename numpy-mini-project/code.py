# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]
new_record=np.asarray(new_record)
#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)
#Code starts here
census=np.concatenate((data,new_record))
age=census[:,0]
max_age=age.max()
min_age=age.min()
age_mean=age.mean()
age_std=age.std()
race=census[:,2]
race_0=race[race==0]
race_1=race[race==1]
race_2=race[race==2]
race_3=race[race==3]
race_4=race[race==4]
len_0=race_0.size
len_1=race_1.size
len_2=race_2.size
len_3=race_3.size
len_4=race_4.size
a=[len_0,len_1,len_2,len_3,len_4]
minority_race=a.index(min(a))
senior_citizens=age[age>60]
work=census[:,6]
working_hours_sum=work[age>60]
avg_working_hours=working_hours_sum.mean()
working_hours_sum=work[age>60].sum()
edu=census[:,1]
high=edu[edu>10]
low=edu[edu<=10]
salary=census[:,7]
avg_pay_high=salary[edu>10].mean()
avg_pay_low=salary[edu<=10].mean()
print("%0.2f\n%0.2f"%(avg_pay_high,avg_pay_low))





