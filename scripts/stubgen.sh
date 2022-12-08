#! /usr/bin/env bash

python -m venv stubgen_venv
source ./stubgen_venv/bin/activate
# TODO: version pin? both? set pyarrow version as script arg?
pip install mypy pyarrow

# Generate stubs
./stubgen_venv/bin/stubgen -p pyarrow -o pyarrow-stubs

deactivate
