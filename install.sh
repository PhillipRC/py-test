#!/bin/bash

echo " ๐งน delete ./venv "
rm -rfd ./venv

echo " ๐ setup ./venv "
python -m venv .venv

echo " ๐ activate virutal envrionment "
. ./.venv/Scripts/activate

echo " ๐ install requirements "
pip install -r requirements.txt

echo " ๐ done "