from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

class Inclui_Conteudo():


    def __init__(self, app):
        self.app = app
    
    
    def incluir_conteudo(self):
         
         ## botao_adicionar 
         botao_adicionar = self.app.find_element_by_xpath('//*[@id="add-content-link"]').click()
         sleep(3) 

         ##campo_nome_incluir 
         campo_nome_incluir = self.app.find_element_by_xpath('//*[@id="descricaoIns"]')
         campo_nome_incluir.send_keys ('TESTE YAZBEK INCLUSAOOOOOOOOOOO nova') 
         sleep(4) 

         # botao_selecionar_arquivo 
         # botao_selecionar_arquivo = self.app.find_element_by_xpath('//*[@id="aba-1"]/div/div/div[3]/div/button').click()
         ##sleep(6) 

         ## nome_arquivo_selecionado
         #nome_arquivo_selecionado = self.app.find_element_by_xpath('//*[@id="aba-1"]/div/div/div[4]/div/div[1]/div/table/tbody/tr/td[2]')
         #sleep(4)

         #nome_arquivo_selecionado.send_keys ('	Passe_Virtual___Instituto_Andr_Luiz.mp3')
         #sleep(4)

         # checkbox lado nome arquivo 
         checkbox_arquivo_selecionado = self.app.find_element_by_xpath('//*[@id="aba-1"]/div/div/div[4]/div/div[1]/div/table/tbody/tr/td[1]/span/input[1]').click()
         sleep(4)

         # botao_categorias selecionar 
         botao_categorias = self.app.find_element_by_xpath('//*[@id="open-category-dialog-button"]').click()
         sleep(5)

         # categoria 1 
         selecao_categoria1 = self.app.find_element_by_xpath('//*[@id="categories-dialog"]/div/div[1]/div/div[3]/dynatree/ul/li[1]/span/span[2]').click()
         sleep(5) 

        # BOTAO ok SELECIONAR CATEGORIA janela 
         botao_selecao_categoria  = self.app.find_element_by_xpath('//*[@id="categories-dialog"]/div/div[3]/button[1]').click()
         sleep(5)
         self.app.execute_script('window.scrollTo( 0, 190000 );')
         sleep(6)
         
         # BOTAO ADICONAR PARA EFETIVAR INCLUSAO 
         botao_adicionar_conteudo  = self.app.find_element_by_xpath('//*[@id="tabs"]/div[3]/input[1]').click()
         sleep(4) 


        ######### MSG 01 ACONFIRMAÇAO INCLUSAO        
         msg01_valida_inclusao = self.app.find_element_by_xpath('//*[@id="managerContent"]/table/tbody/tr/td[2]/table[2]/tbody/tr[3]/td/div[1]')
         assert msg01_valida_inclusao.text == 'Registro inserido com sucesso.' 
         sleep(2) 

        ######### MSG 02 ACONFIRMAÇAO INCLUSAO        
         msg02_valida_inclusao = self.app.find_element_by_xpath('//*[@id="managerContent"]/table/tbody/tr/td[2]/table[2]/tbody/tr[3]/td/div[2]')
         assert  msg02_valida_inclusao.text == 'O vídeo foi incluído na última posição de cada carrossel ao qual foi associado.' 

         sleep (2)