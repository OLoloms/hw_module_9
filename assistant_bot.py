#Dictionary for saving information 
information = {} 

def input_error(func):
    """Decorator function which handles exception"""
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError as e:
            return e
        except IndexError as e:
            return e
        except ValueError as e:
            return e
        except:
            print('Oops! Something has going wrong! Try one more time')
    return inner

def hello():
    """Handler function which says hello to the user"""
    return "How can I help you?"

@input_error
def add(input_information: str) -> str:
    """Handler function which adds information about user (name, phone number) to dictionary"""
    # input_information = input('Enter information: ') 
    name, phone = input_information.split(' ')
    information[name] = phone
    return 'Record is added'

@input_error
def change(input_information: str) -> dict:
    """Handler function which changes information about user in dictionary"""
    # name = input('Enter name: ')
    # phone = input('Enter phone number: ')
    name, phone = input_information.split(' ')
    information[name] = phone
    return 'Record is changed'

@input_error
def phone(input_name) -> str:
    """Handler function which shows information by name"""
    # input_name = input('Enter name: ')
    return information.get(input_name, 'Record is not found')

@input_error
def show_all() -> dict:
    """Handler function which shows all information that contains in dictionary"""
    return information

#Dictionary for carrying
COMMANDS = {
    'hello': hello,
    'add': add,
    'change': change,
    'phone': phone,
    'show_all': show_all
}

words_for_break = ["good bye", "close", "exit"]

def main():
    """Main function in which interaction with the user takes place"""
    while True:
        try:
            answer = input().lower()
            if answer in words_for_break:
                print('Good bye!')
                break
            if answer == 'show_all' or answer == 'hello':
                command = COMMANDS[answer]
                print(command())
            elif answer == 'add' or answer == 'change':
                input_information = input('Enter information: ')
                command = COMMANDS[answer]
                print(command(input_information))
            else:
                raise ValueError
        except ValueError:
            print('Incorrect command')
            continue


if __name__ == '__main__':
    main()