#!/bin/bash

# exit if any command fails
set -eux pipefail

pip install -t lib -r requirements.txt
(cd lib; zip ../lambda_function.zip -r .)
zip lambda_function.zip -u botay.py

# Clean up
rm -rf lib