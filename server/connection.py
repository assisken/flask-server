import psycopg


def init_database_connection(
    host: str = "localhost",
    port: int = 5432,
    database: str = "master",
    user: str = "postgres",
    password: str = "postgres",
):
    return psycopg.connect(f"postgres://{user}:{password}@{host}:{port}/{database}")
