import os
import dill
import numpy as np
from sklearn.metrics import r2_score

def save_object(file_path, obj):
    """
    Saves a Python object to a file using dill serialization.
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)
    except Exception as e:
        raise Exception(f"Error saving object: {e}")

def load_object(file_path):
    """
    Loads a Python object from a dill file.
    """
    try:
        with open(file_path, 'rb') as file_obj:
            return dill.load(file_obj)
    except Exception as e:
        raise Exception(f"Error loading object: {e}")

def evaluate_model(X_train, y_train, X_test, y_test, models: dict):
    """
    Evaluate multiple models and return their R2 scores.
    """
    report = {}
    for name, model in models.items():
        model.fit(X_train, y_train)
        y_train_pred = model.predict(X_train)
        y_test_pred = model.predict(X_test)

        train_score = r2_score(y_train, y_train_pred)
        test_score = r2_score(y_test, y_test_pred)

        report[name] = test_score

    return report
