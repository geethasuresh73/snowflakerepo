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

    sql_files = sorted([f for f in os.listdir('sql') if f.endswith('.sql')])
    print (sql_files)
    try:
        for sql_file in sql_files:
            with open("sql/{sql_file}", 'r') as f:
                cursor.execute(f.read())
            print("Deployment successful 1.")
    except Exception as e:
        print(f"Error during deployment 1: {e}")
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    deploy_sql()