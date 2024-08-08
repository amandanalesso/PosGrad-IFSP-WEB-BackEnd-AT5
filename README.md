# API Dragons

## Descrição

API desenvolvida em Flask com informações sobre os dragões dos livros das Cronicas de Gelo e Fogo e História dos Targaryen, para a disciplina de Backend I do curso de Pós Graduação em desenvolvimento web do IFSP, A API oferece endpoints para um CRUD

### Requisitos

- Python 3.10+
- pip (gerenciador de pacotes do Python)

## Como Utilizar

## Instalação

1. **Clone o repositório**:

   ```bash
    git clone https://github.com/amandanalesso/PosGrad-IFSP-WEB-BackEnd-AT5.git
 
2. **Entrar em seu repositório local** 
 
   ```bash
    cd diretorio

3. **Crie e ative um ambiente virtual**:
   
    ```bash
    python3 -m venv env
    source env/bin/activate  # Linux e macOS
   .\env\Scripts\activate  # Windows


4. **Instalar dependências**
   
   ```bash
     pip install -r requirements.txt
 
5. **Para rodar a API**

    ```bash
     python app.py # na raiz do projeto

A API estará disponível em \`http://localhost:5000\`.



## Rotas 

   #### GET /dragons:   Retorna todos os dragões
   #### POST /dragons
   #### GET  /dragons/id
   #### PUT: /dragons/id
   #### DELETE:  /dragons/id


## Contribuição

Se você quiser contribuir para este projeto, siga os passos abaixo:

1. Faça um fork do repositório.
2. Crie uma nova branch (\`git checkout -b feature/nome-da-sua-feature\`).
3. Faça suas alterações e commit (\`git commit -m 'Adiciona nova feature'\`).
4. Envie suas mudanças para o repositório remoto (\`git push origin feature/nome-da-sua-feature\`).
5. Abra um Pull Request.

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.
EOF
