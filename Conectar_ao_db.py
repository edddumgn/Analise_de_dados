import pyodbc

dados_conexao = (
	"Driver={SQL Server};"
	"Server=LAPTOP-FKR3K1O2\SQLEXPRESS;"  #No cmd hostname
	"Database=PythonSQL"
)


conexao = pyodbc.connect(dados_conexao)
print('Conexão bem sucedida')
