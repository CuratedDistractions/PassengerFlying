import logging

# Create a logger object
logger = logging.getLogger(__name__)


class Globals:
    __instance__ = None

    def __init__(self):
        """ Constructor."""

        if Globals.__instance__ is None:
            Globals.__instance__ = self
        else:
            return Globals.__instance__

    @staticmethod
    def get_instance():
        """ Static method to fetch the current instance."""

        if not Globals.__instance__:
            return Globals()
        return Globals.__instance__

    def __getattr__(self, name):
        logger.warning("Variable {} doesn't exist yet".format(name))
        return None


globals_list = Globals.get_instance()
