'''
    Доробіть консольного бота помічника з попереднього домашнього завдання та 
    додайте обробку помилок за допомоги декораторів.

    Вимоги до завдання:

    Всі помилки введення користувача повинні оброблятися за допомогою декоратора 
    input_error. Цей декоратор відповідає за повернення користувачеві повідомлень 
    типу "Enter user name", "Give me name and phone please" тощо.
    Декоратор input_error повинен обробляти винятки, що виникають у функціях - 
    handler і це винятки: KeyError, ValueError, IndexError. Коли відбувається 
    виняток декоратор повинен повертати відповідну відповідь користувачеві. 
    Виконання програми при цьому не припиняється.
'''

def input_error(func):
    """
    Decorator function to handle input errors.
    """
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        
        except KeyError:
            return 'Error: Key not found.'
        except ValueError:
            return 'Error: Invalid input format. Please provide the correct argument(s).'
        except IndexError:
            return 'Error: Insufficient arguments. Please provide the correct argument(s).'
        except Exception as e:
            return f'Error: {str(e)}. Please check your input and try again.'
        
    return inner

@input_error
def parse_input(user_input: str) -> tuple[str, ...]:
    """
    Parse user input and return a tuple with command and arguments.
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args: tuple[str, str], contacts: dict[str, str]) -> str:
    """
    Add a new contact to the contacts dictionary.
    """
    name, phone = args
    if name in contacts:
        return f"Contact '{name}' already exists. Use 'change' command to update."
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args: tuple[str, str], contacts: dict[str, str]) -> str:
    """
    Update a contact in the contacts dictionary.
    """
    name, phone = args
    if name not in contacts:
        return f"Contact '{name}' not found. Use 'add' command to create a new contact."
    contacts[name] = phone
    return "Contact updated."

@input_error
def show_phone(args: tuple[str], contacts: dict[str, str]) -> str:
    """
    Show the phone number of a contact.
    """
    name = args[0]
    return contacts.get(name, "The name wasn`t found.")

@input_error    
def show_all(contacts: dict[str, str]) -> dict[str, str]:
    return contacts   

def main():
    """
    Main function to interact with the assistant bot.
    """
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        
        if command in ['close', 'exit']:
            print("Good Bye!")
            break    
        elif command == 'hello':
            print("How can i help you?")
        elif command == 'add':
            print(add_contact(args, contacts))
        elif command == 'change':
            print(change_contact(args, contacts))
        elif command == 'phone':
            print(show_phone(args, contacts))
        elif command == 'all':
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == '__main__':
    main()