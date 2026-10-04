import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression

from sklearn.metrics import accuracy_score

# Load Dataset
df = pd.read_csv("dataset/phishing.csv")

# Remove extra spaces
df.columns = df.columns.str.strip()

# Drop index column
df = df.drop("index", axis=1)

# Features and Target
X = df.drop("Result", axis=1)
y = df["Result"]

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Models
models = {
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "Random Forest": RandomForestClassifier(random_state=42)
}

best_accuracy = 0
best_model = None

print("\n========== MODEL ACCURACY ==========\n")

for name, model in models.items():

    model.fit(X_train, y_train)

    prediction = model.predict(X_test)

    accuracy = accuracy_score(y_test, prediction)

    print(f"{name}: {accuracy:.4f}")

    if accuracy > best_accuracy:
        best_accuracy = accuracy
        best_model = model

# Save Best Model
joblib.dump(best_model, "models/phishing_model.pkl")

print("\nBest Accuracy:", round(best_accuracy, 4))
print("Model saved successfully!")