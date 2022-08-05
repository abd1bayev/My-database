import pandas as pd

def table_1():
    table_1 = pd.read_csv("Data/only_wood_customer_us_1.csv")
    table_1 = table_1[["Gender","FirstName", "LastName", "Email", "Age", "City", "Country"]]
    gender = {'0':'Male', '1':'Female','M': 'Male','F': 'Female'}
    table_1['Gender'] = table_1['Gender'].replace(gender)
    table_1['Country'] = 'USA'
    table_1["Email"] = table_1["Email"].str.lower()
    table_1['FirstName'] = table_1['FirstName'].str.capitalize()
    table_1['LastName'] = table_1['LastName'].str.capitalize()
    table_1['City'] = table_1['City'].str.replace('_',' ')
    table_1['City'] = table_1['City'].str.replace('-',' ')
    table_1['FirstName'] = table_1['FirstName'].str.replace('\\','')
    table_1['LastName'] = table_1['LastName'].str.replace('\\','')
    table_1['FirstName'] = table_1['FirstName'].str.replace('"','')
    table_1['LastName'] = table_1['LastName'].str.replace('"','')
    table_1['City'] = table_1['City'].str.title()

    return table_1

table_1 = table_1()

def table_2():
    table_2 = pd.read_csv("Data/only_wood_customer_us_2.csv", sep =';', header = None, names = ['Age', 'City', 'Gender', 'Name', 'Email'])
    table_2[['FirstName','LastName']] = table_2.Name.str.split(expand=True)
    table_2.drop('Name', inplace=True, axis=1)
    table_2['City'] = table_2['City'].str.replace('_',' ').replace('-',' ')
    # table_2['City'] = table_2['City'].str.replace('-',' ')
    table_2['City'] = table_2['City'].str.title()
    gender = {'0':'Male', '1':'Female','M': 'Male','F': 'Female'}
    table_2['Gender'] = table_2['Gender'].replace(gender)
    table_2['Country'] = 'USA'
    table_2["Email"] = table_2["Email"].str.lower()
    table_2['FirstName'] = table_2['FirstName'].str.replace('\\','').str.replace('"','').str.capitalize()
    table_2['LastName'] = table_2['LastName'].str.replace('\\','').str.replace('"','').str.capitalize()
    table_2 = table_2[["Gender","FirstName", "LastName", "Email", "Age", "City", "Country"]]

    return table_2
    # print(table_2)

table_2 = table_2()

def table_3():
    table_3 = pd.read_csv("Data/only_wood_customer_us_3.csv", delimiter='\t',
                          names=['Gender', 'Name', 'Email', 'Age', 'City', 'Country'],
                          header=0, na_values=['N/A'])
    table_3[['FirstName', 'LastName']] = table_3.Name.str.split(expand=True)
    table_3.drop('Name', inplace=True, axis=1)
    table_3['City'] = table_3['City'].str.replace('_', ' ')
    table_3['City'] = table_3['City'].str.replace('-', ' ')
    table_3['City'] = table_3['City'].str.title()
    table_3 = table_3.replace(to_replace=r'string_|integer_|boolean_|character_|String', value='', regex=True)
    table_3['Age'] = table_3['Age'].replace(to_replace=r'[a-zA-Z]', value='', regex=True)
    gender = {'0': 'Male', '1': 'Female', 'M': 'Male', 'F': 'Female'}
    Gender = table_3['Gender'] = table_3['Gender'].replace(gender)
    table_3['Country'] = 'USA'
    table_3["Email"] = table_3["Email"].str.lower()
    table_3['FirstName'] = table_3['FirstName'].str.replace('\\', '')
    table_3['LastName'] = table_3['LastName'].str.replace('\\', '')
    table_3['FirstName'] = table_3['FirstName'].str.replace('"', '')
    table_3['LastName'] = table_3['LastName'].str.replace('"', '')
    table_3['FirstName'] = table_3['FirstName'].str.capitalize()
    table_3['LastName'] = table_3['LastName'].str.capitalize()
    table_3 = table_3[["Gender", "FirstName", "LastName", "Email", "Age", "City", "Country"]]
    # print(table_3)
    return table_3

table_3 = table_3()


