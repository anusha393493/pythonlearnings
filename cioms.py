import fitz
import psycopg2

def extract_data(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    drug=""
    found = False
    for page in doc:
        text+=page.get_text()
        #print(text)
        lines=text.split("\n")

    for line in lines:
        if "PARACETAMOL" in line:
            found=True
            drug="PARACETAMOL"
    return found,drug

def comparision(found,drug,host,database,username,password):
    #print(drug)
    if found==True:
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
            #print(result)

            for i in result:

                if i==drug:
                    print("found")
                    break
                else:
                    print("not found")

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
    found,drug=extract_data(pdf_path)
    comparision(found,drug,host,database,username,password)
