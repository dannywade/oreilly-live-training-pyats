from dotenv import load_dotenv
from pyats.topology import loader
from pyats.easypy import run

def main(runtime):
    # Load environment variables
    load_dotenv()
    
    # Load the testbed file
    tb = loader.load("testbed.yml")
    
    # Set job name
    runtime.job.name = "OReilly-Live-Training"

    # Run the test script with the loaded testbed
    run(testscript="basic_testscript.py", runtime=runtime, testbed=tb, datafile="datafile.yml")

    # To run job:
    # pyats run job basic_jobfile.py