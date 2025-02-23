COMMAND_NAME = 'add'

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            message = f'Failed to add contact: {e}'
            context = args[1]

            return message, context, False

    return inner

@input_error
def run(args, context):
    stop = False

    if len(args) < 2:
        raise ValueError("Give me name and phone please.")

    name, phone = args

    if not name or not phone:
        raise ValueError("Give me name and phone please.")

    if not name.isalpha():
        raise ValueError("Invalid name.")

    if not phone.isdigit():
        raise ValueError("Invalid phone number.")

    contact = {name: phone}

    message = "Contact added."
    updated_context = {**context, **contact}

    return message, updated_context, stop
