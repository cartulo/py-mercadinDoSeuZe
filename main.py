# -*- coding: utf-8 -*-
import math
try:
    print("Seu Zé: Quantas maçãs vai querer?")
    print("Todas 30 centavu, acima de 12 é 25 centavo.")
    num = float(input("Você: Vou querer levar "))

    if num >= 12:
        resultado = num * 0.25
        print("================================================")
        print("A compra deu: R${0: .2f}".format(resultado))
        print("================================================")
        input("Pressione qualquer tecla para sair.")

    else:
        resultado = num * 0.3
        print("================================================")
        print("A compra deu: R${0: .2f}".format(resultado))
        print("================================================")
        input("Pressione qualquer tecla para sair.")

except (TypeError, NameError, SyntaxError, ValueError):
    print("================================================")
    print("Apenas números são aceitos")
    print("================================================")
    input("Pressione qualquer tecla para sair.")