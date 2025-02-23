COMMAND_NAME = "hello"

def run(_, context):
    message = "How can I help you?"
    updated_context = context
    stop = False

    return message, updated_context, stop