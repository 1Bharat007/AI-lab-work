import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


class NeuralNetworkScratch:

  def __init__(self, input_dim, hidden_dim, lr=0.05):
    self.lr = lr
    # He initialization for ReLU
    self.W1 = np.random.randn(input_dim, hidden_dim) * np.sqrt(2.0 / input_dim)
    self.b1 = np.zeros((1, hidden_dim))
    # Xavier initialization for Sigmoid output
    self.W2 = np.random.randn(hidden_dim, 1) * np.sqrt(1.0 / hidden_dim)
    
    self.b2 = np.zeros((1, 1))

  def relu(self, z):
    return np.maximum(0, z)

  def relu_derivative(self, z):
    return (z > 0).astype(float)

  def sigmoid(self, z):
    return 1.0 / (1.0 + np.exp(-np.clip(z, -500, 500)))

  def forward(self, X):
    self.Z1 = np.dot(X, self.W1) + self.b1
    self.A1 = self.relu(self.Z1)
    self.Z2 = np.dot(self.A1, self.W2) + self.b2
    self.A2 = self.sigmoid(self.Z2)
    return self.A2

  def backward(self, X, y):
    m = X.shape[0]

    # Output layer gradients (dLoss/dZ2 for BCE with Sigmoid)
    dZ2 = self.A2 - y
    dW2 = (1 / m) * np.dot(self.A1.T, dZ2)
    db2 = (1 / m) * np.sum(dZ2, axis=0, keepdims=True)

    # Hidden layer gradients
    dA1 = np.dot(dZ2, self.W2.T)
    dZ1 = dA1 * self.relu_derivative(self.Z1)
    dW1 = (1 / m) * np.dot(X.T, dZ1)
    db1 = (1 / m) * np.sum(dZ1, axis=0, keepdims=True)

    # Parameter update step
    self.W2 -= self.lr * dW2
    self.b2 -= self.lr * db2
    self.W1 -= self.lr * dW1
    self.b1 -= self.lr * db1

  def train(self, X, y, epochs=200):
    for epoch in range(epochs):
      preds = self.forward(X)
      # Binary Cross-Entropy loss
      eps = 1e-15
      loss = -np.mean(
          y * np.log(preds + eps) + (1 - y) * np.log(1 - preds + eps)
      )
      self.backward(X, y)

      if (epoch + 1) % 50 == 0:
        print(f"Epoch [{epoch + 1}/{epochs}] - Loss: {loss:.4f}")

  def predict(self, X):
    return (self.forward(X) >= 0.5).astype(int)


# Test run
X, y = make_classification(n_samples=1000, n_features=10, random_state=42)
X = StandardScaler().fit_transform(X)
y = y.reshape(-1, 1)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

nn_scratch = NeuralNetworkScratch(input_dim=10, hidden_dim=16, lr=0.1)
nn_scratch.train(X_train, y_train, epochs=200)

accuracy = np.mean(nn_scratch.predict(X_test) == y_test)
print(f"NumPy Scratch Accuracy: {accuracy * 100:.2f}%")