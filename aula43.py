# Desempacotamento de listas e python

# *outra_lista = gerador automatico de listas
# caso queira pegar o ultimo numero da lista: (n1= luiz) (n2 = joao) (*outra_lista= maria, 1, 2, 3, 4) e Exemplo: ultmo_lista= 5

lista = ['luiz', 'joao', 'maria', 1, 2, 3, 4 ,5]

n1, n2, *outra_lista = lista

print(n1, n2, outra_lista)