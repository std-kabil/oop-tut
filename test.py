import torch
import torch.nn as nn
import torch.nn.functional as F

class SimpleNet(nn.Module):
    def __init__(self):
        super().__init__()
        # Define the layers of the network
        # Example: two fully connected (linear) layers
        self.fc1 = nn.Linear(784, 128) # Input size 784 (e.g., for flattened 28x28 images), output 128
        self.fc2 = nn.Linear(128, 10)  # Input 128, output 10 (e.g., for 10 classes)

    def forward(self, x):
        # Define how data passes through the network
        # Apply activation functions (e.g., ReLU) to the output of the first layer
        x = self.fc1(x)
        x = F.relu(x)
        # Pass through the second layer
        x = self.fc2(x)
        x = F.sigmoid(x)
        return x

# Example usage:
# Create an instance of the model
model = SimpleNet()

# Create a dummy input tensor (e.g., a batch of 64 flattened 28x28 images)
dummy_input = torch.randn(64, 784)

# Pass the input through the model
output = model.forward(dummy_input)

print("Model architecture:")
print(model)
print("\nOutput shape:")
print(output.shape)