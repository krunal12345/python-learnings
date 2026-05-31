import pyodbc

conn = pyodbc.connect(
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=(localdb)\\MSSQLLocalDB;"
    "DATABASE=python_learnings;"
    "Trusted_Connection=yes;"
    "Encrypt=yes;"
    "TrustServerCertificate=yes;"
)

SQL_QUERY = """
SELECT
 * FROM dummytable;
"""

data = conn.execute(SQL_QUERY)

records = data.fetchall()
for r in records:
    print(f"{r}")
