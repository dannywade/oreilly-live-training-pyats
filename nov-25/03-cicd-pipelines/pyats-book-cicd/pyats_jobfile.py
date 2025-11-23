from genie.harness.main import gRun


def main():
    gRun(
        trigger_datafile="net_testing/blitz.yaml",
        trigger_uids=["BgpTestcase"],
        testbed="net_testing/testbed.yaml",
    )


# To run job: pyats run job pyats_jobfile.py --health-checks cpu memory logging core --html-logs pyats_html_logs --archive-dir pyats_archive_logs
