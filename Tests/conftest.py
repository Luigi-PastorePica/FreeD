# python
# file: Tests/conftest.py
import os
import sys

TESTS_DIR = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(os.path.join(TESTS_DIR, ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)