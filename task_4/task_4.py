from command import parser

def task_4():
    contacts = {}

    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        cmd, *args = parser.parse_command(user_input)

        command = parser.get_command(cmd)

        message, updated_context, stop = command(args, contacts)

        contacts = updated_context

        print(message)

        if stop:
            break

def main():
    task_4()

if __name__ == "__main__":
    main()