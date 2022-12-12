# Controle de estacionamento

Projeto consiste em um API de controle de estacionamento, que:

- Registra entrada, saída e pagamento.
- Não libera a saída sem o pagamento
- Fornece um histórico por placa
- Validar máscara AAA-9999

![django.gif](presentation_project.gif)

## Tecnologia

- Django

## Como executar

- Clone este repositório
  ```console
   git clone https://github.com/DandaraF/controle-estacionamento.git
  ```
- Instale a máquina virtual. Python: 3.8

- Ative a máquina virtual:
  ```console
  source venv/bin/activate
  ```
- Instalar o dependências:
  ```console
  pip install -r requirements.txt
  ```
- Starte o projeto:
  ```console
  python manage.py runserver
  ```
- Clique no link abaixo ou digite o link no navegador:
  - http://127.0.0.1:8000

## Informações da API

- Página inicial: http://127.0.0.1:8000
- Saída: http://127.0.0.1:8000/parking/{id}/pay
- Pagamento: http://127.0.0.1:8000/{id}/pay

- Histórico: http://127.0.0.1:8000/parking/{placa}
