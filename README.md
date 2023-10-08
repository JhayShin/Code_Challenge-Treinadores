# Code_Challenge-Treinadores
Este projeto é uma API simples para CRUD de Treinadores e Pokemons, que utiliza a PokéAPI para obter informações sobre os Pokémon. A aplicação é construída em Flask e utiliza um banco de dados em SQLite3 para armazenar informações sobre os treinadores e seus Pokémons.

### Instalação de bibliotecas

O Flask é o framework web utilizado no projeto e o Requests é utilizado para fazer requisições HTTP no projeto. Para instala-los utilize os seguintes comandos:
```bash
# Flask
pip install Flask

# Requests
pip install requests
```

### Instalação do SQLite
No Windows
Visite o site https://www.sqlite.org/download.html na pagina de download e siga as instruções de download e instalção de pré compilado do "sqlite-tools"

No linux
```bash
sudo apt-get update
sudo apt-get install sqlite3
```
No macOS
```bash
brew update
brew install sqlite3
```
### Ambiente Virtual
Recomenda-se o uso de um ambiente virtual para isolar as dependências do projeto.
Utilize o seguinte comando para criar e ativar o ambiente virtual:

```bash
python -m venv venv
# No Windows
.\venv\Scripts\activate
# No Linux/Mac
source venv/bin/activate
```

### Execução
```bash
python app.py
```
