import csv 
import sqlite3


conn = sqlite3.connect('produtos.db') # Cria um banco de dados. 

conn.execute(''' CREATE TABLE producao(
             produto TEXT,
             quantidade INTEGER,
             preco_medio REAL,
             receita_total REAL
             )
''')
conn.commit()#Comita as alterações no banco
conn.close()#fecha a conexão com o banco


File_path = "/home/breno/Documentos/DSA/FundamentosdeEngenhariadedados/Projeto4/produtos.csv" #Contem o caminho do arquivo para extração dos dados


with open(File_path,'r') as file:

    reader = csv.reader(file) #Cria um leitor de csv para leitura do arquivo

    next(reader) #Pula a primeira linha do CSV que contem os cabeçalhos. 

    conn = sqlite3.connect('produtos.db') #cria conexão com o banco de dados. 

    for row in reader:

        conn.execute('INSERT INTO producao(produto, quantidade, preco_medio, receita_total) VALUES (?,?,?,?)',row)

    conn.commit()

    conn.close()
    
print('Job concluido com sucesso!')