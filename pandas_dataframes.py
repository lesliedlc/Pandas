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

print(grades.loc[['Test1','Test2'],['Eva','Katie']]) #rows then columns
print(grades.iloc[[0,1],[1,3]])