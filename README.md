# py-test

Messing around with Python

## Getting Started

- `git clone git@github.com:PhillipRC/py-test.git`
- `./install.sh`

## Commands
- Running Child_Parent_InFile script
  - `python ./src/Child_Parent_InFile.py`
- Running Child_Parent_InModule script
  - `python ./src/Child_Parent_InModule.py`
- Running py-test code
  - `python ./src/ParentChildSingleFile.py`
- Testing py-test
  - `pytest`
- Testing py-test with coverage
  - `pytest --cov`
- Testing py-test with coverage generating a HTML coverage report
  - `pytest --cov --cov-report=html`
  - `start ./coverage_html_report/index.html`

---

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