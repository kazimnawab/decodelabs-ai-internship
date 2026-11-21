# Project 2: Data Classification Using AI

A supervised learning project built during my AI Internship at DecodeLabs (Batch 2026). The model classifies iris flowers into three species using the K-Nearest Neighbors (KNN) algorithm.

## Goal
Build a basic classification model on a small dataset: load the data, split it into training and testing sets, and apply a simple classification algorithm.

## Dataset
The Iris dataset (built into scikit-learn):
- 150 samples, perfectly balanced (50 per class)
- 4 features: sepal length, sepal width, petal length, petal width (cm)
- 3 classes: setosa, versicolor, virginica

## Pipeline (Input, Process, Output)
```
Input    -> load Iris data, check shape, class balance and missing values
Process  -> 80/20 shuffled train-test split, StandardScaler, KNN (K=5)
Output   -> accuracy, confusion matrix, precision / recall / F1 report
```

## What the code does
1. Loads the dataset into a pandas DataFrame and inspects it
2. Separates features (X) and label (y)
3. Splits the data 80/20 with `random_state=42`
4. Scales features. The scaler is fitted on the training data only, to avoid data leakage
5. Trains a KNN classifier and predicts on the test set
6. Evaluates with accuracy, confusion matrix and classification report
7. Compares K = 1 to 20 and plots the error rate
8. Predicts the species of a new flower

## Results
- Test accuracy with K=5: **100%** (30 test samples, `random_state=42`)
- Every flower type was classified correctly in the confusion matrix

Note: Iris is a small and easy dataset, so a perfect score is expected and does not mean the model is perfect on harder data. K was compared on the test set for learning purposes. A stricter approach would use cross-validation on the training data.

## Run it
```bash
pip install -r requirements.txt
python iris_classifier.py
```
Python 3.8 or newer.

## Concepts practiced
Supervised learning, features and labels, train-test split, feature scaling, data leakage, KNN, choosing K, confusion matrix, precision, recall, F1 score.

## Author
Kazim nawab, AI Intern at DecodeLabs