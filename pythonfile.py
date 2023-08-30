import os
import tabula
import fitz
import psycopg2
import pandas as pd
import PyPDF2

#pdf_file = r"C:\Users\anusha.raparthi\Desktop\sampledata\pdfdata2.pdf"
#pdf_file = r"C:\Users\anusha.raparthi\Desktop\sampledata\pdfdata.pdf"

def Start_text(pdf_path, t_text):
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader1 = PyPDF2.PdfReader(pdf_file)

        for page_number1, page1 in enumerate(pdf_reader1.pages, start=1):
            if t_text in page1.extract_text():
                return page_number1

        return None


def End_text(pdf_path, target_text):
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        for page_number, page in enumerate(pdf_reader.pages, start=1):

            if target_text in page.extract_text():
                return page_number

        return None
def extract_sites_study(text,pdf_file):
    #pdf_file=r"C:\Users\anusha.raparthi\Desktop\sampledata\CTRI-2022-08-044806.pdf"
    page_number2 = End_text(pdf_file, "List of Countries")
    page_number3 = End_text(pdf_file, "Name of Committee")
    print(page_number2, page_number3)
    if page_number2 == page_number3:
        area_coordinates = (200, 140, 1000, 5000)
        df_list = tabula.read_pdf(pdf_file, pages='2', area=area_coordinates, multiple_tables=True)
        for i in df_list:
            #print(type(i))
            New_Column_Names = ['Name', 'Site', 'Address', 'Phone']
            i.columns = New_Column_Names
            start_name = 'Name of Principal\rInvestigator'
            start_row = i[i['Name'] == start_name]
            start_row_number = start_row.index[0]
            end_name = 'Name of Committee'
            end_rows = i[i['Name'] == end_name]
            last_row_number = end_rows.index[0]
            Name = i.iloc[start_row_number + 1:last_row_number]['Name']
            Site = i.iloc[start_row_number + 1:last_row_number]['Site']
            Address = i.iloc[start_row_number + 1:last_row_number]['Address']
            Phone = i.iloc[start_row_number + 1:last_row_number]['Phone']
        return Name,Site,Address,Phone

        #print(i.iloc[start_row_number + 1:last_row_number]['Name'])
        #print(i.iloc[start_row_number + 1:last_row_number]['Site'])
        #print(i.iloc[start_row_number + 1:last_row_number]['Address'])
        #print(i.iloc[start_row_number + 1:last_row_number]['Phone'])

if __name__ == "__main__":
    host = "10.140.189.165"
    database = "Internal"
    username = "postgres"
    password = "techsol"
    folder_path = r"F:\clinicaldata2"
    pdf_files = [file for file in os.listdir(folder_path) if file.endswith(".pdf")]
    if len(pdf_files) == 0:
        print("no files")
    else:
        try:
            connection = psycopg2.connect(
                host=host,
                database=database,
                user=username,
                password=password
            )
            cursor = connection.cursor()
            sql_query1 = """
            create table if not exists sites_studydata_single(
            Name varchar,
            Site varchar,
            Address varchar,
            Phone varchar,
            pdf_filename varchar
            );
            """
            sql_query2 = """
            create table if not exists sites_studydata_multiple(
            pdf_filename varchar
            );
            """
            cursor.execute(sql_query1)
            cursor.execute(sql_query2)
            connection.commit()
            for pdf_file in pdf_files:
                pdf_path = os.path.join(folder_path, pdf_file)
                pdf_filename = os.path.basename(pdf_path)
                with fitz.open(pdf_path) as pdf:
                    for page_number in range(pdf.page_count):
                        page = pdf.load_page(page_number)
                        page_text = page.get_text()
                        #Name,Site,Address,Phone= extract_sites_study(page_text,pdf_path)
                        #print(Name, Site, Address, Phone)
                        page_number2 = End_text(pdf_path, "List of Countries")
                        page_number3 = End_text(pdf_path, "Name of Committee")
                        #print(Name,Site,Address,Phone)


                        if page_number2 == page_number3:
                            Name, Site, Address, Phone = extract_sites_study(page_text, pdf_path)
                            sep=''
                            a=sep.join(Name)
                            b= sep.join(Site)
                            c= sep.join(Address)
                            d=sep.join(Phone)
                            d1=(a,b,c,d,pdf_filename)
                            sql_insert_query1 = "INSERT INTO sites_studydata_single(Name,Site,Address,Phone,pdf_filename) VALUES (%s,%s,%s,%s,%s);"
                            cursor.execute(sql_insert_query1,(d1,))
                            connection.commit()
                            break
                        else:
                            print(page_number2,page_number3)
                            sql_insert_query2 = "INSERT INTO sites_studydata_multiple(pdf_filename) VALUES (%s);"
                            cursor.execute(sql_insert_query2,(pdf_filename,))
                            connection.commit()
                            break

            cursor.close()
            connection.close()
            print("Data inserted successfully into PostgreSQL!")
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL or inserting data:", error)
#page_number2 = End_text(pdf_file, "List of Countries")
#page_number3 = End_text(pdf_file, "Name of Committee")


