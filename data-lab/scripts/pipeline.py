import pandas as pd
import psycopg2

data = [
    {"name": "ana", "age": 25},
    {"name": "joao", "age": 30},
    {"name": "maria", "age": 28}
]

df = pd.DataFrame(data)

conn = psycopg2.connect(
    host="localhost",
    database="warehouse",
    user="data",
    password="data"
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS people (
    name TEXT,
    age INT
)
""")

for _, row in df.iterrows():
    cursor.execute(
        "INSERT INTO people VALUES (%s,%s)",
        (row["name"], row["age"])
    )

conn.commit()

print("dados inseridos")
