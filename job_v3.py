import csv
import sqlite3

def remove_ponto(valor):

    return int(valor.replace('.',''))

File_path = "/home/breno/Documentos/DSA/FundamentosdeEngenhariadedados/Projeto4/produtos.csv"

with open(File_path,'r') as file:

    reader = csv.reader(file)

    next(reader)

    conn = sqlite3.connect('pordutos.db')

    conn.execute('DROP TABLE IF EXISTS producao')

    conn.execute(''' CREATE TABLE producao(
                    produto TEXT,
                    quantidade INTEGER,
                    preco_medio REAL,
                    receita_total REAL
                )
                ''')
    
    for row in reader:

        if int(row[1]) >= 6500:

            row[3] = remove_ponto(row[3])

            conn.execute('INSERT INTO producao(produto, quantidade, preco_medio, receita_total) VALUES (?,?,?,?)',row)

    conn.commit()

    conn.close()


print("Job finalizado com sucesso")