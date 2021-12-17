import sys
import socket
import os
def bunner():
    a = '''
        88                                88                              
        88                                88                              
        88                                88                              
        88,dPPYba,  ,adPPYYba,  ,adPPYba, 88   ,d8  ,adPPYba, 8b,dPPYba,  
        88P'    "8a ""     `Y8 a8"     "" 88 ,a8"  a8P_____88 88P'   "Y8  
        88       88 ,adPPPPP88 8b         8888[    8PP""""""" 88          
        88       88 88,    ,88 "8a,   ,aa 88`"Yba, "8b,   ,aa 88          
        88       88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a `"Ybbd8"' 88 ---(  m7  )

    '''
    print(a)
    print("-" * 80)
    print('                          by programmer & hacking (m7)')
    print("-" * 80)
bunner()

print("")
print("")

while True:
    try:

        site = input('[+] Entet your site name >> ')
        
        if site.lower() == 'exit' or site.lower() == 'stop':
            quit()
        
        def ip():
            while site :
                try:
                    ip = socket.gethostbyname(site)
                    print("THE YOUR IP >> " + ip)

                    break

                except ValueError:
                        print("sorry")
                else:
                    pass
        ip()

        def check_ping():
            hostname = site
            response = os.system("ping -a 1" + hostname)
                    
            if response == 0:
                pingstayus = "Network Active"
                print(pingstayus)
            else:
                pingstayus = "Network Erorr"
            return  pingstayus
        pingstayus = check_ping()

        
    except Exception:
        continue
