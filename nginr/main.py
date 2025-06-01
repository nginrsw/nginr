#!/usr/bin/env python3
"""
Nginr Interpreter - Python with fn syntax
"""

import sys
import re
from pathlib import Path

def preprocess_source(source):
    """Preprocess source code to replace 'fn' with 'def'"""
    lines = []
    for line in source.splitlines(keepends=True):
        # Hanya proses baris yang mengandung 'fn' yang merupakan awal kata
        if re.search(r'\bfn\b', line):
            # Ganti 'fn' di awal fungsi
            line = re.sub(r'\bfn\s+([a-zA-Z_][a-zA-Z0-9_]*\s*\()', r'def \1', line)
        lines.append(line)
    return ''.join(lines)

def run_file(file_path):
    """Run a .xg file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            source = f.read()
        
        # Preprocess the source
        processed_source = preprocess_source(source)
        
        # Compile and execute the code
        code = compile(processed_source, file_path, 'exec')
        exec(code, {'__name__': '__main__', '__file__': file_path})
        
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error executing {file_path}: {e}", file=sys.stderr)
        sys.exit(1)

def print_version():
    """Print version information"""
    try:
        from importlib.metadata import version
        print(f"nginr {version('nginr')}")
    except ImportError:
        print("nginr (version unknown - not installed as package)")

def print_usage():
    """Print usage information"""
    print("Usage: nginr [--version] <file.xg>")
    print("\nOptions:")
    print("  --version  Show version and exit")

def main():
    # Handle --version flag
    if '--version' in sys.argv or '-v' in sys.argv:
        print_version()
        return 0
    
    # Handle no arguments or help
    if len(sys.argv) < 2 or sys.argv[1] in ('-h', '--help'):
        print_usage()
        return 1 if len(sys.argv) < 2 else 0
    
    file_path = sys.argv[1]
    
    # Check file extension
    if not file_path.endswith('.xg'):
        print("Error: File must have .xg extension", file=sys.stderr)
        print_usage()
        return 1
    
    # Run the file
    run_file(file_path)
    return 0

if __name__ == '__main__':
    sys.exit(main())
