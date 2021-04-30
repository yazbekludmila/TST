from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

class Altera_Conteudo():


    def __init__(self, app):
        self.app = app
    
    def alterar_conteudo(self):
         simbolo_lapis = self.app.find_element_by_xpath('//*[@id="managerContent"]/table/tbody/tr/td[2]/table[2]/tbody/tr[3]/td/div/table/tbody/tr[2]/td[5]/ul/li[1]/a/i').click()
         campo_nome_alterar = self.app.find_element_by_xpath('//*[@id="litdescricaoIns"]')
         campo_nome_alterar.clear()
         campo_nome_alterar.send_keys ('TESTE YAZBEK 01 ALTERADOOOOOOOOOO') 
         botão_alterar = self.app.find_element_by_xpath('//*[@id="tabs"]/div[3]/input[1]').click()
         sleep(6)
     
         msg_valida_alteracao = self.app.find_element_by_xpath('//*[@id="managerContent"]/table/tbody/tr/td[2]/table[2]/tbody/tr[3]/td/div[1]')
         assert msg_valida_alteracao.text == 'Registro alterado com sucesso.' 
     