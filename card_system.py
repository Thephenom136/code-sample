import sys

def add(line1):
    add_lines = line1.split()
    
    if(luhn_check(add_lines[2])):
        clients_limits.update({add_lines[1]:int(add_lines[3][1:])})
        clients_accounts.update({add_lines[1]:0})
    else:
        clients_limits.update({add_lines[1]:"error"})
        clients_accounts.update({add_lines[1]:"error"})

def charge(line2):
    charge_lines = line2.split()
    charge_lines[2] = int(charge_lines[2][1:])
    if(clients_limits[charge_lines[1]] == "error"):
        clients_accounts[charge_lines[1]] = "error"
    elif (charge_lines[2] + int(clients_accounts[charge_lines[1]]) > clients_limits[charge_lines[1]]):
        pass
    else:
        clients_accounts[charge_lines[1]] += int(charge_lines[2])

def credit(line3):
    credit_lines = line3.split()
    credit_lines[2] = int(credit_lines[2][1:])
    if(clients_limits[credit_lines[1]] == "error"):
        clients_accounts[credit_lines[1]] = "error"
    else:
        clients_accounts[credit_lines[1]] -= credit_lines[2]

def luhn_check(card_num):
    c = card_num
    aux = {5:1,6:3,7:5,8:7,9:9}
    checksum = int(c[-1:-2:-1])
    c = c[-2::-1]
    band = 0
    tot = 0
    for e in c:
        e = int(e)
        if band == 0:
            e = aux[e] if e*2 >= 10 else e*2
        tot += e
        band = abs(band-1)
    tot = 10 - (tot % 10)
    return True if tot == checksum else False


clients_limits = {}
clients_accounts = {}
if len(sys.argv) == 2:
    if ".txt" in sys.argv[1]:
        with open(sys.argv[1],'r') as i:
            lines = i.readlines()
    elif "Add" in sys.argv[1]:
        lines = sys.stdin.readlines()
    else:
        lines = []

elif len(sys.argv) == 3:
    if ".txt" in sys.argv[2]:
        with open(sys.argv[2],'r') as i:
            lines = i.readlines()
else:
    print("No vaild input")
      
for e in lines:
    if "Add" in e:
        res = add(e)
    elif "Charge" in e:
        resu = charge(e)
    elif "Credit" in e:
        resul = credit(e)
i = list(clients_accounts.items())
i.sort()
for e in i:
    print("{0}: ${1}".format(e[0],e[1]) if e[1]!="error" else "{0}: {1}".format(e[0],e[1]))