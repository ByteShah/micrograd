from micrograd import MLP

# Create a multi-layer perceptron
model = MLP(3, [4, 4, 1])

# Forward pass
inputs = [2.0, 3.0, -1.0]
output = model(inputs)

# Backward pass -
output.backward()

# # Visualize computation graph
from micrograd.engine import draw_dot
dot = draw_dot(output)
