import sqlite3
conexao = sqlite3.connect('luan.db')
cursor = conexao.cursor()

cursor.execute('''CREATE TABLE usuarios (''')