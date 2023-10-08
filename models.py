import  sqlite3 as sql

class Treinador:
    def __init__(self, nickname, first_name, last_name, email, password, team):
        self.nickname = nickname
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.team = team

    def __init__(self):
        pass

    def mostrar_all_treinadores(self, ):
        con = sql.connect("treinador_db.db")
        con.row_factory = sql.Row
        cur = con.cursor()
        cur.execute("SELECT * FROM treinador")
        data = cur.fetchall()
        return data

    def mostrar_treinador(self, id):
        con = sql.connect("treinador_db.db")
        con.row_factory = sql.Row
        cur = con.cursor()
        cur.execute("SELECT * FROM treinador WHERE ID=?", (id,))
        data = cur.fetchone()
        return data


    def cad_treinador(self, nickname, first_name, last_name, email, password, team):
        con = sql.connect("treinador_db.db")
        cur = con.cursor()
        cur.execute("INSERT INTO treinador(NICKNAME, FIRST_NAME, LAST_NAME, EMAIL, PASSWORD, TEAM) values (?,?,?,?,?,?)", (nickname, first_name, last_name, email, password, team))
        con.commit()

    def edi_treinador(self, nickname, first_name, last_name, email, password, team, id):
        con = sql.connect("treinador_db.db")
        cur = con.cursor()
        cur.execute("UPDATE treinador SET NICKNAME=?, FIRST_NAME=?, LAST_NAME=?, EMAIL=?, PASSWORD=?, TEAM=? WHERE ID=?", (nickname, first_name, last_name, email, password, team, id))
        con.commit()

    def del_treinador(self, id):
        con = sql.connect("treinador_db.db")
        cur = con.cursor()
        cur.execute("DELETE FROM treinador WHERE id=?",(id,))
        cur.execute("DELETE FROM pokemons WHERE TREINADOR_ID=?",(id,))
        con.commit()


class Pokemon:
    def __init__(self, poke_id, poke_nome, poke_foto, treinador_id):
        self.poke_id = poke_id
        self.poke_name = poke_nome
        self.poke_foto = poke_foto
        self.treinador_id = treinador_id
        
    def __init__(self):
        pass

    def mostrar_pokemon(self, id):
        con = sql.connect("treinador_db.db")
        con.row_factory = sql.Row
        cur = con.cursor()
        cur.execute("SELECT * FROM pokemons WHERE TREINADOR_ID=?", (id,))
        data = cur.fetchall()
        return data
    
    def cad_pokemon(self, poke_id, poke_nome, poke_foto, treinador_id):
        con = sql.connect("treinador_db.db")
        cur = con.cursor()
        cur.execute("INSERT INTO pokemons(POKE_ID, POKE_NOME, POKE_FOTO, TREINADOR_ID) values (?,?,?,?)",(poke_id, poke_nome, poke_foto, treinador_id))
        con.commit()

    def del_pokemon(self, id):
        con = sql.connect("treinador_db.db")
        cur = con.cursor()
        cur.execute("DELETE FROM pokemons WHERE id=?",(id,))
        con.commit()