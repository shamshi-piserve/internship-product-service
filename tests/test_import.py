import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import ProductDB

def test_import():
    assert ProductDB is not None