from pathlib import Path
from setuptools import setup, find_packages

# Read the contents of README.md
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name="nginr",
    version="0.1.8",  
    packages=find_packages(include=['nginr*']),
    entry_points={
        'console_scripts': [
            'nginr=nginr.main:main',
        ],

    },
    python_requires='>=3.7',
    install_requires=[
        # Core dependencies
    ],
    extras_require={
        'dev': [
            'pytest>=6.0',
            'black>=21.0',
            'isort>=5.0',
            'mypy>=0.910',
        ],
    },
    package_data={
        'nginr_pyright': ['*.js'],
    },
    author="Gillar Prasatya",
    author_email="nginrsw@gmail.com",
    description="Nginr - Python Alt syntax with fn keyword and .xr files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nginrsw/nginr",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Typing :: Typed",
    ],
    keywords='python syntax preprocessor language-extension',
    project_urls={
        'Bug Reports': 'https://github.com/nginrsw/nginr/issues',
        'Source': 'https://github.com/nginrsw/nginr',
    },
)
