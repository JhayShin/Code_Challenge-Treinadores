from flask import Flask, render_template, request, redirect, url_for, flash
import requests, json
from models import Treinador, Pokemon



app = Flask(__name__)
exec(open('treinador_db.py').read())

@app.route("/")
@app.route("/index")
def index():
    treinador = Treinador()
    data = treinador.mostrar_all_treinadores()
    return render_template("index.html", datas=data)


@app.route("/add_treinador", methods=["POST", "GET"])
def add_treinador():
    if request.method == "POST":
        try:
            nickname = request.form["nickname"]
            first_name = request.form["first_name"]
            last_name = request.form["last_name"]
            email = request.form["email"]
            password = request.form["password"]
            team = request.form["team"]
            treinador = Treinador()
            treinador.cad_treinador(nickname, first_name, last_name, email, password, team)
            
            flash("Dados cadastrados", "success")
            return redirect(url_for("index"))
        except:
            flash("Houve algum erro", "warining")
            return redirect(url_for("index"))
        
    return render_template("add_treinador.html")


@app.route("/edit_treinador/<string:id>", methods=["POST", "GET"])
def edit_treinador(id):
    if request.method == "POST":
        try:
            nickname = request.form["nickname"]
            first_name = request.form["first_name"]
            last_name = request.form["last_name"]
            email = request.form["email"]
            password = request.form["password"]
            team = request.form["team"]

            treinador = Treinador(nickname, first_name, last_name, email, password, team)
            treinador.edi_treinador(id)

            flash("Dados atualizados", "success")
            return redirect(url_for("index"))
        
        except:
            flash("Houve algum erro", "warning")
            return redirect(url_for("index"))
        
    treinador = Treinador()
    data = treinador.mostrar_treinador(id)
    return render_template("edit_treinador.html", datas=data)


@app.route("/train_poke/<string:id>", methods=["POST", "GET"])
def train_poke(id):
    if request.method == "POST":
        try:
            busca = request.form["poke_nome"].lower()
            url = f'https://pokeapi.co/api/v2/pokemon/{busca}/'
            res = requests.get(url)
            poke = res.json()

            poke_id = poke['id']
            poke_nome = poke['name']
            poke_foto = poke['sprites']['front_default']
            treinador_id = id
            pokemon = Pokemon()
            pokemon.cad_pokemon(poke_id, poke_nome, poke_foto, treinador_id)

            flash("Dados cadastrados", "success")
            return redirect(url_for("train_poke", id = treinador_id))
        except:
            flash("Pokemon não encontrado", "warning")
    
    treinador = Treinador()
    pokemon = Pokemon()
    data1 = treinador.mostrar_treinador(id)
    data2 = pokemon.mostrar_pokemon(id)

    return render_template("train_poke.html", datas1=data1, datas2=data2, )


@app.route("/delete_poke/<string:id>, <string:t_id>", methods=["GET"])
def delete_poke(id, t_id):
    try:
        treinador_id = t_id
        pokemon = Pokemon()
        pokemon.del_pokemon(id)
    except:
        flash("Houve um erro", "warning")

    flash("Dados deletados", "warning")
    return redirect(url_for("train_poke", id = treinador_id))



@app.route("/delete_treinador/<string:id>", methods=["GET"])
def delete_treinador(id):
    treinador = Treinador()
    try:
        treinador.del_treinador(id)
        flash("Dados deletados", "warning")
        return redirect(url_for("index"))
    except:
        flash("Houve um erro", "warning")


if __name__ == '__main__':
    app.secret_key="admin123"
    app.run(debug=True)