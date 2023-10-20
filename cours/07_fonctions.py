print("\n")

# affiche bonjour en espagnol...
def print_hola(prenom, date = "01/01/1970"):
    print(f"Hola {prenom} - {date} !")

def format_hola(prenom: str, date: str = "01/01/1970") -> str:
    return f"Hola {prenom} - {date} !"

print_hola(date="19/10/2023", prenom="Kevin")
print(format_hola(prenom="Mike"))

print(format_hola)