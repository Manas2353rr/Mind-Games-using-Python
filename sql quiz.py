import mysql.connector as my

mydb = my.connect(user='root' , password='Manas@2353r' ,
host='localhost',
database='quiz')

#Step III: Create a temporary memory buffer to store rows known as cursor [Use dictionary
internally=dictionary=True
cursor=mydb.cursor(dictionary=True)

#Step IV: Now we can perform any SQL Query here
sql="select qid, question, category from questions"

#Step V: Execute it
cursor.execute(sql)

#Step VI: Fetch all rows from Cursor into a Dictionary
records=cursor.fetchall()

#Step VI: Dictionary Traversal using for loop to Display rows
print("Qid\tQuestion\tCategory")
for row in records:
    print(row["qid"], "\t", row["question"] , '\t' , row['category'])

#Step VII: Free memory by closing cursor
cursor.close()

#Step VIII: Important to close database connection at the end
mydb.close()
