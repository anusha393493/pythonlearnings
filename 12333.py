import pandas as pd

df=pd.read_excel(r"C:\Users\anusha.raparthi\Desktop\wordtoexcel2.xlsx")

pd.set_option('display.max_columns',None)

pd.set_option('display.max_rows',None)

pd.set_option('display.width',None)

#print(df.columns)

#(Site_NAME,Change_Type,Recommended_Action,Total_No_of_days_CT,IS_ACTIVE,LAST_MODIFIED_DATE,CREATED_DATE,LAST_MODIFIED_BY,CREATED_BY)

#1,CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,'SYSTEM','SYSTEM'

df['Total_No_of_days_CT']=df['Target Completion Days']

Site_NAME='Type of Change_Plant III'

df1=df.drop(['Target Completion Days'], axis=1)

df1.insert(0,'Site_Name',Site_NAME)

df1['IS_ACTIVE']='1'

df1['LAST_MODIFIED_DATE']='CURRENT_TIMESTAMP'

df1['CREATED_DATE']='CURRENT_TIMESTAMP'

df1['LAST_MODIFIED_BY']='SYSTEM'

df1['CREATED_BY']='SYSTEM'

df1.head()

insert_script = ""

for row in df1.values:

        values = ", ".join([f"'{str(value)}'" for value in row.tolist()])

        insert_script += f"\n({values}),"

print(insert_script)
