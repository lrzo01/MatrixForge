import sys
import os

src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "src"))
sys.path.insert(0, src_path)

from matrix_forge.app import main

if __name__ == "__main__":
    main()
