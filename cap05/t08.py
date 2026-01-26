# Boas práticas: Aprendendo a documentar:

def somar(a:float, b:float):
    """Função que realiza a soma entre dois valores (a e b do tipo float) e retorna um valor."""
    return a + b
    
print(f"Chamando o método doc para ler a documentação: {somar.__doc__}")

print(f"Chamando a função help para ler a documentação: {help(somar)}")


