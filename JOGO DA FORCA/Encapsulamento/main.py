'''video 105'''
class BaseDeDados:
    def __init__(self):
        self.__dados = {}

    def inserirCliente(self, id, nome):
        if "clientes" not in self.__dados:
            self.__dados["clientes"] = {id: nome}
        else:
            self.__dados["clientes"].update({id: nome})

    def listaClientes(self):
        for id, nome in self.__dados["clientes"].items():
            print(id, nome)

    def apagaClientes(self, id):
        del self.__dados["clientes"][id]

bd = BaseDeDados()
bd.inserirCliente(1, "Otavio")
bd.inserirCliente(2, "miranda")
bd.inserirCliente(3, "rose")
bd.apagaClientes(2)

bd.listaClientes()