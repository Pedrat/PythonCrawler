import shutil,os,crawler2,sys
from crawler2 import HANDLER
from termcolor import colored,cprint
urlusar=0
obj=[]
listaurl=[]
os.system("clear")
url=input(colored('Qual é o url?','red'))
if "http" not in url:
    if 'https' not in url:
        while 1:
            prefixo=input("HTTP ou HTTPS?")
            if prefixo.lower() == "http":
                url="http://"+url
                break
            if prefixo.lower() == "https":
                url = "https://"+url
                break
            else:
                continue
obj.append(HANDLER(url))
listaurl.append(url)
obj[urlusar].read()
while 1:
    columns = shutil.get_terminal_size().columns
    lines = shutil.get_terminal_size().lines
    os.system("clear")
    calma=''
    menu=['1-Crawler', '2-Pelica', '3-Google Dork Search', '4- Crawler pelo ficheiro',"5-Directory Finder",'6-Adicionar URL', 'Escreva sair', 'Opção:']
    lines= (lines//2)-(len(menu)//2)
    print("\n"*lines)
    print("URL a usar: ",listaurl[urlusar])
    for x in menu:
        print(colored(x,'red').center(columns))
    opc=input()
    if opc == "1":
        print("WIP")
    elif opc == "2":
        print("WIP")
    elif opc == "3":
        print("WIP")
    elif opc == "4":
        print("WIP")
    elif opc == "5":
        print("WIP")
    elif opc == "6":
        url = input(colored("Qual é o url?",'red'))
        if "http" not in url:
            if 'https' not in url:
                while 1:
                    prefixo=input("HTTP ou HTTPS?")
                    if prefixo.lower() == "http":
                        url="http://"+url
                        break
                    if prefixo.lower() == "https":
                        url = "https://"+url
                        break
                    else:
                        continue
        listaurl.append(url)
        obj.append(HANDLER(url))
        obj[len(obj)-1].read()
    elif opc == "7":
        os.system("clear")
        i=1
        print("\n"*lines)
        for x in listaurl:
            print(colored((str(i)+" "+x).center(columns),'magenta'))
            i+=1
        urlusar=int(input("Qual é o id do url?"))-1

    elif opc == "sair":
        sys.exit(1)
    else:
        continue
