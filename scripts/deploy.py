import snowflake.connector
import os


def deploy_sql():
    conn = snowflake.connector.connect(
        user=os.getenv('SNOWFLAKE_USER'),
        password=os.getenv('SNOWFLAKE_PASSWORD'),
        account=os.getenv('SNOWFLAKE_ACCOUNT'),
        warehouse=os.getenv('SNOWFLAKE_WAREHOUSE'),
        database=os.getenv('SNOWFLAKE_DATABASE'),
        role=os.getenv('SNOWFLAKE_ROLE')
    )

    cursor = conn.cursor()

    with open('sql/sample_deployment.sql', 'r') as sql_file:
        sql_commands = sql_file.read()

    try:
        cursor.execute(sql_commands)
        print("Deployment successful.")
    except Exception as e:
        print(f"Error during deployment: {e}")
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    deploy_sql()