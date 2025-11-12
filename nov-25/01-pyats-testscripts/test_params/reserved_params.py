from pyats import aetest

# applicable to other TestContainer classes (Testcase and CommonCleanup) as well
class CommonSetup(aetest.CommonSetup):

    # access reserved parameters by providing their names as keyword arguments to methods
    @aetest.subsection
    def subsection_one(self, testscript, section, steps):
        # testscript object has an attribute called module which is this testscript's module
        print(testscript.module)
        # <module 'example_script' from '/path/to/example.py'>

        # current section object is Subsection and subsections have a unique uid
        print(section.uid)
        # subsection_one

        # steps object enables the usages of steps
        with steps.start('a new demo step'):
            pass
