import pandas as pd

grades = pd.Series([87,100,94]) #indexes numbers 0 based with type of information
#print(grades)

myarray = pd.Series(98.6, range(3))
#print(myarray)

#print(grades[0]) #specific access

#print(grades.describe()) #describe stats on array, from count to mean, std, min, etc

grades = pd.Series([87,100,94], index = ['Wally', 'Eva', 'Sam']) #pairs index with the number
#print(grades)

grades = pd.Series({'Wally':87, 'Eva': 100,'Sam':94}) #giving it a dictionary
#print(grades)

#print(grades['Eva'])
#print(grades.Wally)
#print(grades.dtype)
#print(grades.values)

hardware = pd.Series(['Hammer', 'Saw', 'Wrench']) #any string methods can be applied because they are string series

a = hardware.str.contains('a') #boolean to check if anything in series contains the letter a
#print(a)

b =  hardware.str.upper() #makes everything upper case 
#print(b)