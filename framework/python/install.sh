#!/bin/sh

USE_VENV=0

for arg in "$@"
do
    case $arg in
        --use-venv)
        USE_VENV=1
        shift
        ;;
    esac
done

if [ "$USE_VENV" -eq 1 ]; then
    python -m venv .venv
    . .venv/bin/activate
fi

pip install build
python -m build --outdir dist .
pip install dist/web_oto_dev_sdk-1.0.15-py3-none-any.whl --force-reinstall

if [ "$USE_VENV" -eq 1 ]; then
    deactivate
fi