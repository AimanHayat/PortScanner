from port_scanner import get_open_ports

# Test examples
print(get_open_ports("209.216.230.240", [440, 445]))
print(get_open_ports("www.stackoverflow.com", [79, 82]))
print(get_open_ports("www.google.com", [79, 82], verbose=True))
print(get_open_ports("256.256.256.256", [79, 82]))
print(get_open_ports("invalid_hostname", [79, 82]))
