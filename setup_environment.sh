#!/bin/bash
set -e

ENV_NAME="ho3d"

# Create/Update conda environment
if ! conda env list | grep -q "^$ENV_NAME "; then
    echo "Create an environment $ENV_NAME ..."
    conda env create -f environment.yml
else
    echo "Update an environment $ENV_NAME ..."
    conda env update -f environment.yml
fi

eval "$(conda shell.bash hook)"
conda activate $ENV_NAME

# Patch chumpy
python patch_chumpy.py

echo "   conda activate $ENV_NAME"