# import os
# import string 
# import random 
# import datetime
# import time

# # funkcja generująca logi połączenia SSH
# def generate_ssh_logs():
#   # tworzymy losowe dane połączenia
#   ip_address = '.'.join(str(i) for i in (random.randint(0, 255) for _ in range(4)))
#   username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
#   success = random.choices([True, False])[0]

#   # generujemy wpis logu
#   log_entry = f'{datetime.datetime.now()} - {ip_address} - {username} - {"SUCCESS" if success else "FAIL"}'

#   # zapisujemy wpis do pliku
#   with open('ssh_logs.txt', 'a') as log_file:
#     log_file.write(log_entry + '\n')

# # wywołujemy funkcję co jakiś czas
# while True:
#   generate_ssh_logs()
#   time.sleep(random.uniform(0, 1))
import re
ip_regex = r'\b(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])\.){3}(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])\b'
# otwieramy plik
min_bruteforce = 3
x = {}
reputation = {}

with open('/Users/patryk/Desktop/bf-projekt/plik.txt', 'r') as f:

    for line in f:
        x = re.findall(ip_regex,line)
        if x[0] not in reputation:
            if "SUCCESS" in line:
                reputation[x[0]] = 1
            else:
                reputation[x[0]] = -1
        else:
            if "SUCCESS" in line:
                reputation[x[0]] += 1
            else:
                reputation[x[0]] -= 1
    
for key,val in reputation.items():
    #print(f'{key}:{val}\n')
    if val <= -min_bruteforce:
        print(f'BRUTE FORCE ATTACK FORM {key}')
    

