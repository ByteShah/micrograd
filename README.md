# Micrograd: A Tiny Autograd Engine for Neural Networks

Micrograd is a lightweight autograd engine and a small neural network library built in Python. It provides a way to build and train neural networks with automatic differentiation.

## Installation

You can install Micrograd using pip:

```sh
pip install micrograd
```

If you want to install it from source:

```sh
git clone https://github.com/ByteShah/micrograd.git
cd micrograd
pip install -e .
```

## Usage

### Importing Micrograd

```python
from micrograd import MLP, draw_dot
```

### Creating and Using a Neural Network

```python
# Define a simple Multi-Layer Perceptron (MLP)
model = MLP(3, [4, 4, 1])

# Forward pass
inputs = [2.0, 3.0, -1.0]
output = model(inputs)
print("Output:", output)

# Backward pass
output.backward()
```

### Visualizing the Computation Graph

```python
from micrograd import draw_dot

dot = draw_dot(output)
dot.render("computation_graph", format="png")  # Saves as computation_graph.png
```

## Development & Contribution

To contribute, clone the repository and install dependencies:

```sh
git clone https://github.com/ByteShah/micrograd.git
cd micrograd
pip install -e .
```

### `.gitignore` (Recommended)

To keep your repository clean, add the following `.gitignore` file:

```
# Virtual environment
env/

# Bytecode files
__pycache__/
*.py[cod]

# Distribution files
*.egg-info/
```

## Publishing to PyPI

1. **Build the package:**
   ```sh
   python setup.py sdist bdist_wheel
   ```

2. **Upload to PyPI:**
   ```sh
   pip install twine
   twine upload dist/*
   ```

3. **Verify installation:**
   ```sh
   pip install micrograd
   ```

## License

MIT License. See `LICENSE` for details.

---

For issues or contributions, visit: [GitHub Repo](https://github.com/ByteShah/micrograd).

