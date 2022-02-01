import json, re

def isvalid(ip):
    if [ int(i) >= 0 and int(i) <=255 for i in ip.split(".") ].count(True) == 4:
        return True
    else:
        return False

def ip_validate(file_name):
    with open(file_name) as f:
        data = json.load(f)
    
    for ip in data['ipaddr']:
        try:
            ip_address = re.search("[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}", ip).group()
            if isvalid(ip_address):
                if ip_address.startswith('192') or ip_address.startswith('172') or ip_address.startswith('10'):
                    print(f"{ip_address} is a reserved ip address")
                else:
                    print(f"{ip_address} is a valid ip address")
            else:
                print(f"{ip} is not a valid ip address, i.e range not between 0-255")
        except:
            print(f"{ip} is not a valid ip address")
ip_validate('source.json')