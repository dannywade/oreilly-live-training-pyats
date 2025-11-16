from genie.harness.main import gRun
from pyats.datastructures.logic import And, Not, Or


def main():

    gRun(
        trigger_datafile="blitz.yml",
        trigger_uids = ["TestLoopbackInterface"],  # name of the tests you wish to run
        testbed="testbed.yml",
    )


# Run Easypy job with health checks
# pyats run job easypy_grun.py --health-checks cpu memory logging core --health-threshold cpu:75 memory:8