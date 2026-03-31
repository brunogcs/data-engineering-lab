import pandas as pd
import psycopg2
import boto3
import csv
from datetime import datetime

#Simulação de pipeline de dados: leitura, transformação e carga em um banco de dados PostgreSQL

data = [
    {"name": "ana", "age": 25},
    {"name": "joao", "age": 30},
    {"name": "maria", "age": 28}
]

df = pd.DataFrame(data)

conn = psycopg2.connect(
    host="postgres",
    port=5432,
    user="data",
    password="data",
    database="warehouse"
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


# Simulação de upload de arquivo para o Amazon S3

print ("Parte 2 - Upload para S3 e registro de metadados no Postgres")

# =========================
# 1. CONFIGURAÇÕES
# =========================

# S3 (LocalStack)
s3 = boto3.client(
    "s3",
    endpoint_url="http://localstack:4566",  # importante!
    aws_access_key_id="brunoserver",
    aws_secret_access_key="brunoserver",
    region_name="us-east-1"
)

BUCKET_NAME = "data-lake"
FILE_NAME = "dados.csv"

# Postgres
conn = psycopg2.connect(
    host="postgres",
    port=5432,
    database="warehouse",
    user="data",
    password="data"
)

# =========================
# 2. CRIAR CSV LOCAL
# =========================

data = [
    ["id", "nome", "valor"],
    [1, "produto_a", 100],
    [2, "produto_b", 200],
    [3, "produto_c", 300],
]

with open(FILE_NAME, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)

print("CSV criado")

# =========================
# 3. ENVIAR PARA S3
# =========================

s3.upload_file(FILE_NAME, BUCKET_NAME, FILE_NAME)

print("Arquivo enviado para S3")

# =========================
# 4. SALVAR METADADOS NO POSTGRES
# =========================

cursor = conn.cursor()

# criar tabela se não existir
cursor.execute("""
CREATE TABLE IF NOT EXISTS arquivos_s3 (
    id SERIAL PRIMARY KEY,
    nome_arquivo TEXT,
    bucket TEXT,
    data_upload TIMESTAMP
);
""")

# inserir registro
cursor.execute("""
INSERT INTO arquivos_s3 (nome_arquivo, bucket, data_upload)
VALUES (%s, %s, %s);
""", (FILE_NAME, BUCKET_NAME, datetime.now()))

conn.commit()

print("Metadado salvo no Postgres")

# fechar conexões
cursor.close()
conn.close()