#!/usr/bin/bash
source /home/alexis/miniforge3/etc/profile.d/conda.sh
eval "$(conda shell.bash hook)"
conda activate iccd332
python main.py