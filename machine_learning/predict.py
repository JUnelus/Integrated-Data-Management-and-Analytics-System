import joblib
import numpy as np

# Load the trained model
model = joblib.load('machine_learning/models/random_forest.joblib')

def predict_transaction(amount):
    amount_log = np.log(amount + 1).reshape(1, -1)
    prediction = model.predict(amount_log)
    category = 'High' if prediction[0] == 1 else 'Normal'
    return category

if __name__ == "__main__":
    sample_amount = 750.0
    category = predict_transaction(sample_amount)
    print(f"Transaction amount: {sample_amount} categorized as {category}")
