COMMAND_NAME = 'change'

def input_error(func):
    def inner(*args, **kwargs):
        context = args[1]

        try:
            return func(*args, **kwargs)
        except IndexError as e:
            message = f'Invalid contact: {e}'

            return message, context, False
        except ValueError as e:
            message = f'Failed to update contact: {e}'

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

    if name not in context:
        raise IndexError("Contact not found.")

    if not phone.isdigit():
        raise ValueError("Invalid phone number")

    contact = {name: phone}

    message = "Contact updated."
    updated_context = {**context, **contact}

    return message, updated_context, stop