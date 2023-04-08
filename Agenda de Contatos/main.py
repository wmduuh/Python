#importando módulo com funções da agenda
from ext_1 import *

#Tela de apresentação do programa

print('''
      ################################################################################
      #                                AGENDA DE CONTATOS                            #
      #                                                                              #
      #  Esse projeto foi desenvovido sem necessidade bibliotecas adicionais, porém  #
      #    precisa dos módulos que estão presentes na pasta origem desse projeto.    #
      #                             Portanto não exclua-os!                          #
      #                                                                              #
      #           Aqui você poderá consultar, adicionar e remover contatos           #
      #                                                                              #
      #                                                     Developed by J. Eduardo  #
      ################################################################################
''')

#Verificando necessidade de importação de contatos
importing()

#Cria um arquivo Backup, para previnir perdas se o programa fechar
#Observação: Esse backup será excluído se não importá-lo na próxima execução
export_backup()

#Menu de opções da agenda
options()
