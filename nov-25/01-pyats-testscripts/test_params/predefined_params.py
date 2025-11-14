from pyats import aetest
from pprint import pprint

# testscript level default parameters
parameters = {
    'testscript_param_A': 'some value',
    'testscript_param_B': [],
    'generic_param_A': 100
}

class Testcase(aetest.Testcase):
    # testcase level default parameters
    parameters = {
        'generic_param_A': 200
    }

    # here we'll do a combination access & updating of parameters
    @aetest.setup
    def setup(self):
        # add to the parameters dict
        self.parameters['new_parameter_from_setup'] = 'new value'

    @aetest.test
    def test(self):
        # Print all known parameters
        print("All known parameters at testcase level:")
        pprint(self.parameters)
        # Print parent (testscript) parameters
        print("Testscript level parameters:")
        pprint(self.parent.parameters)
        
        print(f"generic_param_A at testscript-level: {self.parent.parameters["generic_param_A"]}")  # from testscript level
        print(f"generic_param_A at testcase-level: {self.parameters["generic_param_A"]}")     # overridden at testcase level

if __name__ == '__main__':
    aetest.main()