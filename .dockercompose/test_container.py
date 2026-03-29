import docker
import sys

def check_containers(container_names):
    client = docker.from_env()
    all_running = True
    
    print("--- Verificando Saúde do Laboratório de Dados ---")
    
    for name in container_names:
        try:
            container = client.containers.get(name)
            state = container.attrs['State']['Status']
            
            if state == 'running':
                print(f"✅ {name}: {state}")
            else:
                print(f"❌ {name}: {state}")
                all_running = False
        except docker.errors.NotFound:
            print(f"⚠️ {name}: Não encontrado")
            all_running = False

    return all_running

if __name__ == "__main__":
    # Nomes definidos no seu docker-compose.yml
    meus_containers = [
        "data_lab_postgres",
        "data_lab_redis",
        "airflow_webserver",
        "airflow_scheduler",
        "airflow_worker",
        "data_lab_devcontainer",
        "localstack"
    ]
    
    if not check_containers(meus_containers):
        sys.exit(1) # Falha o processo se algo estiver fora do ar