import pandas as pd
df=pd.read_csv('eg.csv')
print(df)
new_col = [1,2]
df.insert(0,'Average',new_col,True)
print(df)
print(df[df['name']=='b'].iloc[:,[1,3]])
df1= df.rename(columns = {"name":"Mod_col"})
print(df1)
# # #Rename multiple columns
df1 = df.rename(columns={"name":"Mod_col1","date":"dob"}) # or , df1 = df.rename({"name":"Mod_col1","date":"dob"},axis='columns')
print(df1)
print(df1.sample()) #print random row