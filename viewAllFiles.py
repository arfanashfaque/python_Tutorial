from pathlib import Path
import glob
import os

path = Path()
for file in path.glob("*.py"): # here *.py, *.xls anything can be searched. one * means to read all directories and files
    print(file)