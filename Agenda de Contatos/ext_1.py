from time import sleep

#Dicionário responsável pelo banco de informações do programa em execução
ADDRESS_BOOK={}

#função apenas para impressão visual
def menu_show():
    print('='*80,'\n')
    print('  >> 1. Mostrar contatos cadastrados.')
    print('  >> 2. Buscar contato.')
    print('  >> 3. Adicionar ou editar contato.')
    print('  >> 4. Excluir contato.')
    print('  >> 5. Exportar')
    print('  >> 6. Sair.\n')

#Está função é "mãe" das demais, responsável por solicitar e compartilhar informações
def options():
    comando=0
    while comando<=7:
        menu_show()
        try:
            print('='*80)
            comando=int(input('Digite a opção que deseja, conforme o número: '))
            if comando/comando==1:
                print("\nCarregando...\n")
                sleep(1)
                if comando==1:
                    show_contact()
                    if ADDRESS_BOOK=={}:
                        print('A agenda está vazia.\n')
                elif comando==2:
                    why=str(input('Qual contato deseja visualizar? ')).upper().strip()
                    if why in ADDRESS_BOOK:
                        for contact in ADDRESS_BOOK:
                            search(contact)
                    else: 
                        print('\nContato não encontrado.')
                elif comando==3:
                    adding_edit()
                elif comando==4:
                    contact=str(input("Qual contato deseja deletar? ")).upper().strip()
                    delete(contact)
                elif comando==5:
                    export()
                    print('Exportado!\n')
                elif comando==6:
                    exiting()
                    break
                else:
                    print('Não há essa opção.')
            else:
                print('Formato incorreto')
        except:
            print('Utilize apenas números!')
            print('Digite uma das opções abaixo:\n')

# Responsável por compartilhar dados de um contato específico
def search(contact):
    try:
        print('Nome: ',contact)
        print('Telefone: ', ADDRESS_BOOK[contact]['Telefone'])
        print('E-mail: ', ADDRESS_BOOK[contact]['E-mail'])
        print('Endereço: ', ADDRESS_BOOK[contact]['Endereço'])
        print('\n')
    except Exception as error:
        print('Erro ',error)
# Mostra todos os contatos que estão na agenda aberta
def show_contact():
    for contact in ADDRESS_BOOK:
        search(contact)

# Função inicial, responsável por questionar e importar um arquivo .csv e convertê-lo para dicionário.
def importing():
    print('Antes de abrir a agenda, preciso saber:')
    entrada=input('>> Possui alguma agenda nesta pasta para importar? (y/n): ')
    entrada=entrada.strip().upper()
    cont=False
    while cont==False:    
            if entrada=='Y':
                arquivo=str(input('Digite o nome exato do seu arquivo .csv (não informe a extensão):  ').strip())
                try:
                    arquivo=str(f'{arquivo}.csv')
                    try:
                        with open(arquivo,'r') as files:
                            lines=files.readlines()
                            for line in lines:
                                details=line.strip().split(',')
                                name=details[0]
                                phone=details[1]
                                email=details[2]
                                address=details[3]
                                add(name,phone,email,address)
                            print('Contatos importados!\n')
                    except FileNotFoundError:
                        sleep(1)
                        print('\nProblema ao importar, não há arquivo com esse nome.\n')
                        f=str(input('Deseja prosseguir mesmo assim? (y/n):  ').upper())
                        if f=='Y':
                            print('\n\n')
                            pass
                        else:
                            print('Finalizando agenda...')
                            sleep(1)
                            exit()
                except Exception as Error:
                    print(f'Algo deu errado\nIdentificador:{Error}')
                    pass
                cont=True
            elif entrada == "N":
                print('\n''  # Tudo bem, iremos criar uma nova agenda.\n')
                cont=True
            else:
                print('Saindo...')
                sleep(1)
                exit()               

# Responsável por anexar dados ao dicionário
def add(name, cellphone, email, address):
    ADDRESS_BOOK[name]={
    'Telefone':cellphone,
    'E-mail':email,
    'Endereço':address
    }

# Utilizado para solicitar dados ao usuário e acionar a função "add" para anexar.
def adding_edit():
    importing_backup()
    name=input("Qual o nome do contato?  ").upper().strip()
    phone=input("Digite o número de telefone (DDD+Número):  ").strip()
    email=input("Qual seu email?  ").strip().lower()
    address=input("Qual seu endereço? (rua, nº - bairro - cidade / UF)  ").upper()
    add(name,phone,email,address)
    export_backup()
    print('\n''Contato adicionado!\n')

# guarda todo contato que é adicionado no programa aberto
# Serve para casos de fechamento inesperado ou queda de energia/desligamento
# Porém se o cliente abrir novamente o main.py e não importar o arquivo 'agenda_backup.csv', os dados serão apagados.
def importing_backup():
    with open('agenda_backup.csv','r') as files:
        lines=files.readlines()
        for line in lines:
            details=line.strip().split(',')
            name=details[0]
            phone=details[1]
            email=details[2]
            address=details[3]
            add(name,phone,email,address)

# Função responsável por Exportar um arquivo .csv com os dados do dicionário. Transformando em uma agenda.
def export():
    file=input('Qual o nome do arquivo? ').strip()
    file=str(f'{file}.csv')
    with open(file,'w') as files:
        for contact in ADDRESS_BOOK:
            phone=ADDRESS_BOOK[contact]['Telefone']
            email=ADDRESS_BOOK[contact]['E-mail']
            address=ADDRESS_BOOK[contact]['Endereço']
            exporting=(f'{contact},{phone},{email},{address}\n')
            files.write(exporting)

# Complementa a função importing_backup, pois lê o que foi colocado no dicionário
# Salva as alterações do dicionário no arquivo de backup 
def export_backup():
    file=str('agenda_backup.csv')
    with open(file,'w') as files:
        for contact in ADDRESS_BOOK:
            phone=ADDRESS_BOOK[contact]['Telefone']
            email=ADDRESS_BOOK[contact]['E-mail']
            address=ADDRESS_BOOK[contact]['Endereço']
            exporting=(f'{contact},{phone},{email},{address}\n')
            files.write(exporting)

# Utilizado para excluir um contato específico
def delete(contact):
    try:
        ADDRESS_BOOK.pop(contact)
        print('Deletado!')
    except:
        print('  >> Algo deu errado. Contato não encontrado!\n')
# Exibição da mensagem de saída
def exiting():
    print('Finalizando Agenda...')
    sleep(1)
    print('Processo fechado.')