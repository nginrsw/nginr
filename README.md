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
fn hello(name: str) -> None:
    print(f"Hello, {name}!")

hello("World")
```

2. Run it with:

```bash
nginr hello.xr
```

---

## Initializing a New Project

Nginr can also help you quickly set up a new project structure. Use the `init` command:

```bash
nginr init your_project_name
```

This will create a directory named `your_project_name` with the following structure:

```
your_project_name/
├── README.md
├── requirements.txt
├── nginr_config.yaml
├── docs/
│   ├── architecture.md
│   ├── api.md
│   └── dev-notes.md
├── src/
│   ├── __init__.py
│   └── main.xr
├── tests/
│   └── test_main.xr
└── .gitignore
```

The `src/main.xr` will contain a simple "Hello from nginr!" program, and `README.md` will be pre-filled with the project title. Other files are created as placeholders for you to fill in.

If the target directory already exists, `nginr init` will display an error and will not overwrite existing files.

---

## How It Works

Nginr is a simple preprocessor:

1. Reads `.xr` files
2. Replaces `fn` with `def`
3. Executes the resulting Python code

### Example Conversion

```python
# Input (hello.xr)
fn greet(name: str) -> None:
    print(f"Hi, {name}!")

# After preprocessing:
def greet(name):
    print(f"Hi, {name}!")
```

---

## More Examples

### Function with Parameters

```python
fn add(a: int, b: int) -> int:
    return a + b

result = add(5, 3)
print(f"5 + 3 = {result}")
```

### Loops and Conditionals

```python
fn factorial(n: int) -> int:
    if n <= 1:
        return 1
    return n * factorial(n - 1)

for i in range(1, 6):
    print(f"{i}! = {factorial(i)}")
```

### Using External Libraries

```python
fn calculate_stats(data: Any) -> Dict[str, float]:
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
fn get_weather(city: str) -> Any:
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

Nginr provides the following command-line options:

*   `nginr <file.xr> [args...]`: Runs an `.xr` script. You can pass arguments to your script as well.
    ```bash
    nginr script.xr arg1 arg2
    ```
*   `nginr init <project_name>`: Initializes a new Nginr project structure.
    ```bash
    nginr init my_new_app
    ```
*   `nginr --help`: Shows the help message, including available commands and options.
*   `nginr --version`: Shows the installed Nginr version.

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
