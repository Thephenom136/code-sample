import sys

#Add Tom Home 4111111111111111 $1000
def add(line1):
    add_lines = line1.split()
    client_name = add_lines[1]
    client_limit = add_lines[4][1:]

    name = client_name + "_" + add_lines[2]
    
    if(luhn_check(add_lines[3])):
        clients_limits.update({name:int(client_limit)})
        clients_accounts.update({name:0})
    else:
        clients_limits.update({name:"error"})
        clients_accounts.update({name:"error"})


#Charge Tom Home $500
def charge(line2):
    charge_lines = line2.split()
    client_name = charge_lines[1] +"_"+charge_lines[2]
    client_amount = int(charge_lines[3][1:])

    if(clients_limits[client_name] == "error"):
        clients_accounts[client_name] = "error"
    elif (client_amount + int(clients_accounts[client_name]) > clients_limits[client_name]):
        pass
    else:
        clients_accounts[client_name] += int(client_amount)

#Credit Lisa Platinum $100
def credit(line3):
    credit_lines = line3.split()
    client_name = credit_lines[1]+"_"+credit_lines[2]
    client_amount = int(credit_lines[3][1:])

    if(clients_limits[client_name] == "error"):
        clients_accounts[client_name] = "error"
    else:
        clients_accounts[client_name] -= client_amount

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
    return tot == checksum


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
    lines = []
    opt = ""
    while(opt != "5"):
        print("Choose one option")
        print("1: Add a new user")
        print("2: Make a charge to a user")
        print("3: Add credit to a user")
        print("4: Print current accounts")
        print("5: Exit")
        opt = input()
        if opt == "1":
            print("Type the user to add")
            inp = input()
            add(inp)
        if opt == "2":
            print("Type the charge")
            inp = input()
            charge(inp)
        if opt == "3":
            print("Type the credit to add")
            inp = input()
            credit(inp)
        if opt == "4":
            print(clients_accounts)
      
for e in lines:
    if "Add" in e:
        res = add(e)
    elif "Charge" in e:
        resu = charge(e)
    elif "Credit" in e:
        resul = credit(e)
name_type_list = list(clients_accounts.items())
name_type_list.sort()

clients_names = []
final_list = []
for c in name_type_list:
    client_name = c[0].split("_")[0]
    if client_name not in clients_names:
        clients_names.append(client_name)
        print(clients_names)
        client_list_account = []
        for cl in name_type_list:
            print(client_name in cl[0])
            if client_name in cl[0]:
                client_list_account.append((cl[0].split("_")[1],cl[1]))
        final_list.append((client_name,client_list_account))


final_client = ""
for client in final_list:
    final_client = client[0]+": "
    for account in client[1]:
        if account[1] == "error":
            final_client = final_client + "("+account[0]+") error,"
        else:
            final_client = final_client+"("+account[0]+") $"+str(account[1])+","
    final_client = final_client[:-1]
    print(final_client)
#Lisa: (Gold) error, (Platinum) $-100, (Work) $7
#for e in i:
#    print("{0}: ${1}".format(e[0],e[1]) if e[1]!="error" else "{0}: {1}".format(e[0],e[1]))