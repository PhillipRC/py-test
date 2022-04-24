# py-test

Messing around with Python testing
- [pytest](https://pypi.org/project/pytest/)
- Mocking a modules used as a Parent class 

## Getting Started

- `git clone git@github.com:PhillipRC/py-test.git`
- `./install.sh`

## Commands
- Running Child_Parent_InFile script
  - `python ./src/Child_Parent_InFile.py`
- Running Child_Parent_InModule script
  - `python ./src/Child_Parent_InModule.py`
- Running Tests
  - PyTest with Verbose
    - `pytest -v`
  - PyTest with Coverage ouput to Console
    - `pytest -v --cov`
  - PyTest with Coverage output as HTML
    - `pytest -v --cov --cov-report=html`
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