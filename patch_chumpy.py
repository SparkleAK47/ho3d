#!/usr/bin/env python3
import os
import site
import sys

def patch_chumpy():
    paths = site.getsitepackages()
    for p in paths:
        init_file = os.path.join(p, 'chumpy', '__init__.py')
        if os.path.isfile(init_file):
            break
    else:
        print("chumpy not installed, please install first with pip install chumpy")
        sys.exit(1)

    with open(init_file, 'r') as f:
        content = f.read()

    # Replace import on line 11
    old_line = "from numpy import bool, int, float, complex, object, unicode, str, nan, inf"
    new_line = "import numpy as np; bool = np.bool_; int = np.int_; float = np.float_; complex = np.complex_; object = object; unicode = str; str = str; nan = np.nan; inf = np.inf"

    if old_line not in content:
        print("chumpy seems to have already been patched or is a different version, skipping.")
        return

    new_content = content.replace(old_line, new_line)
    with open(init_file, 'w') as f:
        f.write(new_content)

    print(f"chumpy patch applied: {init_file}")

if __name__ == "__main__":
    patch_chumpy()