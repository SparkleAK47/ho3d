#!/bin/bash
set -e

ENV_NAME="ho3d"

# 1. 创建/更新 conda 环境（宽松版本）
if ! conda env list | grep -q "^$ENV_NAME "; then
    echo "🔄 创建环境 $ENV_NAME ..."
    conda env create -f environment.yml
else
    echo "🔄 更新环境 $ENV_NAME ..."
    conda env update -f environment.yml
fi

# 2. 激活环境
eval "$(conda shell.bash hook)"
conda activate $ENV_NAME

# 3. 修补 chumpy
python patch_chumpy.py

echo "🎉 环境准备完毕！现在可以运行 HO-3D 脚本了。"
echo "   conda activate $ENV_NAME"