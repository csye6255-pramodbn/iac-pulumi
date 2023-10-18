import requests

def get_my_ip():
    response = requests.get('https://httpbin.org/ip')
    return response.json()['origin']

# Get your IP address
my_ip = get_my_ip()

# Convert IP to CIDR notation
my_ip_cidr = f"{my_ip}/32"