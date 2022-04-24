# py-test

Messing around with Python

## Getting Started

- git clone git@github.com:PhillipRC/py-test.git
- ./install.sh
- python ./src/MyApp.py

# Handy Commands

## Run a Python script on the command line
`python -c "import os; import sys; print(os.path.dirname(sys.executable))"`

## Find where Python executable folder
- Windows: `where.exe python.exe`
- Unix: `which python.exe`

## Windows: Run PowerShell command as an Administrator
`Start-Process -Verb RunAs powershell.exe -Args "-executionpolicy bypass -command dir"`

### Allow running locally written PowerShell scripts
`Start-Process -Verb RunAs powershell.exe -Args "-executionpolicy bypass -command Set-ExecutionPolicy RemoteSigned"`