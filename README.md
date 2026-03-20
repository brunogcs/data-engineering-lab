# 🚀 Data Engineering Lab

> Modern Data Engineering Laboratory - Docker-based environment for learning and implementing data pipelines. Features orchestration with Airflow, data warehousing with PostgreSQL, and extensible architecture for streaming (Kafka), transformation (DBT), and processing (Spark).

## 🏗️ Architecture

### Current Stack
- **PostgreSQL 15** - Data warehouse and storage
- **Apache Airflow 2.7.1** - Workflow orchestration
- **Python 3** - Data processing and transformation
- **Docker & Docker Compose** - Containerization

### Planned Additions
- 🔄 **Kafka** - Real-time data streaming
- 🔧 **DBT** - Data transformation and modeling
- ⚡ **Spark** - Big data processing

## 🚀 Quick Start

### Prerequisites
- Docker and Docker Compose installed
- Git (for cloning)

### Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd data-engineering-lab
   ```

2. **Start all services**
   ```bash
   docker-compose up -d
   ```

3. **Verify services**
   - PostgreSQL: `localhost:5432`
   - Airflow UI: `http://localhost:8080`
   - Default Airflow credentials: admin/admin

## 📁 Project Structure

```
data-engineering-lab/
├── docker-compose.yml          # Orchestration of all services
├── requirements.txt            # Python dependencies
├── dags/                      # Airflow DAGs
│   └── pipeline_dag.py        # Main data pipeline DAG
├── scripts/                   # Data processing scripts
│   └── pipeline.py            # Sample ETL pipeline
└── README.md                  # This file
```

## 🔧 Services Configuration

### PostgreSQL
- **Host**: localhost:5432
- **Database**: warehouse
- **User**: data
- **Password**: data

### Airflow
- **UI**: http://localhost:8080
- **Executor**: SequentialExecutor
- **Database**: PostgreSQL (shared)

### Python Service
- **Base Image**: Custom build from Dockerfile
- **Dependencies**: Defined in requirements.txt
- **Mount**: Scripts directory

## 📊 Sample Pipeline

The project includes a sample ETL pipeline that:

1. **Extract**: Creates sample data with pandas
2. **Transform**: Processes the data structure
3. **Load**: Inserts into PostgreSQL warehouse

**Run manually:**
```bash
docker-compose exec python python scripts/pipeline.py
```

**Run via Airflow:**
1. Access Airflow UI at http://localhost:8080
2. Enable the `data_pipeline` DAG
3. Trigger manually or wait for schedule

## 🔮 Roadmap

- [ ] Add Kafka for real-time streaming
- [ ] Integrate DBT for data transformations
- [ ] Implement Spark for big data processing
- [ ] Add monitoring and logging
- [ ] Create CI/CD pipelines
- [ ] Add data quality checks
- [ ] Implement security best practices

## 🛠️ Development

### Adding New DAGs
1. Create Python files in `/dags/` directory
2. Follow Airflow DAG conventions
3. Restart Airflow service if needed

### Extending Services
1. Update `docker-compose.yml` with new services
2. Add necessary environment variables
3. Configure networking with `data-net`

### Dependencies
Add Python packages to `requirements.txt`:
```txt
pandas
psycopg2-binary
apache-airflow
```

## 🧪 Testing

### Test Database Connection
```bash
docker-compose exec python python -c "
import psycopg2
conn = psycopg2.connect(host='postgres', database='warehouse', user='data', password='data')
print('Database connection successful!')
"
```

### Test Airflow
```bash
curl http://localhost:8080/health
```

## 📚 Learning Resources

- [Apache Airflow Documentation](https://airflow.apache.org/docs/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [Docker Compose Reference](https://docs.docker.com/compose/)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙋‍♂️ Support

For questions and support:
- Open an issue on GitHub
- Check the documentation
- Review existing issues

---

**Built with ❤️ for the Data Engineering Community**
