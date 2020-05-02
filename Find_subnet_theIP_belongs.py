
def get_ip_and_submask(subnet):
    ip_add = subnet.split("/")[0]
    subn_mask = subnet.split("/")[1]
    return ip_add, subn_mask

def get_portions(ip):
    first_three_byte = ip.split(".")[0:3]
    last_byte = ip.split(".")[-1]
    return first_three_byte, last_byte

def host_range(first_host, s_mask):
    n = 32 - int(s_mask)
    usable_hosts = 2**n - 2
    last_host = int(get_portions(first_host)[1]) + int(usable_hosts)
    return last_host

ranges = list()
names = list()

def within_range_or_not(user_ip_add, ip_range_lines):
  for rang in ip_range_lines:
      rang = rang.strip().split(":")
      rang = {'device_type': rang[0],
             'ip': rang[1]
            }
      ranges.append(rang["ip"])
      names.append(rang["device_type"])

  for address in ranges:
      Q = get_ip_and_submask(address)[0]
      P = get_ip_and_submask(address)[1]
      if list(map(int,get_portions(user_ip_add)[0])) == list(map(int, get_portions(Q)[0])):
        if get_portions(user_ip_add)[1] >= get_portions(Q)[1] and str(get_portions(user_ip_add)[1]) < str(host_range(Q, P)):
          nth_element = ranges.index(address)
          return "The IP address belongs to " + names[nth_element] + " subnet"
      return "Unfortunately, the IP address does not depent on any subnet"


IP = input("Please type in your IP address: ")

'''
with open("/Users/User/Desktop/ip_ranges.txt") as ip_ranges:
    	    ip_range_lines = ip_ranges.readlines()'''

ip_range_lines=["Office-1 LAN: 78.100.1.1/24", "Office-2 LAN: 78.100.2.1/24", "Office-3 LAN: 78.100.3.1/24", "Office Wireless: 78.100.1.33/27", "Store-1 net: 78.100.2.49/28", "Home net: 172.16.16.1/30", "Test-1: 192.168.1.1/32", "Test-2: 192.168.1.1/24"]

result = within_range_or_not(IP, ip_range_lines)
print(result)
