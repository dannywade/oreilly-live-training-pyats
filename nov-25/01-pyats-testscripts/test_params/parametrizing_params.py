import random
from pyats import aetest

# a parametrized function called ‘number’ that 
# accepts an upper and lower bound
# random.randint() is used to generate a random number within the bounds
@aetest.parameters.parametrize(lower_bound=1, upper_bound=100)
def number(lower_bound, upper_bound):
    return random.randint(lower_bound, upper_bound)

# accepts the current section as input, and
# returns 9999 when the section uid is 'expected_to_pass', or 0 otherwise.
@aetest.parameters.parametrize
def expectation(section):
    if section.uid == 'expected_to_pass':
        return 9999
    else:
        return 0

class Testcase(aetest.Testcase):

    # parametrized functions must be passed as function arguments to be evaluated
    # (just like callable parameters)

    # this section is expected to pass
    # the generated number is between 1 and 100, and the
    # expectation is 9999 (section uid is "expected_to_pass")
    @aetest.test
    def expected_to_pass(self, number, expectation):
        # test whether expectation is > than generated number
        assert expectation > number

    # this section is expected to fail
    # the generated number is still between 1 and 100, but the
    # expectation is 0 (section uid is not "expected_to_pass")
    @aetest.test
    def expected_to_fail(self, number, expectation):
        # test whether expectation is > than generated number
        assert expectation > number

