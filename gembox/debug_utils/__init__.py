from .debug_utils import (
    Debugger,
    FileDebugger,
    ConsoleDebugger,
    FileConsoleDebugger,
)
'''
class Debugger:
    """
    Debugger class for logging and debugging.

    This class is a wrapper of `logging.Logger` class. But it provides more.

    When instantiating a `Debugger`, if a `name` is provided, the Debugger will be attached to a logger with the given
    name. Otherwise, a random name will be generated so that different Debugger won't interfere with each other.
    """
    def debug(self, msg):
        self._logger.debug(msg)

    def info(self, msg):
        self._logger.info(msg)

    def warn(self, msg):
        self._logger.warning(msg)
    ...
'''