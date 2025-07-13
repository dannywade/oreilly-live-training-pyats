from pyats import aetest
import logging

logger = logging.getLogger(__name__)
logger.setLevel("INFO")

class CommonSetup(aetest.CommonSetup):
    @aetest.subsection
    def connect_to_devices(self, testbed):
        """Connect to all testbed devices"""
        try:
            testbed.connect(learn_hostname=True, init_config_commands=[], init_exec_commands=[])
        except ConnectionError:
            self.failed(f"Could not connect to all devices in {testbed.name}")
        # Print log message confirming all devices are in a 'connected' state
        logger.info(f"Connected to all devices in {testbed.name}")


class BasicTestcase(aetest.Testcase):

    @aetest.test
    def check_device_os_version(self, testbed, expected_os_version):
        """Check OS version of each device"""
        # Iterate through devices in the testbed
        for device_name, device in testbed.devices.items():
            # Check if the device has an OS version attribute
            # Parse the device's OS version
            os_version = device.parse("show version")["version"]["version"]
            if os_version == expected_os_version:
                self.passed(f"{device_name} is running the expected OS version: {os_version}")
            else:
                self.failed(f"{device_name} is running an unexpected OS version: {os_version}. Expected: {expected_os_version}")

    @aetest.test
    def check_routes(self, testbed, expected_routes):
        """Check routing tables for specific routes"""
        # Parse routing table on R1
        # r1_routes = testbed.devices["R1"].parse("show ip route")

        for device_name, device in testbed.devices.items():
            routes = device.parse("show ip route")
            # Check for list of specific routes in the routing table
            for route in expected_routes:
                if route not in routes["vrf"]["default"]["address_family"]["ipv4"]["routes"]:
                    self.failed(f"Route {route} not found in {device_name}'s routing table.")
            
            # If all expected routes are found, pass the test
            self.passed(f"All expected routes were found in {device_name}'s routing table.")

    @aetest.test
    def check_interface_status(self, testbed):
        """Check interface status on R1 to ensure they are up or administratively down"""
    
        for device_name, device in testbed.devices.items():
            interfaces = device.parse("show ip interface brief")
            status_list = Dq(interfaces).get_values("status")
            
            # Check if all interfaces are up or in an administratively down state
            if all(status in ["up", "administratively down"] for status in status_list):
                self.passed(f"All interfaces on {device_name} are either up or administratively down.")
            else:
                self.failed(f"Some interfaces on {device_name} are neither up nor administratively down.")


class CommonCleanup(aetest.CommonCleanup):
    @aetest.subsection
    def disconnect_from_devices(self, testbed):
        """Disconnect from all devices"""
        testbed.disconnect()
        logger.info(f"Disconnected from all devices in {testbed.name}")

if __name__ == "__main__":
    from pyats.topology import loader
    from dotenv import load_dotenv
    from genie.utils import Dq

    # Load environment variables
    load_dotenv()

    # Load the testbed file
    tb = loader.load("testbed.yml")

    # and pass all arguments to aetest.main() as kwargs
    aetest.main(testbed=tb, datafile="datafile.yml")

    # To run standalone execution:
    # python bgp_testscript.py