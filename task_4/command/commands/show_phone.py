COMMAND_NAME = 'phone'

def input_error(func):
    def inner(*args, **kwargs):
        context = args[1]

        try:
            return func(*args, **kwargs)
        except IndexError as e:
            message = f'Invalid contact: {e}'

            return message, context, False
        except KeyError as e:
            message = f'Invalid phone: {e}'

            return message, context, False
        except ValueError as e:
            message = f'Failed to get contact: {e}'

            return message, context, False

    return inner

@input_error
def run(args, context):
    if len(args) < 1:
        raise ValueError("Give me phone please.")

    contact = args[0]
    updated_context = context
    stop = False

    if not contact:
        raise IndexError("Contact not found.")

    phone = context.get(contact)

    if not phone:
        raise KeyError("Phone not found.")
    else:
        message = str(phone)

    return message, updated_context, stop