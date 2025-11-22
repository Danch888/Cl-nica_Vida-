# Projeto Integrado - Clínica Vida+ (ADS 2025.2)

Repositório contendo as soluções desenvolvidas para o Projeto Integrado do curso de **Análise e Desenvolvimento de Sistemas** (2º Semestre). O objetivo é aplicar conhecimentos interdisciplinares para resolver problemas de gestão da "Clínica Vida+".

## 🏥 Cenário do Projeto
A **Clínica Vida+** enfrenta dificuldades com processos manuais de agendamento, histórico de pacientes e relatórios. A diretora, Sra. Helena, solicitou o desenvolvimento de um sistema de gestão para modernizar a clínica.

## 🛠️ Tecnologias e Conceitos Abordados
* **Gestão Ágil:** Scrum e Kanban (Trello).
* **Linguagem de Programação:** Python.
* **Lógica Computacional:** Estruturas de dados, Algoritmos e Lógica Booleana.
* **Engenharia de Software:** Modelagem UML (Diagrama de Casos de Uso).

## 📋 Estrutura do Trabalho

O projeto foi dividido em 5 passos práticos:

### Passo 1: Gestão de Projeto (Scrum)
Planejamento das tarefas utilizando um quadro Scrum no Trello, dividido em Backlog, Sprint Atual, Em Progresso e Concluído.

### Passo 2: Sistema em Python
Desenvolvimento de um protótipo funcional em Python com as seguintes funcionalidades:
* Cadastro de pacientes (Nome, Idade, Telefone).
* Cálculo de estatísticas (Total de pacientes, média de idade, paciente mais novo/velho).
* Busca de pacientes pelo nome.
* Listagem geral de cadastros.

### Passo 3: Lógica de Acesso (Tabelas Verdade)
Definição de regras lógicas para autorização de atendimento (Normal vs. Emergência) baseadas em variáveis como agendamento, documentos e pagamentos. Criação das respectivas tabelas verdade.

### Passo 4: Algoritmo de Fila
Elaboração de um pseudocódigo para simular uma fila de atendimento (FIFO - First In, First Out), permitindo inserção e remoção de pacientes.

### Passo 5: Modelagem UML
Criação de um Diagrama de Casos de Uso para representar as interações entre a Secretária, o Médico e o Sistema (agendamentos, receitas e cadastros).

---
## 🚀 Como executar o projeto
Para rodar o script do sistema da clínica:
1. Certifique-se de ter o **Python** instalado.
2. Clone este repositório.
3. Execute o arquivo principal no terminal:
   ```bash
   python sistema_clinica.py
