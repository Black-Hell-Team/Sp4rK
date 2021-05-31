try:

    import random
    import os
    import socket
    from time import sleep

    def clear():

        os.system('cls' if os.name == 'nt' else 'clear')

    def random_phrase():

        ppl = ["Jo Power Tech", "Sasaki", "sysb1n", "Gr3n0xX", "Quiliarca", "Lucazz Dev", "vl0ne-$", "Xernoboy", "marreta cabeça de rato", "S4SUK3"]

        phrase = ["was here", "is watching you", "knows your name", "knows your location", "hacked NASA", "hacked FBI", "hacked you", "is looking 4 u", "is right behind you", "has hype"]

        return random.choice(ppl) + " " + random.choice(phrase)

    def main():

        clear()
        print(f"""\033[1;101m\033[1;97m{random_phrase()}\033[0;0m
\033[1;92m
███████╗██████╗ ██╗  ██╗██████╗ ██╗  ██╗
██╔════╝██╔══██╗██║  ██║██╔══██╗██║ ██╔╝
███████╗██████╔╝███████║██████╔╝█████╔╝
╚════██║██╔═══╝ ╚════██║██╔══██╗██╔═██╗
███████║██║          ██║██║  ██║██║  ██╗
╚══════╝╚═╝          ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝

\033[1;92m[\033[1;95m01\033[1;92m]\033[1;95m CheckPort
\033[1;92m[\033[1;95m02\033[1;92m]\033[1;95m Portscan
\033[1;92m[\033[1;95m03\033[1;92m]\033[1;95m Back/Credits\n""")

        opc = input("\033[1;93m-\033[1;95mSp4rK\033[1;93m->\033[1;92m ")

        if opc == '1' or opc == '01':

            clear()
            cnx = socket.socket()
            print("\033[1;92mEnter an IP and a port to check if it is open or not\n")

            try:
                IP = input("\033[1;93m-\033[1;95mIP\033[1;93m->\033[1;92m ")
                PORT = int(input("\033[1;93m-\033[1;95mPORT\033[1;93m->\033[1;92m "))
                time = 0.2
                cnx.settimeout(time)
                n = cnx.connect_ex((IP,PORT))

                if n == 0:

                    print("\n\033[1;92mOpen door !!\n")

                else:

                    print("\n\033[1;91mClosed door\n")

            except Exception as erro:
                print('\n\033[1;91mOps!!!\n')

            print("\033[1;92m1 \033[1;93m-> \033[1;92mBack to menu\n\033[1;92m2 \033[1;93m-> \033[1;92mTo go out\n")
            opt = input("\033[1;96m>\033[1;95m>\033[1;93m>\033[1;97m ")

            if opt == '01' or opt == '1':

                main()

            else:

                clear()
                print(f"\033[1;101m\033[1;97m{random_phrase()}\033[0;0m\n")
                exit()

        elif opc == '02' or opc == '2':

            clear()
            print("\033[1;92mEnter an IP to perform a simple PORTSCAN, be calm as it may take a while\n")

            try:
                ip = input("\033[1;93m-\033[1;95mIP\033[1;93m->\033[1;92m ")

                ports = {
                        21: 'ftp',
                        22: 'ssh',
                        23: 'telnet',
                        25: 'smtp',
                        53: 'domain',
                        80: 'http',
                        110: 'pop3',
                        111: 'rpcbind',
                        135: 'RPC',
                        139: 'netbios',
                        143: 'imap',
                        443: 'https',
                        445: 'microsoft-ds',
                        993: 'imaps',
                        995: 'pop3s',
                        1723: 'pptp',
                        3306: 'mysql',
                        3389: 'RDP',
                        5900: 'vnc',
                        8080: 'http-proxy'
                }

                for key, value in ports.items():

                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.settimeout(0.2)
                    code = s.connect_ex((ip, key))
                    if code == 0:

                        print(f"\n\033[1;92mPort: \033[1;101m\033[1;97m{key} {value} \033[0;0m\033[1;92m-> OPEN")

            except Exception as erro:
                print('\n\033[1;91mOps!!!')

            print("\n\033[1;92m1 \033[1;93m-> \033[1;92mBack to menu\n\033[1;92m2 \033[1;93m-> \033[1;92mTo go out\n")
            opt = input("\033[1;96m>\033[1;95m>\033[1;93m>\033[1;97m ")

            if opt == '01' or opt == '1':

                main()

            else:

                clear()
                print(f"\033[1;101m\033[1;97m{random_phrase()}\033[0;0m\n")
                exit()

        elif opc == '03' or opc == '3':

            clear()
            print(f"""\033[1;101m\033[1;97m{random_phrase()}\033[0;0m

\033[1;101m\033[1;97m[•] Coded by: Jo Power Tech
[•] Github ORG: https://github.com/Black-Hell-Team
[•] Black Hell Team\n\033[0;0m""")

        else:

            clear()
            print("\033[1;91mInvalid option")
            sleep(2)
            main()

    main()

except KeyboardInterrupt:
    print('\n\033[1;91mCRTL + C = Bye Bye\n')
