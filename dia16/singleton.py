class Gerente:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super(Gerente, cls).__new__(cls)
        return cls._instancia
    
gerente1 = Gerente()
gerente2 = Gerente()

print(gerente1 is gerente2)