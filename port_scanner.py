import socket

# Dictionary of common ports and their services
ports_and_services = {
    20: 'ftp-data',
    21: 'ftp',
    22: 'ssh',
    23: 'telnet',
    25: 'smtp',
    53: 'dns',
    80: 'http',
    110: 'pop3',
    119: 'nntp',
    123: 'ntp',
    143: 'imap',
    161: 'snmp',
    194: 'irc',
    443: 'https',
    465: 'smtps',
    587: 'submission',
    631: 'ipp',
    993: 'imaps',
    995: 'pop3s',
    # Add more common ports and services here
}

def get_open_ports(target, port_range, verbose=False):
    open_ports = []
    start_port, end_port = port_range

    # Validate if the target is an IP address or a hostname
    try:
        ip = socket.gethostbyname(target)
    except socket.gaierror:
        if is_valid_ip(target):
            return "Error: Invalid IP address"
        else:
            return "Error: Invalid hostname"

    # Scan the ports
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            open_ports.append(port)
        sock.close()

    if verbose:
        if is_valid_ip(target):
            output = f"Open ports for {ip}"
        else:
            output = f"Open ports for {target} ({ip})"
        output += "\nPORT     SERVICE\n"
        for port in open_ports:
            service = ports_and_services.get(port, "unknown")
            output += f"{port:<9}{service}\n"
        return output.strip()

    return open_ports

def is_valid_ip(ip):
    parts = ip.split(".")
    if len(parts) != 4:
        return False
    for part in parts:
        try:
            if not 0 <= int(part) <= 255:
                return False
        except ValueError:
            return False
    return True
