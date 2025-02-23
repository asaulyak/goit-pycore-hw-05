COMMAND_NAME = 'all'

def run(_, context):

    message = str(context)
    updated_context = context
    stop = False

    return message, updated_context, stop