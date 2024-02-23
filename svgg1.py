import xml.etree.ElementTree as ET
import psycopg2
import os

def read_svg_file(file_path):
    svg_data={}
    for filename in os.listdir(folder_path):
        if filename.endswith(".svg"):
            file_path=os.path.join(folder_path,filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                svg_data[filename] = file.read()
                #print(svg_data)

    return svg_data

def find_desc_elements(root):
    desc_elements = []
    for element in root.iter():
        if 'desc' in element.tag:
            desc_elements.append(element)
    return desc_elements

def find_title_elements(root):
    title_elements = []
    for element in root.iter():
        if 'title' in element.tag:
            title_elements.append(element)
    return title_elements

def extracting_data(root):
    rectangle = []
    rounded_rectangle=[]
    curved_rectangle=[]
    Pentagon=[]
    found = 0
    for element in root.iter():
        if 'title' in element.tag:
            if "Process" in element.text or "Closed State" in element.text or "Opened State" in element.text:
                found = 1
            if "Terminator" in element.text:
                found = 2
            if "Document" in element.text:
                found=3
            if "Off-page reference" in element.text:
                found=4
        elif found==1 and 'desc' in element.tag:
            rectangle.append(element.text)
            found=0
        elif found==2 and 'desc' in element.tag:
            rounded_rectangle.append(element.text)
            found=0
        elif found==3 and 'desc' in element.tag:
            curved_rectangle.append(element.text)
            found=0
        elif found==4 and 'desc' in element.tag:
            Pentagon.append(element.text)
            found=0
        else:
            found=0
    return rectangle,rounded_rectangle,curved_rectangle,Pentagon

def creating(host,database,username,password):
    try:
        connection = psycopg2.connect(
            host=host,
            database=database,
            user=username,
            password=password
        )
        cursor=connection.cursor()
        sql_query="""
             CREATE TABLE IF NOT EXISTS SVG(
                 Rectangle TEXT,
                 Rounded_Rectangle Text,
                 Curved_Rectangle Text,
                 Pentagon Text
                 );
             """
        cursor.execute(sql_query)
        connection.commit()
        cursor.close()
        connection.close()
        print("Table created successfully in PostgreSQL!")

    except psycopg2.Error as error:
        print("Error while connecting to PostgreSQL or creating table:", error)


def inserting(rectangle,rounded_rectangle,curved_rectangle,Pentagon,host,database,username,password):
    try:
        connection = psycopg2.connect(
            host=host,
            database=database,
            user=username,
            password=password

        )
        cursor = connection.cursor()

        sql_query = """
                     INSERT INTO SVG (rectangle, rounded_rectangle, curved_rectangle, Pentagon )
                     VALUES (%s,%s, %s, %s) 
                     
                     ;"""

        #rectangle,rounded_rectangle,curved_rectangle,Pentagon = extracting_data(root)
        max_length = max(len(rectangle), len(rounded_rectangle), len(curved_rectangle), len(Pentagon))

        for i in range(max_length):
            values = (
                rectangle[i] if i < len(rectangle) else None,
                rounded_rectangle[i] if i < len(rounded_rectangle) else None,
                curved_rectangle[i] if i < len(curved_rectangle) else None,
                Pentagon[i] if i < len(Pentagon) else None
            )

            cursor.execute(sql_query, values)
        connection.commit()
        cursor.close()
        connection.close()
        print("Data inserted successfully into PostgreSQL!")
    except psycopg2.Error as error:
        print("Error while connecting to PostgreSQL or inserting data:", error)
if __name__ == "__main__":
    host = "10.140.189.165"
    database = "Internal"
    username = "postgres"
    password = "techsol"
    port = "5432"
    folder_path = r"C:\Users\anusha.raparthi\Desktop\svg"
    svg_data = read_svg_file(folder_path)
    for filename,svg_content in svg_data.items():
        root = ET.fromstring(svg_content)
        desc_elements = find_desc_elements(root)
        #for desc_element in desc_elements:
            #print(desc_element.text)

        title_elements = find_title_elements(root)
        #for title_element in title_elements:
            #print(title_element.text)
        rectangle,rounded_rectangle,curved_rectangle,Pentagon=extracting_data(root)
        #print(rounded_rectangle)
        #for text in rectangle:
            #print(text)
        #print(len(desc_texts))
        creating(host,database,username,password)
        inserting(rectangle,rounded_rectangle,curved_rectangle,Pentagon,host,database,username,password)
