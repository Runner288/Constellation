# base_model.py

from abc import ABC, abstractmethod
import joblib   #It is used efficient serialization and deserialization of Python objects.

class BaseModel(ABC):
    """
    Abstract base class for all machine learning models.
    """

    def __init__(self):
        self.model = None

    @abstractmethod
    def train(self, X_train, y_train):
        """Train the model."""
        pass

    @abstractmethod
    def predict(self, X_test):
        """Make predictions with the model."""
        pass

    def save_model(self, filepath):
        """Save the trained model to a file."""
        if self.model:
            joblib.dump(self.model, filepath)
            print(f"Model saved to {filepath}")
        else:
            raise ValueError("No model found to save.")

    def load_model(self, filepath):
        """Load a trained model from a file."""
        self.model = joblib.load(filepath)
        print(f"Model loaded from {filepath}")
