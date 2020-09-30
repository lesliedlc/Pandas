import pandas as pd

grades_dict = {'Wally':[87,96,70], 'Eva':[100,87,90], 'Sam':[94,77,90],'Katie':[100,81,82], 'Bob':[83,65,85]}

grades = pd.DataFrame(grades_dict)

grades.index = ['Test1','Test2','Test3']

#print(grades)
#print(grades.Sam)

#print(grades.loc['Test1']) #what you want to grab based on name
#print(grades.iloc[1]) #returns test2 scores

#print(grades.loc[['Test1','Test3']]) #location method, gets lower and upper limit
#print(grades.iloc[0:2]) #0 based indexing only going up to 2, -1
#print(grades.iloc[0,2]) #will give specifics not a range

#print(grades.loc[['Test1','Test2'],['Eva','Katie']]) #rows then columns
#print(grades.iloc[[0,1],[1,3]])

#print(grades)
#print(grades[grades>90]) #NaN means not a number, so it did not pass this boolean test
#print(grades[(grades>=80) & (grades<90)])

#print(grades.at['Test2','Eva']) #at method can be used to get a specific values
#grades.at['Test2','Eva'] = 100 #makes a permanent change to the original dataframe

#print(grades.iat[1,2]) 

#grades.iat[1,2] = 87 #updates the exact row/column

#print(grades.desribe()) #gives stats by student

pd.set_option('precision', 2) #gives 2 decimal places
#print(grades.describe())
#print(grades.mean()) #gives avg per student, per column
#to get mean by grades, need to transpose
#print(grades.T.mean()) #does not affect the original dataframe

#print(grades.sort_index(ascending = False))
#print(grades.sort_index(axis=1)) #wil do columns, in ascending because did not signify otherwise
#axis 1 columns
#axis 0 row

#print(grades.sort_values(by='Test1',axis=1,ascending = False)) #what students scored the highest only on test1

#print(grades.T.sort_values(by='Test1',ascending = False))
print(grades.loc['Test1'].sort_values(ascending = False)) #gives only the results for test 1, in a series, in descending order
#inplace=true sort dataframe and make it permanant