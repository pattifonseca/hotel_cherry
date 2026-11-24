quartos = []
reservas = []
def cadastrar_quartos(quartos,numero,tipo,diaria):
    if numero <=0:
        print("Erro. Número de quarto negativo")
        return
    if diaria <= 0 :
         print("Erro. Diária negativa")
         return
    for quarto in quartos:
            if quarto['numero'] == numero:
                print("Número de quarto já cadastrado")
                return
            
    quarto = {
        "numero": numero,
        "tipo": tipo,
        "diaria": diaria,
        "disponivel": True
    }

    quartos.append(quarto)
    print("Cadastro efetuado com sucesso!")

    
def listar_quartos(quartos):
    contador = 0
    for quarto in quartos: 
        for k,v in quarto.items():
             print(f"{k}: {v}")
             if v == True:
              contador += 1 
        print("_"*20)

    if contador >= 0:
        print(f"Estamos com {contador} quartos disponveís")
    else:
        print("Estamos com todos os quartos reservados")


def realizar_reservas(quartos,reservas,numero,hospede,dias):
    quarto_encontrado = None
    for quarto in quartos:
        if numero == quarto['numero']:
            quarto_encontrado = quarto
            break

    if quarto_encontrado is None:
        print("Quarto não encontrado")
        return
    
    if quarto_encontrado["disponivel"] == False:
        print("Reserva negada. Quarto não disponível!")
        return

    
    if dias <= 0 :
            print("Dados inválidos. Diária esta negativa")
            return

    valor_total = dias * quarto_encontrado['diaria']

    reserva_efetuada = {"hospede":hospede,
                        "numero": numero,
                        "dias": dias,
                        "valor_total": valor_total,
                        "ativa" : True                   

    }   
    reservas.append(reserva_efetuada)
    quarto_encontrado["disponivel"] = False

    print("Reserva realizada com sucesso!")

def cancelar_reserva(reservas,quartos,hospede):
    for reserva in reservas:
        if hospede == reserva['hospede'] and reserva['ativa'] == True:
            reserva['ativa'] = False
            for quarto in quartos:
                if quarto['numero'] == reserva['numero']:
                    quarto['disponivel'] = True
            print(f"Reserva de {reserva['hospede']} cancelada.")
            return
    print("Nenhuma reserva ativa encontrada para esse hóspede.")       

def consultar_reserva(reservas,hospede):
    encontrou = False
    for reserva in reservas:         
        if reserva['hospede'] == hospede:
            encontrou = True

            if reserva['ativa'] == False:
                print("Esta reserva já foi cancelada")
            else:
                for k,v in reserva.items():
                    print(f"{k}: {v}")
    if not encontrou:
        print("Nnenhuma reserva encontrada.") 

while True:
    print()
    print("="*10,"HOTEL CHERRY", 10 *"=")
    print(f"1 - Cadastrar quarto",
        f"\n2 - Listar quartos",
        f"\n3 - Realizar reserva",
        f"\n4 - Cancelar reserva",
        f"\n5 - Consultar reserva",
        f"\n6 - Sair")
    try:
        opcao = int(input("Escolha uma opção: "))
        print()

        if opcao == 6:
             print("Saindo do programa...")
             break 
          
        if opcao == 1:
            numero = int(input("Número do quarto: "))
            tipo = str(input("Tipo de acomodação:(Simples,Duplo ou Luxo) ")).strip().capitalize()
            diaria = float(input("Diária do quarto:R$ ").replace(",","."))
            cadastrar_quartos(quartos,numero,tipo,diaria)

        elif opcao == 2:
            listar_quartos(quartos)


        elif opcao == 3:
            numero = int(input("Qual quarto gostaria de fazer a reserva? "))
            hospede = input("Responsável pela reserva? ").strip().capitalize()
            if hospede.isdigit() or not hospede:
                print("Nome inválido! Digite um nome válido.")
            else:
                dias = int(input("Quantos dias de reserva? "))
                realizar_reservas(quartos, reservas, numero, hospede, dias)


        elif opcao == 4:
            hospede = str(input("Nome do responsavél pela reserva: ")).strip().capitalize()
            cancelar_reserva(reservas,quartos,hospede)


        elif opcao == 5:
            hospede = str(input("Colsultar reserva no nome de: ")).strip().capitalize()
            if hospede.isdigit() or not hospede:
                print("Nome inválido! Digite um nome válido.")
            else:
                break
            consultar_reserva(reservas,hospede)

        elif opcao == 6:
            print("Programa encerrado!")
            break
        else:
            print("Opção inválida")

            
    except ValueError:
        print("Solicitação negada, dados invalidos.")




