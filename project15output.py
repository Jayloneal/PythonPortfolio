import socket

def check_site_connectivity(site):
    try:
        socket.create_connection((site, 80))
        return True
    except OSError:
        return False

# Check the connectivity of a few websites
sites = ["youtube.com", "myspace.com", "123movies.com"]
for site in sites:
    if check_site_connectivity(site):
        print(f"{site} is good to go, my boy! You good!")
    else:
        print(f"{site} is down right now, my boy! Check back lata!")
