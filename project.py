import pymysql as db
try:
    emp_id,name,mobile_no,email=input('Enter emp details:').split(' ')
    con=db.connect(host='127.0.0.1',port=3306,user='root',passwd="",db='vjit_db')#creating connections
    cur=con.cursor()#returns number of rows
    sql="insert into emp(emp_id,name,mobile_no,email)VALUES(%s,%s,%s,%s)"#sql is a variale which holds a query
    values=[emp_id,name,mobile_no,email]
    cur.execute(sql,values)
    con.commit()
    con.close()
    print('1 Record Save!!!')
except Exception as e:
    print('Error:',e)
str=input('enter your name:')
str=input('enter your rollnumber:')
try:
    sql='select*from emp WHERE emp=emp_id'
    cur.execute(sql,values)
    con.commit()
    con.close()
lan=input('enter the language')
if lan=='python':
    python=open('python.txt','r')
    for each in python:
        print (each)
    str=input('enter the file name')
    if str=='file1':
        file1=open('file1.txt','r')
        for each in file1:
            print (each)
    elif str=='file2':
        file2 = open('file2.txt', 'r')
        for each in file2:
            print (each)
    else:
        exit()
if lan=='Java':
    Java=open('java.txt','r')
    for each in Java:
        print (each)
    str=input('enter the file name')
    if str=='file3':
        file3=open('file3.txt','r')
        for each in file3:
            print (each)
    elif str=='file4':
        file4 = open('file4.txt', 'r')
        for each in file4:
            print (each)
    else:
        exit()
if lan=='html':
    html=open('html.txt','r')
    for each in html:
        print (each)
    str=input('enter the file name')
    if str=='file5':
        file5=open('file5.txt','r')
        for each in file5:
            print (each)
    elif str=='file6':
        file6 = open('file6.txt', 'r')
        for each in file6:
            print (each)
    else:
        exit()
if lan=='sql':
    sql=open('sql.txt','r')
    for each in sql:
        print (each)
    str=input('enter the file name')
    if str=='file7':
        file7=open('file7.txt','r')
        for each in file7:
            print (each)
    elif str=='file8':
        file8 = open('file8.txt', 'r')
        for each in file8:
            print (each)
    else:
        exit()

 
