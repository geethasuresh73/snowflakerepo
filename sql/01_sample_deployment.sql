Drop CATALOG INTEGRATION glue_rest_catalog_int;
CREATE CATALOG INTEGRATION if not exists glue_rest_catalog_int;
  CATALOG_SOURCE = ICEBERG_REST
  
  TABLE_FORMAT = ICEBERG
  CATALOG_NAMESPACE = 'testnamespace'
  REST_CONFIG = (
    CATALOG_URI = 'https://glue.us-east-1.amazonaws.com/iceberg'
    CATALOG_API_TYPE = AWS_GLUE
    WAREHOUSE = '416124521039:s3tablescatalog/s3tables-snowflake-integration'
    ACCESS_DELEGATION_MODE = VENDED_CREDENTIALS
  )
  REST_AUTHENTICATION = (
    TYPE = SIGV4
    SIGV4_IAM_ROLE = 'arn:aws:iam::416124521039:role/snowflake_access_role'
    SIGV4_SIGNING_REGION = 'us-east-1'
  )
  REFRESH_INTERVAL_SECONDS = 30
  ENABLED = TRUE;
Describe CATALOG INTEGRATION glue_rest_catalog_int;