import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# 1. Load the data
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["species"] = iris.target_names[iris.target]

print(df.head())
print("Shape:", df.shape)
print(df["species"].value_counts())
print("Missing values:\n", df.isnull().sum())

# 2. Split features and label, then train/test (80/20)
X = df[iris.feature_names]
y = df["species"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print("Train:", X_train.shape, "Test:", X_test.shape)

# 3. Scale the features (fit on training data only)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 4. Train the KNN model and predict
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train_scaled, y_train)
predictions = model.predict(X_test_scaled)

# 5. Evaluate
print("\nAccuracy:", accuracy_score(y_test, predictions))
print("\nConfusion matrix:\n", confusion_matrix(y_test, predictions))
print("\nClassification report:\n", classification_report(y_test, predictions))

# 6. Try different values of K
k_values = range(1, 21)
accuracies = []
for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train_scaled, y_train)
    accuracies.append(accuracy_score(y_test, knn.predict(X_test_scaled)))
for k, acc in zip(k_values, accuracies):
    print(f"K={k}: accuracy={acc:.3f}")

best_k = k_values[accuracies.index(max(accuracies))]
print("Best K:", best_k)

error_rates = [1 - a for a in accuracies]
plt.plot(k_values, error_rates, marker="o")
plt.xlabel("K value")
plt.ylabel("Error rate")
plt.title("Choosing K")
plt.savefig("k_vs_error.png")
plt.show()

# 7. Predict a brand new flower
new_flower = pd.DataFrame([[5.1, 3.5, 1.4, 0.2]], columns=iris.feature_names)
new_flower_scaled = scaler.transform(new_flower)
print("\nNew flower prediction:", model.predict(new_flower_scaled)[0])