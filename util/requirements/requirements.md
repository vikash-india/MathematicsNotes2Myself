# Description: Python Environment for the Project

### Python Virtual Environment
* Create virtual environment `MathematicsNotes2Myself` for this project.
* MathematicsNotes2Myself is a Python 3 virtual environment.
```
mkvirtualenv --no-site-packages MathematicsNotes2Myself
```

### Python Packages
* This is a list of Python modules needed for this project.
* The `requirements.txt` contains the complete list including the dependencies.
```
pip install matplotlib          # For visualisations
pip install sympy               # For algebra
```

### Python Requirement File
```
# Generate Requirements File
workon MathematicsNotes2Myself
pip freeze > requirements.txt

# Install From Requirements File
workon MathematicsNotes2Myself
pip install -r requirements.txt
```

### TODO
* None

