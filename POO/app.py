from modelos.restaurante import Restaurante

Restaurante_praca = Restaurante('Restaurante da Praça', 'Gourmet')
# Restaurante_praca.receber_avaliacao('Gui', 10)
# Restaurante_praca.receber_avaliacao('Lucas', 9)
# Restaurante_praca.receber_avaliacao('Luan', 8)
# restaurante_mexicano = Restaurante('Mexican Food', 'Mexicano')
# restaurante_japones = Restaurante('Japa', 'Japa')

# restaurante_mexicano.alternar_estado()

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()