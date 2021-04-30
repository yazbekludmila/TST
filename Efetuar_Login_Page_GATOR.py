from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

class Fazer_Login():

    def __init__(self, app):
        self.app = app
        
        ###JANELA COOKIES  ===botao aceitar 
        ##<a href="javascript:void(0)" id="cookie-cta" class="cookie-cta">entendi</a>


    def FAZER_LOGIN_USUARIO_EM_BRANCO(self):

        #DEIXAR EMAIL EM BRANCO CLICAR AVANCAR 
        campo_email = self.app.find_element_by_xpath('//*[@id="login"]/div[1]/input[1]')
        campo_email.clear()
                
        #campo_senha = self.app.find_element_by_id('pass')
        #campo_senha = self.app.find_element_by_xpath('//*[@id="nav-horizontal"]/div/div[2]/form/fieldset/div[2]/input')
        #campo_senha.send_keys('27vbqu')
        
        ### campo_nome_alterar.send_keys ('TESTE YAZBEK 01 ALTERADOOOOOOOOOO') 

        #CLICAR NO BOTÃO AVANCAR PARARA EFETUAR LOGIN == MENSAGEM 
        botao_avancar_login = self.app.find_element_by_xpath('//*[@id="login"]/div[2]/button').click()
        sleep(6)
        
        valida_msg_email_branco = self.app.find_elements_by_link_text('Preencha este campo.')
        assert valida_msg_email_branco.text == 'Preencha este campo.'
 #       login_valido = self.app.find_element_by_class_name('ellipsis-text')
        
        ##print(valida_msg_email_branco.text)
  #      assert  login_valido.text == 'Olá, Ludmila'    
        
        # botao_pesquisa.submit()   

        #  /html/body/div[6]/div[3]/div/button[2]
        ## <button type="button" class="btn-default">Fechar</button>

#def validar_login_efetuado(self):   
        #valido_login = self.app.find('link_text',"Olá, Ludmila")
        #element_2 = self.app.find_element_by_class_name('nm-searched-term')
 #       login_valido = self.app.find_element_by_class_name('ellipsis-text')
        #print(login_valido.text)
  #      assert  login_valido.text == 'Olá, Ludmila'    
        #resultado = element_2
        # print(resultado.text)
        # print(total)
        #assert resultado.text == 'Resultados para: Gestão da Emoção'