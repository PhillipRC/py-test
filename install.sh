#!/bin/bash

echo " 🧹 delete ./venv "
rm -rfd ./venv

echo " 🐍 setup ./venv "
python -m venv .venv

echo " 🐍 activate virutal envrionment "
. ./.venv/Scripts/activate

echo " 🐍 install requirements "
pip install -r requirements.txt

echo " 🏁 done "