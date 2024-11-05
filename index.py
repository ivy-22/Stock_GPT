from wsgi import app 
import py_compile

# Path to your Python file
python_file = "./index.py"

# Compile the Python file to bytecode
py_compile.compile(python_file)
