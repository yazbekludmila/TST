from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

class Consulta_Conteudo():


    def __init__(self, app):
        self.app = app
    
    
    def consultar_conteudo(self):

         campo_pesquisar = self.app.find_element_by_xpath('//*[@id="content-id-name"]')
         campo_pesquisar.send_keys ('TESTE YAZBEK 02') 
        
         botão_lupa_consulta = self.app.find_element_by_xpath('//*[@id="for"]/div/div[1]/div[2]/span/button[1]').click()
         sleep(5)
    
    #def validar_consulta(self):
    #    valida_consulta = self.app.find_elements_by_link_text('link_text',"TESTE 01 YAZBEK 01")
    #    assert valida_consulta.text == 'TESTE 01 YAZBEK 01'    
        
        ##self.app.assert_element_displayed("link_text", "Meus endereços")               
    #    complemento_editar = self.app.find_element_by_id('complemento_endereco')
    #    print(complemento_editar.text)
        #assert complemento_editar.text == 'largo treze'
        #resultado = element_2
        #print(resultado.text)
        # print(total)
        
        #self.app.find(link_text='O endereço foi salvo.', timeout=4)
        #self.app.assert_element_displayed(('link_text', 'O endereço foi salvo.'))
        # alteracoes_ok = self.app.find_element_by_xpath('//*[@id="core_messages"]/ul/li/ul/li/span')
        #assert alteracoes_ok.text == 'O endereço foi salvo.'    

       