#Functions with outputs
#Docstring
def format_name(f_name, l_name):
    """Pega o primeiro nome e o ultimo nome e formata isso retornando com title case do nome completo."""
    if f_name == "" or l_name == "":
        return "Nenhum valor encontrado"
    else:
        formated_f_name = f_name.title()
        formated_l_name = l_name.title()
        return f"Result: {formated_f_name} {formated_l_name}"

#Posso verificar o que a função irá fazer deixando o mouse em cima do call
print(format_name(
    input("Qual seu primeiro nome?"), 
    input("Qual seu segundo nome?")))
