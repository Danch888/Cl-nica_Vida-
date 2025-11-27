import sys
import io
import os

# ==============================================================================
# CONFIGURAÇÕES INICIAIS
# ==============================================================================

# Força a saída padrão a usar UTF-8 (para corrigir acentos no Windows)
# Reatribui sys.stdout para garantir que prints exibam acentuação corretamente
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Listas globais para armazenamento em memória
# 'pacientes' guarda dicionários com dados de cada paciente
# 'medicos' criado para futuro uso (ainda não utilizado neste código)
pacientes = []
medicos = []

# ==============================================================================
# FUNÇÕES AJUDANTES (VALIDAÇÃO E INTERFACE)
# ==============================================================================

def limpar_tela():
    """Limpa o terminal dependendo do sistema operacional."""
    # Use 'cls' no Windows, 'clear' em Unix/Linux/Mac
    os.system('cls' if os.name == 'nt' else 'clear')

def voltar_ao_menu():
    """Pausa a execução para o usuário ler a mensagem antes de voltar."""
    # Aguarda Enter e em seguida limpa a tela para voltar à interface principal
    input("\n[Pressione Enter para voltar ao menu principal...]")
    limpar_tela()

def ler_texto(mensagem):
    """Lê apenas letras e espaços. Rejeita números e vazios.
    Retorna o texto formatado com Title Case ou None em caso de interrupção.
    """
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
            # Ex.: "joão da silva" -> "João Da Silva"
            return texto.title()
        except (KeyboardInterrupt, EOFError):
            # Trata Ctrl+C ou Ctrl+D e retorna None para cancelar operação
            print("\nOperação interrompida.")
            return None

def ler_inteiro(mensagem):
    """Lê apenas números inteiros positivos.
    Em caso de entrada inválida, repete a solicitação.
    Retorna int ou None se interrompido.
    """
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
            # Entrada que não é um inteiro válido
            print("Erro: Entrada inválida. Digite apenas números inteiros.")
        except (KeyboardInterrupt, EOFError):
            print("\nOperação interrompida.")
            return None

def ler_generico_numerico(mensagem):
    """Lê strings que devem conter apenas números ou símbolos permitidos (Telefone/RG).
    Não valida formato específico, apenas garante que não seja vazio e tenha tamanho mínimo.
    """
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
    """Coleta dados do paciente, valida e adiciona o registro à lista 'pacientes'."""
    print("\n--- CADASTRO DE PACIENTE ---")
    
    # Nome (apenas letras e espaços)
    nome = ler_texto("Nome do Paciente: ")
    if not nome: return  # interrompido pelo usuário

    # Idade (inteiro positivo)
    idade = ler_inteiro("Idade: ")
    if not idade: return

    # Sexo: aceita apenas 'M' ou 'F' (upper)
    while True:
        sexo = input("Sexo (M/F): ").strip().upper()
        if sexo in ["M", "F"]:
            break
        print("Opção inválida. Digite M ou F.")

    # Telefone (ou outro campo numérico genérico)
    telefone = ler_generico_numerico("Telefone: ")
    if not telefone: return

    # Cria dicionário do paciente e adiciona à lista global
    novo_paciente = {
        "nome": nome,
        "idade": idade,
        "sexo": sexo,
        "telefone": telefone
    }
    pacientes.append(novo_paciente)
    print(f"\n✅ Paciente {nome} cadastrado com sucesso!")

def estatisticas():
    """Calcula e exibe estatísticas básicas sobre os pacientes cadastrados."""
    print("\n--- ESTATÍSTICAS DA CLÍNICA ---")
    total = len(pacientes)
    print(f"Total de pacientes cadastrados: {total}")

    if total == 0:
        # Se não houver pacientes, não faz cálculos de média ou extremos
        print("⚠️ Não há dados suficientes para calcular médias.")
        return

    # Soma das idades e cálculo da média
    soma_idades = sum(pac["idade"] for pac in pacientes)
    media = soma_idades / total
    print(f"Média de idade dos pacientes: {media:.1f} anos")

    # Identifica o paciente mais novo e o mais velho usando key na função min/max
    mais_novo = min(pacientes, key=lambda pac: pac["idade"])
    mais_velho = max(pacientes, key=lambda pac: pac["idade"])
    
    print(f"Paciente mais novo: {mais_novo['nome']} ({mais_novo['idade']} anos)")
    print(f"Paciente mais velho: {mais_velho['nome']} ({mais_velho['idade']} anos)")

def buscar_paciente():
    """Busca pacientes por termo no nome (busca parcial, case-insensitive)."""
    print("\n--- BUSCAR PACIENTE ---")
    termo = input("Digite o nome para buscar: ").strip().lower()
    
    # Lista todos pacientes cujo nome contém o termo (ignora maiúsculas/minúsculas)
    encontrados = [pac for pac in pacientes if termo in pac["nome"].lower()]
    
    if encontrados:
        print(f"\nEncontrados {len(encontrados)} paciente(s):")
        for pac in encontrados:
            # Exibe resumo dos dados encontrados
            print(f"- {pac['nome']} | Idade: {pac['idade']} | Tel: {pac['telefone']}")
    else:
        print("❌ Nenhum paciente encontrado com esse nome.")

def listar_tudo():
    """Imprime todos os pacientes cadastrados de forma organizada."""
    print("\n--- LISTA GERAL DE PACIENTES ---")
    if not pacientes:
        print("Nenhum paciente cadastrado.")
    else:
        # Enumera e mostra cada registro com formatação simples
        for i, pac in enumerate(pacientes, 1):
            print(f"{i}. {pac['nome'].ljust(20)} | {pac['idade']} anos | Tel: {pac['telefone']}")

# ==============================================================================
# MENU PRINCIPAL
# ==============================================================================

def executar_sistema():
    """Loop principal que exibe o menu e chama as funções conforme a opção escolhida."""
    limpar_tela()
    while True:
        print("\n=== SISTEMA CLÍNICA VIDA+ ===")
        print("1. Cadastrar Paciente")
        print("2. Ver Estatísticas")
        print("3. Buscar Paciente")
        print("4. Listar Todos os Pacientes")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ").strip()

        # Roteamento simples por comparação de string
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
            # Encerra o loop principal e finaliza o programa
            print("\nSaindo do sistema... Até logo!")
            break
        else:
            # Tratamento para opções inválidas
            print("\n❌ Opção inválida! Tente novamente.")
            voltar_ao_menu()

if __name__ == "__main__":
    # Executa o sistema apenas se o arquivo for executado diretamente (não quando importado)
    executar_sistema()