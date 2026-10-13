from colorama import Fore, Style
nivel = int(input("Qual é o nível atual do reservatório (1 a 5)? "))

for a in range(1):
    
    if nivel == 1:
        print(Fore.RED + "Nível 1: Muito baixo (crítico)!")
    if nivel == 2:
        print(Fore.YELLOW + "Nível 2: Baixo")
    if nivel == 3:
        print(Fore.GREEN + "Nível 3: Médio")
    if nivel == 4:
        print(Fore.CYAN + "Nível 4: Alto")
    if nivel ==5:
         print(Fore.BLUE + "Nível 5: Muito alto (alerta)")

print(Style.RESET_ALL)