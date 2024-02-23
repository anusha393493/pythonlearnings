import pandas as pd
df=pd.read_excel(r"C:\Users\anusha.raparthi\Desktop\DIvisionsNm.xlsx",sheet_name='Type of Change_Plant III')
pd.set_option('display.max_columns',40000)
pd.set_option('display.max_rows',40000)
pd.set_option('display.width',100000)
#print(df.columns)
#(Site_NAME,Change_Type,Recommended_Action,Total_No_of_days_CT,IS_ACTIVE,LAST_MODIFIED_DATE,CREATED_DATE,LAST_MODIFIED_BY,CREATED_BY)
#1,CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,'SYSTEM','SYSTEM'
Site_NAME='Type of Change_Plant III'
Change_Type=df['Type of Change']
Recommended_Action=df['Recommended Action / Impact Assessment']
Total_No_of_days_CT=str(df['Target Completion '])
IS_ACTIVE='1'
LAST_MODIFIED_DATE='CURRENT_TIMESTAMP'
CREATED_DATE='CURRENT_TIMESTAMP'
LAST_MODIFIED_BY='SYSTEM'
CREATED_BY='SYSTEM'

#print(Site_NAME)
rows=len(df)
for row in df.values:
    print("("+"'"+Site_NAME+"'"+","+"'"+Change_Type+"'"+","+"'"+Recommended_Action+"'"+","+"'"+Total_No_of_days_CT+"'"+","+"'"+IS_ACTIVE+"'"+","+"'"+LAST_MODIFIED_DATE+"'"+","+"'"+CREATED_DATE+"'"+","+"'"+LAST_MODIFIED_BY+"'"+","+"'"+Site_NAME+"'"+")")
