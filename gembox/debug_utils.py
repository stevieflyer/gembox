import uuid
import logging


DEFAULT_LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'


def debug_decorator(action):
    async def wrapper(self, selector, *args, **kwargs):
        self.debug_tool.info(f'{action}ing {selector}...')
        result = await action(self, selector, *args, **kwargs)
        self.debug_tool.info(f'{selector} {action}ed successfully')
        return result
    return wrapper


def get_file_handler(filepath, fmt=DEFAULT_LOG_FORMAT, encoding: str = 'utf-8') -> logging.FileHandler:
    file_handler = logging.FileHandler(filename=filepath, encoding=encoding)
    formatter = logging.Formatter(fmt)
    file_handler.setFormatter(formatter)
    return file_handler


def get_console_handler(fmt=DEFAULT_LOG_FORMAT) -> logging.StreamHandler:
    console_handler = logging.StreamHandler()
    formatter = logging.Formatter(fmt)
    console_handler.setFormatter(formatter)
    return console_handler


class Debugger:
    """
    Debugger class for logging and debugging.

    This class is a wrapper of `logging.Logger` class. But it provides more.

    When instantiating a `Debugger`, if a `name` is provided, the Debugger will be attached to a logger with the given
    name. Otherwise, a random name will be generated so that different Debugger won't interfere with each other.
    """
    def __init__(self, name=None, level=logging.WARNING):
        """
        :param name: (Optional) name of the logger, providing it when you want to attach to a shared logger.
        :param level: (Optional) minimum logging level
        """
        self._name = name if name is not None else f"{__name__}_{uuid.uuid4().hex[:4]}_logger"
        self._logger = logging.getLogger(self._name)
        # Clear existing handlers
        self._logger.handlers = []
        # Basic configuration
        logging.basicConfig(format=DEFAULT_LOG_FORMAT)
        self._logger.setLevel(level)
        # Prevent log propagation to higher-level loggers
        self._logger.propagate = False

    @property
    def name(self):
        return self._name

    @property
    def logger(self):
        return self._logger

    def enable_debug(self):
        self._logger.setLevel(logging.DEBUG)

    def disable_debug(self):
        self._logger.setLevel(logging.WARNING)

    def silence(self):
        self._logger.setLevel(logging.CRITICAL)

    def log(self, msg):
        self._logger.debug(msg)

    def debug(self, msg):
        self._logger.debug(msg)

    def info(self, msg):
        self._logger.info(msg)

    def warn(self, msg):
        self._logger.warning(msg)

    def error(self, msg):
        self._logger.error(msg)

    def critical(self, msg):
        self._logger.critical(msg)


class FileDebugger(Debugger):
    def __init__(self, name=None, level=logging.WARNING, filepath="debug.log"):
        super().__init__(name=name, level=level)
        self._filepath = filepath
        self._logger.addHandler(get_file_handler(filepath))

    @property
    def filepath(self):
        return self._filepath


class ConsoleDebugger(Debugger):
    def __init__(self, name=None, level=logging.WARNING):
        """
        :param name: (str) name of the logger, providing it when you wanna attach to a shared logger.
        :param level: (int) minimum logging level
        """
        super().__init__(name=name, level=level)
        self._logger.addHandler(get_console_handler())


class FileConsoleDebugger(Debugger):
    def __init__(self, filepath, name=None, level=logging.WARNING):
        """
        :param filepath: (str | pathlib.Path) path to the log file
        :param name: (str) name of the logger, providing it when you wanna attach to a shared logger.
        :param level: (int) minimum logging level
        """
        super().__init__(name=name, level=level)
        self._filepath = filepath
        self._logger.addHandler(get_file_handler(filepath))
        self._logger.addHandler(get_console_handler())

    @property
    def filepath(self):
        return self._filepath


__all__ = ["Debugger", "FileDebugger", "ConsoleDebugger", "FileConsoleDebugger"]
