import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib

# Load data from Snowflake
def load_data():
    import snowflake.connector
    conn = snowflake.connector.connect(
        user='junelus',
        password='SnowFlake924!',
        account='mfkwhap-nu09395',
        warehouse='COMPUTE_WH',
        database='MY_DB',
        schema='PUBLIC'
    )
    query = "SELECT * FROM final_transactions"
    df = pd.read_sql(query, conn)
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
