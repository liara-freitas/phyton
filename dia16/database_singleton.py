class Database:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia=super(Database, cls).__new__(cls)
            cls._instancia.conexao = "Conexão com o banco de dados estabelecida"

        return cls._instancia

    def conectar(self):
        print(self.conexao)

db1 = Database()
db2 = Database()

db1.conectar()
db2.conectar()

print(db1 is db2)