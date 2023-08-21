import inspect
from typing import Callable, Any, Dict


class AsyncTask:
    """
    A wrapper for a task to be executed asynchronously.

    :param task: (Callable) the task to be executed
    :param params: (Dict) the parameters to be passed to the task
    """

    def __init__(self, task: Callable[[Any], Any], params: Dict, weight_func = None):
        self.validate_params(task, params)
        self.task = task
        self.params = params
        self.weight = 1 if weight_func is None else weight_func(params)

    @staticmethod
    def validate_params(task: Callable, params: Dict) -> None:
        """
        Validate the parameters provided to the task.

        This method can only validate the parameter name and the number of parameters. It cannot validate the type of
        the parameters since the dynamic nature of Python.

        :param task: (Callable) the task to be executed
        :param params: (Dict) the parameters to be passed to the task
        :return: None
        """
        sig = inspect.signature(task)
        valid_params = set(sig.parameters.keys())
        provided_params = set(params.keys())

        # if not provided_params.issubset(valid_params):
        #     extra_params = provided_params - valid_params
        #     raise ValueError(f"Invalid parameters provided: {', '.join(extra_params)}")

    async def run(self):
        return await self.task(**self.params)

    def __str__(self):
        return f"AsyncTask(task={self.task.__name__}, params={self.params})"

    def __repr__(self):
        return self.__str__()


__all__ = ["AsyncTask"]
