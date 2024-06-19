import sqlite3

conn = sqlite3.connect("mycomapany.db")
cObj = conn.cursor()
"""All queries are done here"""

# cObj.execute("CREATE TABLE employees(id INTEGER primary key , name Text, salary REAL,department TEXT, position TEXT )")
# conn.commit()
def insert_values(id,name,salary,department,position):
    cObj.execute("insert into employees values(?,?,?,?,?)",(3,name,salary,department,position))
    conn.commit()
def update_department(department):
        cObj.execute("UPDATE employees set department ='Python' where id =3")
        conn.commit()

def select_all():
        cObj.execute("select *from employees")
        result = cObj.fetchall()
        for item in result:
            print(item)
# conn.commit()
def delete_all():
    cObj.execute("delete from employees")
    conn.commit()
# insert_values(3,"Gashaw",15400, "Software Engineering","Software Engineer")
# delete_all()
cObj.close()
conn.close()

