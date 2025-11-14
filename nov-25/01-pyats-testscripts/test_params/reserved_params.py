from pyats import aetest

# applicable to other TestContainer classes (Testcase and CommonCleanup) as well
class CommonSetup(aetest.CommonSetup):

    # access reserved parameters by providing their names as keyword arguments to methods
    @aetest.subsection
    def subsection_one(self, testscript, section, steps):
        # testscript object has an attribute called module which is this testscript's module
        print(f"Testscript module: {testscript.module}")
        # <module 'example_script' from '/path/to/example.py'>

        # current section object is Subsection and subsections have a unique uid
        print(f"Section UID: {section.uid}")
        # subsection_one

    @aetest.subsection
    def subsection_two(self, section, steps):
        print(f"Section UID: {section.uid}")
        # subsection_one

        # steps object enables the usages of steps
        with steps.start('a new demo step') as step:
            print(f"Step UID: {step.uid}")
            # STEP 1
            with step.start('a nested demo step') as nested_step:
                print(f"Nested Step UID: {nested_step.uid}")
                # STEP 1.1

if __name__ == '__main__':
    aetest.main()