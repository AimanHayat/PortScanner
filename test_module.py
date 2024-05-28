import unittest
from port_scanner import get_open_ports

class TestPortScanner(unittest.TestCase):
    def test_valid_ip(self):
        self.assertEqual(get_open_ports("209.216.230.240", [440, 445]), [443])

    def test_valid_hostname(self):
        result = get_open_ports("www.stackoverflow.com", [79, 82])
        self.assertIn(80, result)

    def test_verbose_output(self):
        result = get_open_ports("www.google.com", [79, 82], verbose=True)
        self.assertIn("Open ports for www.google.com", result)

    def test_invalid_ip(self):
        self.assertEqual(get_open_ports("256.256.256.256", [79, 82]), "Error: Invalid IP address")

    def test_invalid_hostname(self):
        self.assertEqual(get_open_ports("invalid_hostname", [79, 82]), "Error: Invalid hostname")

if __name__ == "__main__":
    unittest.main()
