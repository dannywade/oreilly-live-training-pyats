from genie.harness.main import gRun
from pyats.datastructures.logic import And, Not, Or


def main():

    gRun(
        trigger_datafile="blitz.yml",
        trigger_uids = ["TestLoopbackInterface"],  # name of the tests you wish to run
        testbed="testbed.yml",
    )