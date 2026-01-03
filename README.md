# README.md

# Snowflake Project

This project is designed to deploy a sample schema and table in Snowflake using SQL scripts and Python. It includes a CI/CD pipeline for automated deployment and testing.

## Project Structure

```
snowflake-project
├── sql
│   └── sample_deployment.sql       # SQL statements for deploying the schema and table
├── scripts
│   └── deploy.py                    # Python script to execute SQL commands
├── tests
│   └── test_integration.py          # Integration tests for the deployment process
├── .gitlab-ci.yml                   # CI/CD pipeline configuration
├── requirements.txt                 # Python dependencies
└── README.md                        # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd snowflake-project
   ```

2. **Install dependencies:**
   Ensure you have Python installed, then run:
   ```
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   You need to set the following environment variables for Snowflake connection:
   - `SNOWFLAKE_ACCOUNT`
   - `SNOWFLAKE_USER`
   - `SNOWFLAKE_PASSWORD`
   - `SNOWFLAKE_WAREHOUSE`
   - `SNOWFLAKE_DATABASE`
   - `SNOWFLAKE_SCHEMA`

## Usage

To deploy the SQL commands, run the following command:
```
python scripts/deploy.py
```

## Testing

Integration tests can be run using:
```
pytest tests/test_integration.py
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.