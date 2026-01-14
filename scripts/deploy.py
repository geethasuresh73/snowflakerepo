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
    print(sql_files)
    try:
        for sql_file in sql_files:
            with open(f"sql/{sql_file}", 'r') as f:
                sql_content = f.read()
                # Execute multiple SQL statements separated by semicolons
                for statement in sql_content.split(';'):
                    statement = statement.strip()
                    if statement:
                        cursor.execute(statement)
            print(f"Deployment successful for {sql_file}.")
        conn.commit()
    except Exception as e:
        print(f"Error during deployment: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    deploy_sql()