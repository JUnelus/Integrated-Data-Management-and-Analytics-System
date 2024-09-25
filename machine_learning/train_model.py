import os
import snowflake.connector
from dotenv import load_dotenv
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib

# Load the .env file
load_dotenv()


def load_data():
    # Get Snowflake credentials from environment variables
    user = os.getenv('SNOWFLAKE_USER')
    password = os.getenv('SNOWFLAKE_PASSWORD')
    account = os.getenv('SNOWFLAKE_ACCOUNT')
    warehouse = os.getenv('SNOWFLAKE_WAREHOUSE')
    database = os.getenv('SNOWFLAKE_DATABASE')
    schema = os.getenv('SNOWFLAKE_SCHEMA')

    # Connect to Snowflake
    conn = snowflake.connector.connect(
        user=user,
        password=password,
        account=account,
        warehouse=warehouse,
        database=database,
        schema=schema
    )

    # Execute the query
    query = "SELECT * FROM final_transactions"
    df = pd.read_sql(query, conn)

    # Close the connection
    conn.close()

    return df


def train_model():
    df = load_data()
    # Feature engineering
    df['amount_log'] = df['amount'].apply(lambda x: np.log(x + 1))
    X = df[['amount_log']]
    y = df['transaction_category'].apply(lambda x: 1 if x == 'High' else 0)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    print(classification_report(y_test, predictions))

    # Save the model
    joblib.dump(model, 'machine_learning/models/random_forest.joblib')


if __name__ == "__main__":
    train_model()
