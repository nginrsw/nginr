# Nginr

**nginr** is a Python syntax alternative (or dialect) that allows using the `fn` keyword instead of `def`. It is **not** a new programming language, but rather a **preprocessor** that converts `.xr` files into standard Python code before execution.

> Inspired by Python’s readability, Nginr adds a fun twist by using `fn` — making your code feel fresh-modern while staying fully compatible with Python.

---

## Features

- **Full Python Compatibility**: Use any Python3 library or framework
- **Alternative Syntax**: `fn` keyword instead of `def` | but still can use `def`
- **Seamless Integration**: Works with existing Python tooling
- **Lightweight**: Simple preprocessing with minimal overhead
- **Extensible**: Supports all Python 3.7+ syntax and libraries

---

## Installation

### Using pip (recommended)

```bash
pip install nginr
````

### From source

```bash
git clone https://github.com/nginrsw/nginr.git
cd nginr
pip install -e .
```

---

## Quick Start

1. Create a file with `.xr` extension:

```python
# hello.xr
fn hello(name):
    print(f"Hello, {name}!")

hello("World")
```

2. Run it with:

```bash
nginr hello.xr
```

---

## How It Works

Nginr is a simple preprocessor:

1. Reads `.xr` files
2. Replaces `fn` with `def`
3. Executes the resulting Python code

### Example Conversion

```python
# Input (hello.xr)
fn greet(name):
    print(f"Hi, {name}!")

# After preprocessing:
def greet(name):
    print(f"Hi, {name}!")
```

---

## More Examples

### Function with Parameters

```python
fn add(a, b):
    return a + b

result = add(5, 3)
print(f"5 + 3 = {result}")
```

### Loops and Conditionals

```python
fn factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

for i in range(1, 6):
    print(f"{i}! = {factorial(i)}")
```

### Using External Libraries

```python
fn calculate_stats(data):
    import numpy as np
    import pandas as pd

    df = pd.DataFrame(data)
    return {
        'mean': np.mean(df.values),
        'std': np.std(df.values),
        'sum': np.sum(df.values)
    }
```

### Using the Standard Library

```python
fn get_weather(city):
    import json
    from urllib.request import urlopen

    with urlopen(f'https://weather.example.com/api?city={city}') as response:
        return json.load(response)
```

---

## Python Library Compatibility

You can use **any** Python package in your `.xr` files.

Install them as usual:

```bash
pip install numpy pandas requests
```

---

## CLI Options

Run this to see available options:

```bash
nginr --help
```

You can also pass arguments to your `.xr` script:

```bash
nginr script.xr arg1 arg2
```

---

## Limitations

* Only performs basic `fn → def` substitution
* No new syntax or typing system
* `.xr` errors will show traceback in the transformed `.py` version
* No built-in macro system or advanced parsing (yet)

---

## Contributing

Contributions are welcome!

1. Fork the repo
2. Create a feature branch
   `git checkout -b feature/amazing-feature`
3. Commit your changes
   `git commit -m 'Add amazing feature'`
4. Push your branch
   `git push origin feature/amazing-feature`
5. Open a Pull Request

---

## License

Licensed under the [MIT License](LICENSE).
