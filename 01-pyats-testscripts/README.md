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

## Running TestScripts and Jobfiles

### Standalone Execution

Standalone execution is only recommended for quick iteration when developing testscripts. The testscript file executes `aetest.main()` if you run the script directly.

Execute the script with the following command:
```
python basic_testscript.py
```

You'll notice all the test logs and results are printed directly to the terminal via standard output (stdout).

### Easypy Execution

The recommended execution method is using the Easypy runtime environment. The testscripts are executed as tasks in an Easypy Job. For this exercise, the testbed and datafile have already been provided as arguments to the `run()` in the jobfile, so no additional command line flags/options are needed when running the job.

To execute the Easypy jobfile, run the following command:
```
pyats run job basic_jobfile.py
```
