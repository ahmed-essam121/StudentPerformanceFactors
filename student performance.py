import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


stud_performance=pd.read_csv(r"C:\Users\EL-BOSTAN\OneDrive\Desktop\archive_5\StudentPerformanceFactors.csv")
stud_performance.head()
stud_performance.dropna()
stud_performance.isnull().sum()


for col in stud_performance:
    print(stud_performance[col].value_counts())
    print('-----------')
    
#visulization

#Countplot for categorical data
for col in stud_performance:
    if stud_performance[col].dtype == 'O':
        sns.countplot(x=col,data=stud_performance)
        plt.show()
        
#Distribution of numerical columns
for col in stud_performance:
    if stud_performance[col].dtype != 'O':
        sns.histplot(stud_performance[col],kde=True)
        plt.show()
        
        
#Attendance of student based on distance from home
sns.boxplot(x='Distance_from_Home',y='Attendance',data=stud_performance)

#ours Studied vs Exam Score
plt.figure(figsize=(8,8))
sns.lmplot(x='Hours_Studied', y='Exam_Score', data=df)
plt.show()