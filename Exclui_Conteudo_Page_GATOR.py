from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
 
class Exclui_Conteudo():


    def __init__(self, app):
        self.app = app
     
    def excluir_conteudo(self):
      ## botao_lixeira 
         botao_lixeira  = self.app.find_element_by_xpath('//*[@id="managerContent"]/table/tbody/tr/td[2]/table[2]/tbody/tr[3]/td/div/table/tbody/tr[2]/td[5]/ul/li[2]/a/i').click()
         sleep(6)   
         #botao_ok_janela_confirmar = self.app.find_elements_by_link_text('ATENÇÃO! Confirma a exclusão?').click()
         
         #botao_ok_janela_confirmar = self.app.find_element_by_xpath('//*[@id="managerContent"]/table/tbody/tr/td[2]/table[1]/tbody').click()
                 
         ####### MSG CONFIRMAÇÃO EXCLUSÃO 
         msg0_valida_exclusao = self.app.find_element_by_xpath('//*[@id="managerContent"]/table/tbody/tr/td[2]/table[2]/tbody/tr[3]/td/div[1]')
         assert msg_valida_exclusao.text == 'Registro excluído com sucesso' 
        
         sleep (6)         

    
     