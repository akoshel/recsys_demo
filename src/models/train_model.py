import numpy as np
import joblib
from sklearn.linear_model import LinearRegression

if __name__ == "__main__":
    model = LinearRegression()
    X = np.random.rand(100, 5)
    y = np.random.rand(100)
    model.fit(X, y)
    joblib.dump(model, 'models/model.joblib') 