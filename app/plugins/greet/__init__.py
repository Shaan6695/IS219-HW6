import logging
from app.commands import Command


class GoodbyeCommand(Command):
    def execute(self):
        logging.info("Hello!")
        print("Hello!")