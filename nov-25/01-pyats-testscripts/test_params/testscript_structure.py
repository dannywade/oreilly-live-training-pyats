import argparse
from pyats import aetest
from pprint import pprint

class ScriptCommonSetup(aetest.CommonSetup):

    @aetest.subsection
    def common_setup_subsection(self):
        pass

# setup/test/cleanup sections within Testcases
class Testcase(aetest.Testcase):

    @aetest.setup
    def testcase_setup(self):
        pass

    @aetest.test
    def test_one(self):
        pprint(self.parameters)
        pass

    @aetest.cleanup
    def testcase_cleanup(self):
        pass

class ScriptCommonCleanup(aetest.CommonCleanup):

    @aetest.subsection
    def common_cleanup_subsection(self):
        pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--device_id', help="Provide specific device ID") # Device ID from other mgmt system
    parser.add_argument("--offline", action=argparse.BooleanOptionalAction) # Flag for offline testing
    args, unknown = parser.parse_known_args()
    if args.device_id:
        aetest.main(device_id=args.device_id, offline=args.offline)
    else:
        aetest.main()