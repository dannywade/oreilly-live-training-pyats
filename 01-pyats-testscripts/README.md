# Installation

## Pre-requisites

- Python 3.8+
- Mac/Linux or WSL for Windows


## Installing pyATS and the pyATS Library (Genie)

1. Create and activate a Python virtual environment
```
python -m venv venv
source venv/bin/activate
```

2. Install the pyATS and pyATS Library (Genie) Python packages
```
pip install pyats[library]
```

*Note: Depending on the OS shell/terminal, you may need to include quotation marks around the package name due to the square brackets being treated as special characters: ```pip install "pyats[library]"```*