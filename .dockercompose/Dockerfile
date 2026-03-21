    FROM python:3.11

WORKDIR /workspace

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    git \
    curl \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Copiar e instalar requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt || echo "requirements.txt vazio ou não existe"

# Instalar dependências do postCreateCommand
RUN pip install --no-cache-dir pandas psycopg2-binary

CMD ["bash"]
