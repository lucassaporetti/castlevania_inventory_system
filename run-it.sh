#!/usr/bin/env bash

CUR_DIR="$(pwd)"

export PYTHONPATH="${CUR_DIR}"

pushd src &> /dev/null || exit 1
if pyrcc5 resources.qrc -o resources_rc.py; then
  python3 main.py qt
fi
popd &> /dev/null || exit 1

exit 0
