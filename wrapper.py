import pandas
import os
result = pandas.read_csv('C:\\Users\\msand\\Desktop\\Contacts.csv')

df = pandas.DataFrame(result, columns = ['Number', 'Message'])
dfResult = []


for index, row in df.iterrows():
    print(
        row['Message'])
    os.system('python Message.py %s %s' %  
    (row['Number'], row['Message']))

""" print(df["Number"].size)

print(df["Number"][0])
print(df["Message"][0]) """
 

 
 
