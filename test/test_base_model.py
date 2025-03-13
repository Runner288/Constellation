# test/test_base_model.py

from libra.models.base_model import BaseModel

# Example Test
class DummyModel(BaseModel):
    def train(self, X_train, y_train):
        print("Training Dummy Model")

    def predict(self, X_test):
        print(f"X_test={X_test}")
        return ["dummy"] * len(X_test)

# Test if the dummy model works
if __name__ == "__main__":
    model = DummyModel()
    model.train([], [])
    predictions = model.predict([1, 2, 3])
    print(predictions)  # Output: ['dummy', 'dummy', 'dummy']
