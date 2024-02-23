import fitz
import psycopg2
import pandas as pd
def comparision(host,database,username,password):
    try:
        connection=psycopg2.connect(
            host=host,
            database=database,
            user=username,
            password=password
        )
        cursor=connection.cursor()
        sql_query=""" 
             select product from cioms;
            """
        #print(sql_query)

        cursor.execute(sql_query)
        result = cursor.fetchall()
        #results=list(result)
        for i in result:
            result1=str(result)
            result1=result1.replace("('","")
            result1=result1.replace("',)","")
            result1=result1.replace("[","")
            result1=result1.replace("]","")


        #print(result1[0])
        #result1list(result1)
        result2=result1.split(",")


        connection.commit()
        connection.close()
    except:
        print("error!")






if __name__=="__main__":
    host = "10.140.189.165"
    database = "Internal"
    username = "postgres"
    password = "techsol"
    pdf_path=r"C:\Users\anusha.raparthi\Desktop\CIOMS 11Jan 1.pdf"

    comparision(host,database,username,password)


