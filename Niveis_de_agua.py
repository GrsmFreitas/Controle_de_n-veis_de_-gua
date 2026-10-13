from colorama import Fore, Style
nivel = int(input("Qual é o nível atual do reservatório (1 a 5)? "))
niveis = [1, 2, 3, 4, 5]
# indice  0, 1, 2, 3, 4

for a in range(1):
    
    if nivel == niveis[0]:
        print(Fore.RED + "Nível 1: Muito baixo (crítico)!")
    if nivel == niveis[1]:
        print(Fore.YELLOW + "Nível 2: Baixo")
    if nivel == niveis[2]:
        print(Fore.GREEN + "Nível 3: Médio")
    if nivel == niveis[3]:
        print(Fore.CYAN + "Nível 4: Alto")
    if nivel == niveis[4]:
         print(Fore.BLUE + "Nível 5: Muito alto (alerta)")

print(Style.RESET_ALL)