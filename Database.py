import psycopg2

connection = psycopg2.connect(
    host = "localhost",
    dbname = "PulseAndPaw",
    user = "postgres",
    password = "Ramita@2005",
    port = "5432"
)

cur = connection.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS Employees (
    EmployeeID INT PRIMARY KEY,
    Name VARCHAR(50),
    Department VARCHAR(50)
);
""")

cur.execute("""INSERT INTO Employees (EmployeeID, Name, Department)
VALUES
(1, 'Alice Johnson', 'HR'),
(2, 'Bob Smith', 'IT'),
(3, 'Charlie Brown', 'Finance');
""")

connection.commit()
cur.close()
connection.close()

import psycopg2

connection = psycopg2.connect(
    host = "localhost",
    dbname = "PulseAndPaw",
    user = "postgres",
    password = "Ramita@2005",
    port = "5432"
)

cur = connection.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS Employees (
    EmployeeID INT PRIMARY KEY,
    Name VARCHAR(50),
    Department VARCHAR(50)
);
""")

cur.execute("""INSERT INTO Employees (EmployeeID, Name, Department)
VALUES
(1, 'Alice Johnson', 'HR'),
(2, 'Bob Smith', 'IT'),
(3, 'Chor Chotta', 'CSE');
""")

connection.commit()
cur.close()
connection.close()

