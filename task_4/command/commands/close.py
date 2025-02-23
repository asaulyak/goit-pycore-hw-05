COMMAND_NAME = "close"

def run(_, context):
    message = "Good bye!"
    updated_context = context
    stop = True

    return message, updated_context, stop