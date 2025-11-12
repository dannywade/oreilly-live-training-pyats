from pyats import aetest

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
        # access & print all known parameters
        print(self.parameters)
        # {'new_parameter_from_setup': 'new value',
        #  'generic_param_A': 200,
        #  'testscript_param_B': [],
        #  'testscript_param_A': 'some value'}