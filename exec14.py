def get_user_address():
    address = input("Por favor informe o seu endereço:\n")
    return address

def remove_space(value_to_format):
    return value_to_format.replace(" ","")

def count_vogals(value_to_count):
    index = 0
    for letter in value_to_count:
        if letter.lower() in "aeiou":
            index += 1
    return index

def show_to_user(value_to_show):
    print(value_to_show)

def main():
    address = get_user_address()
    show_to_user(f"Você forneceu o seguinte endereço: {address}")

    address_without_space = remove_space(address)
    show_to_user(f"O seu endereço sem contabilizar espaços tem o total de {len(address_without_space)} caracteres")

    total_vogals = count_vogals(address_without_space)
    show_to_user(f"Seu endereço tem o total de {total_vogals} vogais")

main()
