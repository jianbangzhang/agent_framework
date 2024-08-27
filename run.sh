#!/bin/bash

PYTHON_SCRIPT="app/app.py"

python $PYTHON_SCRIPT

if [ $? -eq 0 ]; then
    echo "Script executed successfully"
else
    echo "Script failed to execute"
fi
