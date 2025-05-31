# test/conftest.py

import sys
import os

# Agrega la ruta absoluta de la carpeta 'app' al sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))
