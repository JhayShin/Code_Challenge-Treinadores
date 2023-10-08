import sqlite3 as sql

con = sql.connect('treinador_db.db')

cur = con.cursor()

cur.execute('DROP TABLE IF EXISTS treinador')


sql = '''CREATE TABLE IF NOT EXISTS "treinador" (
    "ID" INTEGER PRIMARY KEY AUTOINCREMENT,
    "NICKNAME" TEXT,
    "FIRST_NAME" TEXT,
    "LAST_NAME" TEXT,
    "EMAIL" TEXT,
    "PASSWORD" TEXT,
    "TEAM" TEXT
)'''


sql1 = '''CREATE TABLE IF NOT EXISTS "pokemons" (
    "ID" INTEGER PRIMARY KEY AUTOINCREMENT,
    "POKE_ID" INTEGER,
    "POKE_NOME" TEXT,
    "POKE_FOTO" TEXT,
    "TREINADOR_ID" INTEGER, 
    FOREIGN KEY ("TREINADOR_ID") REFERENCES treinador(ID)
    ON DELETE CASCADE
    ON UPDATE CASCADE
)'''


cur.execute(sql)
cur.execute(sql1)


con.commit()
con.close()