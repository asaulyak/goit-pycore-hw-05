import importlib
import pkgutil
from . import commands

def load_commands():
    """
    Import all modules from `commands` and return a dictionary of command names to their functions.
    """
    imported_functions = {}

    for _, module_name, _ in pkgutil.iter_modules(commands.__path__):
        full_module_name = f"{commands.__name__}.{module_name}"
        try:
            module = importlib.import_module(full_module_name)
            if hasattr(module, 'run') and hasattr(module, 'COMMAND_NAME'):
                imported_functions[module.COMMAND_NAME] = module.run
            else:
                print(f"Module {full_module_name} does not have a run function or COMMAND_NAME.")
        except Exception as e:
            print(f"Failed to import {full_module_name}: {e}")

    return imported_functions

packages = load_commands()

def default_command(_, context):
    message = "Invalid command."
    stop = False

    return message, context, stop

def get_command(command_name):

    command = packages.get(command_name)

    if not command:
        return default_command

    return command

def parse_command(user_input):
    if not user_input:
        return 'not_a_command', []

    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()

    return cmd, *args