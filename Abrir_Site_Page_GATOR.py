from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

from time import sleep as segundo
from Pyautomators.Verifica import Valida
from time import sleep

class Abrir_Site():

    def __init__(self, app):
        self.app = app
        #self.pagina('https://qa3.4yousee.com.br/')

    def abrir_home(self):
        self.app.get('https://financeiro.hostgator.com.br/')
        botao_entendi_cookies = self.app.find_element_by_xpath('//*[@id="cookie-cta"]').click()
       
    
    def valida_tela(self,imagem):
        tentativas = 50
        for tentativas in range(tentativas):
            if(self.app.verifica_tela(imagem, 80, similaridade=50) != None):
                break
            segundo(2)


    def valida_abertura(self):
        self.valida_tela(imagem=r'data\images\valida_login.png')
        self.app.clica_imagem(r'data\images\valida_login.png', similar = 70)

    def preencher_login(self,senha):
        self.app.escrever_direto('ltais')
        self.app.digitos('tab')
        sleep(5)
        self.app.escrever_direto(senha)
        segundo(5)
        self.app.digitos('enter')
        sleep(5)
        
        
        
        
        def selecionar_menu_promotor(self):
            self.app.clica_imagem(r'data\images\procuramenu.png', similar=70)
        self.app.escrever_direto('promotor')
        self.app.digitos('enter')      
        sleep(5)         
    ##duplo clique munu promotoress = abrir janela promotores
    def selecionar_menu01(self):
        self.app.clica_imagem(r'data\images\MENUPROMOTORESLCFO.png',similar=80, cliques =2 )
        sleep(5)  


    def pesquisar_todos_promotores_cadastrados(self, usertw, usercts):
        
        if(usertw == ' ' and usercts== '0'):   # pesquisa geral 
            self.app.clica_imagem(r'data\images\pesquisarpromotor.png',similar=80)
            sleep(5)   
            
        else:    ### faz pesqauisa de acordo com parametros passados 
            self.app.clica_imagem(r'data\images\usuariotw.png', similar=70)
            self.app.escrever_direto(usertw)
            self.app.digitos('tab')    
            self.app.escrever_direto(usercts)
            self.app.clica_imagem(r'data\images\pesquisarpromotor.png',similar=80)
            sleep(5)

        #self.app.combo_digitos('alt','f4')

        #self.app.clica_imagem(r'data\images\valida_acesso.png', similar=70)    

    