# O sistema deverá permitir:
# • Cadastro de pacientes, médicos e exames;
# • Agendamento de consultas e exames, com controle de horários disponíveis;
# • Registro de atendimentos, com histórico de evolução por paciente;
# • Geração de relatórios mensais para a administração;

# ==============================================================================
# PROJETO INTEGRADO - SISTEMA CLÍNICA VIDA+
# ROTEIRO DE IMPLEMENTAÇÃO
# ==============================================================================

# 1. Inicializar as listas ou dicionários para armazenamento dos dados na memória.
#    Sugestão: Criar uma lista vazia chamada 'pacientes'.

# 2. Criar a estrutura de repetição principal (loop while) para manter o programa em execução.
#    O loop deve rodar indefinidamente até o usuário escolher sair.

    # 3. Implementar a exibição do menu de opções na tela.
    #    Opções: 1. Cadastrar, 2. Estatísticas, 3. Buscar, 4. Listar, 5. Sair.

    # 4. Criar a lógica de leitura da opção do usuário (input).
    #    Importante: Usar tratamento de erro (try/except) para entradas inválidas.

    # ==========================================================================
    # OPÇÃO 1: CADASTRAR PACIENTE
    # ==========================================================================
    # 5. Solicitar e validar as entradas de dados: Nome, Idade e Telefone.
    #    Dica: Idade deve ser um número inteiro.

    # 6. Armazenar os dados capturados (criar um dicionário e adicionar à lista 'pacientes').
    #    Exibir mensagem de sucesso.

    # ==========================================================================
    # OPÇÃO 2: ESTATÍSTICAS
    # ==========================================================================
    # 7. Calcular e exibir o número total de pacientes cadastrados (len da lista).

    # 8. Calcular e exibir a média de idade dos pacientes.
    #    Lógica: Somar todas as idades e dividir pelo total de pacientes.

    # 9. Identificar e exibir o paciente mais novo e o mais velho.
    #    Lógica: Percorrer a lista comparando as idades.

    # ==========================================================================
    # OPÇÃO 3: BUSCAR PACIENTE
    # ==========================================================================
    # 10. Solicitar o nome do paciente a ser buscado.
    #     Percorrer a lista e exibir os dados se encontrar o nome correspondente.

    # ==========================================================================
    # OPÇÃO 4: LISTAR TODOS
    # ==========================================================================
    # 11. Percorrer a lista de pacientes e imprimir todos os dados de forma organizada.

    # ==========================================================================
    # OPÇÃO 5: SAIR
    # ==========================================================================
    # 12. Encerrar o loop principal e finalizar o programa com uma mensagem de despedida.

import sys
import io
import os

# ==============================================================================
# CONFIGURAÇÕES INICIAIS
# ==============================================================================

# Força a saída padrão a usar UTF-8 (para corrigir acentos no Windows)
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Listas globais para armazenamento em memória
pacientes = []
medicos = []

# ==============================================================================
# FUNÇÕES AJUDANTES (VALIDAÇÃO E INTERFACE)
# ==============================================================================

def limpar_tela():
    """Limpa o terminal dependendo do sistema operacional."""
    os.system('cls' if os.name == 'nt' else 'clear')

def voltar_ao_menu():
    """Pausa a execução para o usuário ler a mensagem antes de voltar."""
    input("\n[Pressione Enter para voltar ao menu principal...]")
    limpar_tela()

def ler_texto(mensagem):
    """Lê apenas letras e espaços. Rejeita números e vazios."""
    while True:
        try:
            texto = input(mensagem).strip()
            if not texto:
                print("Erro: O campo não pode ficar vazio.")
                continue
            # Verifica se, tirando os espaços, sobram apenas letras
            if not texto.replace(" ", "").isalpha():
                print("Erro: Este campo aceita apenas letras. Tente novamente.")
                continue
            return texto.title() # Retorna com a primeira letra maiúscula (ex: João)
        except (KeyboardInterrupt, EOFError):
            print("\nOperação interrompida.")
            return None

def ler_inteiro(mensagem):
    """Lê apenas números inteiros positivos."""
    while True:
        try:
            entrada = input(mensagem).strip()
            if not entrada:
                print("Erro: O campo não pode ficar vazio.")
                continue
            numero = int(entrada)
            if numero <= 0:
                print("Erro: O número deve ser positivo.")
                continue
            return numero
        except ValueError:
            print("Erro: Entrada inválida. Digite apenas números inteiros.")
        except (KeyboardInterrupt, EOFError):
            print("\nOperação interrompida.")
            return None

def ler_generico_numerico(mensagem):
    """Lê strings que devem conter apenas números ou símbolos permitidos (Telefone/RG)."""
    while True:
        try:
            entrada = input(mensagem).strip()
            if not entrada:
                print("Erro: O campo não pode ficar vazio.")
                continue
            if len(entrada) < 3:
                print("Erro: Entrada muito curta.")
                continue
            return entrada
        except (KeyboardInterrupt, EOFError):
            print("\nOperação interrompida.")
            return None

# ==============================================================================
# FUNÇÕES DO SISTEMA (LÓGICA DE NEGÓCIO)
# ==============================================================================

def cadastrar_paciente():
    print("\n--- CADASTRO DE PACIENTE ---")
    
    nome = ler_texto("Nome do Paciente: ")
    if not nome: return

    idade = ler_inteiro("Idade: ")
    if not idade: return

    while True:
        sexo = input("Sexo (M/F): ").strip().upper()
        if sexo in ["M", "F"]:
            break
        print("Opção inválida. Digite M ou F.")

    telefone = ler_generico_numerico("Telefone: ")
    if not telefone: return

    novo_paciente = {
        "nome": nome,
        "idade": idade,
        "sexo": sexo,
        "telefone": telefone
    }
    pacientes.append(novo_paciente)
    print(f"\n✅ Paciente {nome} cadastrado com sucesso!")

def estatisticas():
    print("\n--- ESTATÍSTICAS DA CLÍNICA ---")
    total = len(pacientes)
    print(f"Total de pacientes cadastrados: {total}")

    if total == 0:
        print("⚠️ Não há dados suficientes para calcular médias.")
        return

    # Média de idade (Variável alterada de p -> pac)
    soma_idades = sum(pac["idade"] for pac in pacientes)
    media = soma_idades / total
    print(f"Média de idade dos pacientes: {media:.1f} anos")

    # Mais novo e mais velho (Variável alterada de p -> pac)
    mais_novo = min(pacientes, key=lambda pac: pac["idade"])
    mais_velho = max(pacientes, key=lambda pac: pac["idade"])
    
    print(f"Paciente mais novo: {mais_novo['nome']} ({mais_novo['idade']} anos)")
    print(f"Paciente mais velho: {mais_velho['nome']} ({mais_velho['idade']} anos)")

def buscar_paciente():
    print("\n--- BUSCAR PACIENTE ---")
    termo = input("Digite o nome para buscar: ").strip().lower()
    
    # Busca com variável alterada de p -> pac
    encontrados = [pac for pac in pacientes if termo in pac["nome"].lower()]
    
    if encontrados:
        print(f"\nEncontrados {len(encontrados)} paciente(s):")
        for pac in encontrados:
            print(f"- {pac['nome']} | Idade: {pac['idade']} | Tel: {pac['telefone']}")
    else:
        print("❌ Nenhum paciente encontrado com esse nome.")

def listar_tudo():
    print("\n--- LISTA GERAL DE PACIENTES ---")
    if not pacientes:
        print("Nenhum paciente cadastrado.")
    else:
        # Loop com variável alterada de p -> pac
        for i, pac in enumerate(pacientes, 1):
            print(f"{i}. {pac['nome'].ljust(20)} | {pac['idade']} anos | Tel: {pac['telefone']}")

# ==============================================================================
# MENU PRINCIPAL
# ==============================================================================

def executar_sistema():
    limpar_tela()
    while True:
        print("\n=== SISTEMA CLÍNICA VIDA+ ===")
        print("1. Cadastrar Paciente")
        print("2. Ver Estatísticas")
        print("3. Buscar Paciente")
        print("4. Listar Todos os Pacientes")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_paciente()
            voltar_ao_menu()
        elif opcao == "2":
            estatisticas()
            voltar_ao_menu()
        elif opcao == "3":
            buscar_paciente()
            voltar_ao_menu()
        elif opcao == "4":
            listar_tudo()
            voltar_ao_menu()
        elif opcao == "5":
            print("\nSaindo do sistema... Até logo!")
            break
        else:
            print("\n❌ Opção inválida! Tente novamente.")
            voltar_ao_menu()

if __name__ == "__main__":
    executar_sistema()