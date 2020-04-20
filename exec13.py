def get_user_data():
    full_name = input("Forneça seu nome completo:\n")
    return full_name.split()

def show_formatted_name(name, last_name):
    print(f"Nome: {name.title()} - Sobrenome: {last_name.title()}")

def main():
    name, last_name = get_user_data()
    show_formatted_name(name, last_name)

if __name__ == "__main__":
    main()
