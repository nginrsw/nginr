#!/usr/bin/env python3
"""
Nginr Interpreter - Python with fn syntax
"""

import sys
import re
import argparse
import os
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
    """Run a .xr file"""
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

def generate_project(project_name: str):
    """Generates the project structure for the given project name."""
    project_path = Path(project_name)

    if project_path.exists():
        print(f"Error: Directory '{project_name}' already exists.", file=sys.stderr)
        sys.exit(1)

    try:
        # Create root project directory
        project_path.mkdir()

        # Create README.md
        with open(project_path / "README.md", "w", encoding="utf-8") as f:
            f.write(f"# Project: {project_name}\n\nHello from nginr!")

        # Create requirements.txt (empty)
        (project_path / "requirements.txt").touch()

        # Create nginr_config.yaml (empty)
        (project_path / "nginr_config.yaml").touch()

        # Create docs directory and files
        docs_path = project_path / "docs"
        docs_path.mkdir()
        (docs_path / "architecture.md").touch()
        (docs_path / "api.md").touch()
        (docs_path / "dev-notes.md").touch()

        # Create src directory and files
        src_path = project_path / "src"
        src_path.mkdir()
        (src_path / "__init__.py").touch()
        with open(src_path / "main.xr", "w", encoding="utf-8") as f:
            f.write("fn main() -> None:\n    print(\"Hello from nginr!\")\n\nif __name__ == \"__main__\":\n    main()\n")

        # Create tests directory and files
        tests_path = project_path / "tests"
        tests_path.mkdir()
        (tests_path / "test_main.xr").touch()

        # Create .gitignore
        with open(project_path / ".gitignore", "w", encoding="utf-8") as f:
            f.write("__pycache__/\n*.py[cod]\n*$py.class\n\n# Distribution / packaging\n.Python\nbuild/\ndevelop-eggs/\ndist/\ndownloads/\neggs/\n.eggs/\nlib/\nlib64/\nparts/\nsdist/\nvar/\nwheels/\n*.egg-info/\n.installed.cfg\n*.egg\nMANIFEST\n\n# Virtualenv\n.env\n.venv\nenv/\nvenv/\nENV/\n\n# IDE specific files\n.vscode/\n.idea/\n*.sublime-project\n*.sublime-workspace\n")

        print(f"Project '{project_name}' initialized successfully.")

    except OSError as e:
        print(f"Error creating project '{project_name}': {e}", file=sys.stderr)
        if project_path.exists():
            import shutil
            shutil.rmtree(project_path)
        sys.exit(1)

def get_nginr_version():
    """Helper function to get nginr version for argparse"""
    try:
        from importlib.metadata import version
        return version('nginr')
    except ImportError:
        try:
            # Fallback for development mode, assuming setup.py is in parent dir
            # This is a simplified example; a real app might use a __version__ file
            # For now, we'll hardcode the current known version as a dev fallback.
            # A more robust solution would read it from setup.py or a version file.
            return "0.1.7 (dev)" 
        except Exception:
            return "(version unknown)"

def main():
    parser = argparse.ArgumentParser(
        description="Nginr - Python Alt syntax with fn keyword and .xr files",
        # Removed custom usage to let argparse generate it, which might be more accurate with subparsers
    )
    parser.add_argument(
        '--version', 
        action='version', 
        version=f"nginr {get_nginr_version()}", 
        help="Show version and exit"
    )

    # This will hold the file path if it's not a subcommand
    parser.add_argument(
        'file_or_command', 
        nargs='?', 
        default=None, 
        help="Either an .xr file to run, or the 'init' command."
    )
    # This will hold the project name if the command is 'init'
    parser.add_argument(
        'project_name_arg', 
        nargs='?', 
        default=None, 
        help="The project name (only used with 'init' command)."
    )

    # Parse known args first to check for --version or --help, which exit early.
    # We use parse_known_args because 'init' might be followed by project_name, 
    # which could be misinterpreted if not handled carefully.
    args, unknown_args = parser.parse_known_args()

    if args.file_or_command == 'init':
        if args.project_name_arg:
            generate_project(args.project_name_arg)
        else:
            # Re-parse with a specific init parser to show proper error for missing project_name
            init_specific_parser = argparse.ArgumentParser(prog="nginr init", description='Initialize a new nginr project')
            init_specific_parser.add_argument('project_name', help='The name of the new project directory to create')
            try:
                # We expect this to fail and print help for 'nginr init'
                init_specific_parser.parse_args(unknown_args if unknown_args else []) 
            except SystemExit:
                # Let argparse handle the exit after printing help
                raise 
            # Fallback if parse_args didn't exit (should not happen for missing required arg)
            init_specific_parser.print_help(sys.stderr)
            return 1
            
    elif args.file_or_command is not None and args.file_or_command.endswith('.xr'):
        # If project_name_arg is also present, it's an error with file execution
        if args.project_name_arg is not None:
            parser.error(f"Too many arguments when trying to run file: {args.file_or_command}. Did you mean 'nginr init {args.file_or_command}' if '{args.file_or_command}' was a project name?")
        run_file(args.file_or_command)
    else:
        # If file_or_command is something else, or None and no early exit from --help/--version
        # This will handle 'nginr' alone, or 'nginr some_unknown_command'
        # For 'nginr --help', argparse exits before this point.
        # For 'nginr init --help', we need a way to trigger its specific help.
        # A full solution for 'nginr init --help' requires true subparsers.
        # The current structure is a bit of a hybrid to keep 'nginr file.xr' simple.
        
        # Let's try to reconstruct for help if 'init' was intended but no project name
        # or if an unknown command was typed.
        # A more robust CLI might use a library like 'click' or structure argparse with true subparsers
        # for commands like 'init', and a default action for file paths.
        
        # For now, if it's not 'init' and not a .xr file, print general help.
        # If 'init' was typed but no project name, the block above handles it.
        if args.file_or_command is not None and args.file_or_command != 'init':
             print(f"Error: Unknown command or invalid file: {args.file_or_command}", file=sys.stderr)
        parser.print_help(sys.stderr)
        return 1
    return 0

if __name__ == '__main__':
    sys.exit(main())
