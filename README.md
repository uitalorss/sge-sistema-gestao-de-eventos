# sistema-gestao-eventos

<!---Esses são exemplos. Veja https://shields.io para outras pessoas ou para personalizar este conjunto de escudos. Você pode querer incluir dependências, status do projeto e informações de licença aqui--->

![Static Badge](https://img.shields.io/badge/status-finished-green?style=for-the-badge)
![GitHub repo size](https://img.shields.io/github/repo-size/uitalorss/sge-sistema-gestao-de-eventos?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/uitalorss/sge-sistema-gestao-de-eventos?style=for-the-badge)
![GitHub Contributors](https://img.shields.io/github/contributors/uitalorss/sge-sistema-gestao-de-eventos?style=for-the-badge&color=blue)

### 💡 Um pouco sobre o projeto.

A API de gestão de eventos é um projeto desenvolvido com o intuito de consolidar conhecimento no desenvolvimento back-end utilizando Python e o framework FastAPI através de uma API que permite gerenciar usuários que querem divulgar eventos e promover inscrições. Ela permite que organizadores criem, organizem e acompanhem seus eventos e participantes se inscrevam nos eventos criados.

## 💻 Tecnologias utilizadas

- Back-end
    - Python
    - FastAPI
    - SQLAlchemy
    - Alembic
    - JWT
    - Redis
    - Docker

## 🚀 Instalando o projeto
- Faça o clone do projeto através do comando `git clone https://github.com/uitalorss/todo-list_fast_api.git`
- Configure as variáveis de ambiente do backend em um arquivo `.env`.
  - Na pasta já há um arquivo .env.example.
  - Instale as dependências através do comando `pip install -r requirements.txt`.
  - Exeute `alembic upgrade head` para as migrações do banco de dados.
  - Caso utilize o Docker, configure as variáveis de ambientte e execute `docker compose up`.
    
## ☕ Usando o projeto
- Acesse a pasta do projeto.
- Digite o comando `fastapi dev main.py`.
    - Não é necessário executar esse comando caso tenha utilizado o comando do docker e o ambiente tenha subido corretamente.  
- Para acessar a documentação dos endpoints da APi digite o comando `http://localhost:8000/docs` ou `http://localhost:8000/redoc`.



## ✅ Requisitos funcionais

### Gestão de usuários 
- [x] **Criar usuário:** O sistema deve permitir a criação de um novo usuário.
- [x] **Atribuir perfis ao usuário:** O sistema deve permitir atribuir perfis (organizador ou participante).
- [x] **Autenticação:**  O sistema deve permitir que o usuário se autentique como organizador ou participante.

### Gestão de Eventos (Organizador):
- [x] **Criar evento:**  O organizador deve poder criar novos eventos no sistema.
- [x] **Editar evento:**  O organizador deve poder editar eventos criados.
- [x] **Excluir evento:**  O organizador deve poder excluir eventos criados.
- [x] **Listar eventos criados:**  O organizador deve poder listar todos os eventos que criou.

### Inscrição e Participação (Participante):
- [x] **Inscrever-se em evento:**  O participante deve poder se inscrever em um evento.
- [x] **Cancelar inscrição:**  O participante deve poder cancelar sua inscrição em um evento.
- [x] **Listar eventos inscritos:**  O participante deve poder listar todos os eventos em que está inscrito.

### Visualização de Eventos:
- [x] **Listar todos os eventos:**  O sistema deve permitir que qualquer pessoa (usuário ou não) acesse a lista de eventos.
- [x] **Listar determinado evento:**  O sistema deve permitir que qualquer pessoa (usuário ou não) acesse os detalhes de determinado evento.

## 📫 Contribuindo para o projeto

<!---Se o seu README for longo ou se você tiver algum processo ou etapas específicas que deseja que os contribuidores sigam, considere a criação de um arquivo CONTRIBUTING.md separado--->

Para contribuir com o projeto, siga estas etapas:

1. Bifurque este repositório.
2. Crie um branch: `git checkout -b <nome_branch>`.
3. Faça suas alterações e confirme-as: `git commit -m '<mensagem_commit>'`
4. Envie para o branch original: `git push origin <nome_do_projeto> / <local>`
5. Crie a solicitação de pull.

## 🤝 Colaboradores

Agradecemos às seguintes pessoas que contribuíram para este projeto:

<table>
  <tr>
    <td align="center">
      <a href="#">
        <img src="https://avatars.githubusercontent.com/u/15834173?v=4" width="100px;" alt="Foto do Uítalo Souza no GitHub"/><br>
        <sub>
          <b>Uítalo Souza</b>
        </sub>
      </a>
    </td>
  </tr>
</table>  


## 📝 Licença

Esse projeto está sob licença. Veja o arquivo [LICENÇA](LICENSE.md) para mais detalhes.

[⬆ Voltar ao topo](#sistema-gestao-eventos)<br>
