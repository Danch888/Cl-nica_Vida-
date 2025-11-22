from typing import List, Dict
import sys
import io

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


"""
Sistema simples para cadastro e consulta de pacientes.
Segui os passos comentados no arquivo original:
1) Lista 'pacientes' em memória.
2) Loop principal com menu (Cadastrar, Estatísticas, Buscar, Listar, Sair).
3) Validações básicas de entrada com try/except.
Todos os trechos do código estão comentados de forma direta para facilitar entendimento.
"""

# Força a saída padrão a usar UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# ---------- Estrutura de armazenamento ----------
# Cada paciente será representado por um dicionário com chaves: nome, idade, sexo, telefone
pacientes: List[Dict[str, object]] = []


# ---------- Funções auxiliares ----------

def cadastrar_paciente():
  """
  Solicita dados do paciente, valida entradas e adiciona o dicionário resultante
  à lista 'pacientes'. Trata erros de entrada do usuário (EOF, KeyboardInterrupt,
  valores inválidos) e informa quando o cadastro é cancelado.
  """
  try:
    # Nome
    nome = input("Nome: ").strip()
    if not nome:
      print("Nome não pode ficar vazio. Cadastro cancelado.")
      return

    # Idade: loop até obter um inteiro positivo ou cancelar
    try:
      idade_str = input("Idade: ").strip()
    except (EOFError, KeyboardInterrupt):
      print("\nEntrada cancelada pelo usuário. Cadastro abortado.")
      return

    try:
      idade = int(idade_str)
      if idade <= 0:
        print("Idade deve ser um número inteiro positivo. Cadastro cancelado.")
        return
    except ValueError:
      print("Entrada inválida para idade. Use um número inteiro. Cadastro cancelado.")
      return

    # Sexo: aceitar 'M' ou 'F' (case-insensitive)
    try:
      sexo = input("Sexo (M/F): ").strip().upper()
    except (EOFError, KeyboardInterrupt):
      print("\nEntrada cancelada pelo usuário. Cadastro abortado.")
      return

    if sexo not in {"M", "F"}:
      print("Sexo inválido. Use 'M' para masculino ou 'F' para feminino. Cadastro cancelado.")
      return

    # Telefone: apenas valida presença; pode-se estender para validar formato
    try:
      telefone = input("Telefone: ").strip()
    except (EOFError, KeyboardInterrupt):
      print("\nEntrada cancelada pelo usuário. Cadastro abortado.")
      return

    if not telefone:
      print("Telefone não pode ficar vazio. Cadastro cancelado.")
      return

    # Criar e adicionar o paciente
    paciente = {"nome": nome, "idade": idade, "sexo": sexo, "telefone": telefone}
    pacientes.append(paciente)
    print(f"Paciente '{nome}' cadastrado com sucesso.")

  except Exception as e:
    # Tratamento genérico para evitar que erros inesperados quebrem o programa
    print(f"Ocorreu um erro inesperado durante o cadastro: {e}")
    print("Cadastro cancelado.")


def estatisticas():
  """
  Exibe estatísticas básicas: total de pacientes, média de idade, paciente mais novo e mais velho.
  """
  total = len(pacientes)
  print(f"Total de pacientes cadastrados: {total}")

  if total == 0:
    print("Não há pacientes para calcular estatísticas.")
    return

  # Calcular média de idade
  soma_idades = sum(p["idade"] for p in pacientes)
  media = soma_idades / total
  print(f"Média de idade: {media:.2f} anos")

  # Encontrar paciente mais novo e mais velho
  mais_novo = min(pacientes, key=lambda p: p["idade"])
  mais_velho = max(pacientes, key=lambda p: p["idade"])
  print(f"Paciente mais novo: {mais_novo['nome']} ({mais_novo['idade']} anos)")
  print(f"Paciente mais velho: {mais_velho['nome']} ({mais_velho['idade']} anos)")


def buscar_paciente():
  """
  Busca paciente pelo nome (busca parcial e case-insensitive) e exibe resultados encontrados.
  """
  termo = input("Digite o nome (ou parte do nome) para buscar: ").strip().casefold()
  if not termo:
    print("Termo de busca vazio. Operação cancelada.")
    return

  encontrados = [p for p in pacientes if termo in p["nome"].casefold()]
  if not encontrados:
    print("Nenhum paciente encontrado com esse termo.")
    return

  # Exibir todos os pacientes encontrados
  print(f"{len(encontrados)} paciente(s) encontrado(s):")
  for idx, p in enumerate(encontrados, start=1):
    print(f"{idx}. Nome: {p['nome']}, Idade: {p['idade']}, Telefone: {p['telefone']}")


def listar_pacientes():
  """
  Lista todos os pacientes cadastrados de forma organizada.
  """
  if not pacientes:
    print("Nenhum paciente cadastrado.")
    return

  print("Lista de pacientes:")
  for i, p in enumerate(pacientes, start=1):
    print(f"{i}. Nome: {p['nome']} | Idade: {p['idade']} | Telefone: {p['telefone']}")


# ---------- Loop principal com menu ----------
def executar_sistema():
  """
  Loop principal que mostra o menu, lê a opção do usuário com tratamento de erros
  e chama as funções correspondentes até o usuário escolher sair.
  """
  while True:
    print("\n--- SISTEMA CLÍNICA VIDA+ ---")
    print("1. Cadastrar paciente")
    print("2. Estatísticas")
    print("3. Buscar paciente")
    print("4. Listar todos os pacientes")
    print("5. Sair")

    # Ler opção com tratamento para entradas inválidas
    opcao = input("Escolha uma opção (1-5): ").strip()
    if not opcao:
      print("Opção vazia. Tente novamente.")
      continue

    # Validar que a opção é um número entre 1 e 5
    if opcao not in {"1", "2", "3", "4", "5"}:
      print("Opção inválida. Informe um número entre 1 e 5.")
      continue

    # Mapear e executar as ações
    if opcao == "1":
      cadastrar_paciente()
    elif opcao == "2":
      estatisticas()
    elif opcao == "3":
      buscar_paciente()
    elif opcao == "4":
      listar_pacientes()
    elif opcao == "5":
      print("Encerrando o sistema. Obrigado e até logo!")
      break


# Permite executar o sistema quando o arquivo for executado diretamente
if __name__ == "__main__":
  executar_sistema()
