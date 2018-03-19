import requests,os,sys
from bs4 import BeautifulSoup
from termcolor import colored,cprint
from threading import Thread as th

class HANDLER:
    def __init__(self,url):
        self.url = url
        self.listadork=[]
        self.listadork2=[]
        self.listadorks=[self.listadork,self.listadork2]
        self.listadorksvalidos=[]

    def read(self):
        tamanho=0
        i=0
        for x in open("dorks.txt",'r'):
            tamanho+=1
        for x in open("dorks.txt",'r'):
            if i<=(tamanho//2):
                self.listadork.append("/"+x.replace("\n",''))
                i+=1
            else:
                self.listadork2.append("/"+x.replace("\n",''))
                i+=1

    def crawler(self,lista):
        for x in lista:
            #if valida == 1:
            try:
            #if 1==1:
                if "http" not in self.url:
                    if "https" not in self.url:
                        self.url= "http://"+self.url
                url2 = self.url + x + "1'"
                page= requests.get(url2)
                contents=page.text
                print(url2)
                if 'deprecated' in contents  :
                    self.listadorksvalidos.append(x)
                    cprint("vulnerabilidade encontrada!",'red')
                elif 'You have an error in your SQL syntax' in contents:
                    self.listadorksvalidos.append(x)
                    cprint("vulnerabilidade encontrada!",'red')
                elif 'Query fail' in contents:
                    self.listadorksvalidos.append(x)
                    cprint("vulnerabilidade encontrada!",'red')
            except:
                    cprint("Ocorreu um erro (Time out talvez?)",'red')
                    continue
            #else:
            #    sys.exit(1)
        sys.exit(1)

    def pelica(self,url):
        if 'https' not in self.url:
            if 'http' not in self.url:
                while 1:
                    prefix=input("É http ou https?\n")
                    if prefix == "http":
                        prefix='http://'
                        self.url = prefix + self.url
                        break
                    elif prefix == "https":
                        prefix ='https://'
                        self.url = prefix + self.url
                        break
                    else:
                        cprint("Invalido!",'red')
        cprint(self.url,'magenta')
        page=requests.get(self.url+"'")
        contents=page.text
        if 'deprecated' in contents  :
            cprint("Vulneravel",'red')
        elif 'You have an error in your SQL syntax' in contents:
            cprint("Vulneravel",'red')
        elif 'Query fail' in contents:
            cprint("Vulneravel",'red')
        else:
            cprint("Não foi encontrada vulnerabilidade",'green')

    def subfinder(self):
        print("bom dia")
        #if 1==1:
        try:
            prefixo=""
            url = input("URL do website:\n")
            if "http" not in url:
                if "https" not in url:
                    antes = input("HTTP ou HTTPS?\n")
                    if antes == "https":
                        prefixo = 'https://'
                    elif antes == "http":
                        prefixo = 'http://'
            sufixo = '/'
            r = requests.get(prefixo + url + sufixo)
            data = r.text
            sopa = BeautifulSoup(data, "lxml")
            nome=url.split(".")
            nomecompleto = (nome[1]+".txt")
            for x in sopa.find_all('a'):
                print(x.get('href'))
                f = open(nomecompleto,"a")
                f.write("\n"+x.get('href'))
                f.close()
        except:
            cprint('Ocorreu um erro!\n','red')
