print("=" * 30)

print("╭━━━╮  ╭╮      ╭╮     ╭╮")
print("┃╭━╮┃  ┃┃      ┃┃     ┃┃")
print("┃┃ ╰╋━━┫┃╭━━┳╮╭┫┃╭━━┳━╯┣━━┳━┳━━╮")
print("┃┃ ╭┫╭╮┃┃┃╭━┫┃┃┃┃┃╭╮┃╭╮┃╭╮┃╭┫╭╮┃")
print("┃╰━╯┃╭╮┃╰┫╰━┫╰╯┃╰┫╭╮┃╰╯┃╰╯┃┃┃╭╮┃")
print("╰━━━┻╯╰┻━┻━━┻━━┻━┻╯╰┻━━┻━━┻╯╰╯╰╯")

print("=" * 30)

#Escolha de equações

print("Qual equação")
print(" +   -   *   /   M")
print(" 1   2   3   4   5")

escolha = int(input())

print("=" * 30)

#Os Números escolhidos

print(" Digite dois números ")

print("=" * 30)

N1 = int(input("N1 =", ))
N2 = int(input("N2 =", ))

#Tipos de equações

Soma = N1 + N2
Menos = N1 - N2
Vezes = N1 * N2
Divisão = N1 // N2
Media = (N1 + N2) / 2

#Resultados

if escolha == 1:
    print("=" * 30)

    print("O Resultado é ", Soma)

    print("=" * 30)

if escolha == 2:
    print("=" * 30)

    print("O Resultado é ", Menos)

    print("=" * 30)

if escolha == 3:
    print("=" * 30)

    print("O Resultado é ", Vezes)

    print("=" * 30)

if escolha == 4:
    print("=" * 30)

    print("O Resultado é", Divisão)

    print("=" * 30)

if escolha == 5:
    print("=" * 30)

    print("A média é ", Media)

    print("=" * 30)