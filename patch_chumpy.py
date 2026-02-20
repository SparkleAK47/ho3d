#!/usr/bin/env python3
import os
import site
import sys

def patch_chumpy():
    # 获取 chumpy 安装路径
    paths = site.getsitepackages()
    for p in paths:
        init_file = os.path.join(p, 'chumpy', '__init__.py')
        if os.path.isfile(init_file):
            break
    else:
        print("❌ chumpy 未安装，请先 pip install chumpy")
        sys.exit(1)

    with open(init_file, 'r') as f:
        content = f.read()

    # 替换第 11 行的 import
    old_line = "from numpy import bool, int, float, complex, object, unicode, str, nan, inf"
    new_line = "import numpy as np; bool = np.bool_; int = np.int_; float = np.float_; complex = np.complex_; object = object; unicode = str; str = str; nan = np.nan; inf = np.inf"

    if old_line not in content:
        print("⚠️  chumpy 似乎已经打过补丁或版本不同，跳过。")
        return

    new_content = content.replace(old_line, new_line)
    with open(init_file, 'w') as f:
        f.write(new_content)

    print(f"✅ chumpy 补丁已应用: {init_file}")

if __name__ == "__main__":
    patch_chumpy()