import random
from pyats import aetest

# random.random() generates a float number between 0 and 1
parameters = {
    'number': random.random,
}

class Testcase(aetest.Testcase):

    @aetest.test
    def test(self, number):
        print(f"Random number object: {self.parameters['number']}") # still an object if viewed from self.parameters
         # <built-in method random of Random object at 0x91e2fc4
        print(f"Number value: {number}")  # the actual generated number
        # test whether the generated number is greater than 0.5
        assert number > 0.5

if __name__ == '__main__':
    aetest.main()