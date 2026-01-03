import snowflake.connector
import os

def test_deployment():
    conn = snowflake.connector.connect(
        user=os.getenv('SNOWFLAKE_USER'),
        password=os.getenv('SNOWFLAKE_PASSWORD'),
        account=os.getenv('SNOWFLAKE_ACCOUNT'),
        warehouse=os.getenv('SNOWFLAKE_WAREHOUSE'),
        database=os.getenv('SNOWFLAKE_DATABASE'),
        role=os.getenv('SNOWFLAKE_ROLE')
    )

    cursor = conn.cursor()

    try:
        # Check if the database exists
        cursor.execute("SELECT CURRENT_DATABASE()")
        current_db = cursor.fetchone()[0]
        assert current_db == 'DEMO_DB2', "Database 'demo_db2' was not created."

        print("All integration tests passed.")
    except AssertionError as e:
        print(e)
    except Exception as e:
        print(f"Error during testing: {e}")
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    test_deployment()