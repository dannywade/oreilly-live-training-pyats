from pyats import aetest

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
        pass

    @aetest.cleanup
    def testcase_cleanup(self):
        pass

class ScriptCommonCleanup(aetest.CommonCleanup):

    @aetest.subsection
    def common_cleanup_subsection(self):
        pass