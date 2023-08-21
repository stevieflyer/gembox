import asyncio
from typing import List

from .async_task import AsyncTask
from .task_spliter import TaskSplitter


class ParallelAsyncRunner:
    @staticmethod
    async def _run_task_list(task_list: List[AsyncTask]):
        """
        Run a list of tasks sequentially.

        :param task_list: A list of tasks to run sequentially.
        :return: The results of the tasks.
        """
        results = []
        for task in task_list:
            try:
                result = await task.run()
                results.append(result)
            except Exception as e:
                print(f"Error while executing task: {e}")
                results.append(None)
        return results

    @classmethod
    async def _run_chunks(cls, tasks_lists: List[List[AsyncTask]]):
        """
        Run multiple lists of tasks in parallel, but each list is processed sequentially.

        :return: The results of the tasks.
        """
        return await asyncio.gather(*[cls._run_task_list(task_list) for task_list in tasks_lists])

    @classmethod
    async def run(cls, tasks: List[AsyncTask], n_workers: int = 1):
        """
        Run a list of tasks in parallel, but each list is processed sequentially.

        :param tasks: A list of tasks to run.
        :param n_workers: Number of workers to use.
        :return: The results of the tasks.
        """
        tasks_lists = TaskSplitter.split_evenly_by_weight(tasks, n_split=n_workers)
        return await cls._run_chunks(tasks_lists=tasks_lists)


__all__ = ["ParallelAsyncRunner"]

# TEST CODE
# async def example_task(name: str, duration: int):
#     print(f"Task {name} started, will run for {duration} seconds")
#     await asyncio.sleep(duration)
#     print(f"Task {name} completed after {duration} seconds")
#     return f"{name} done"
#
#
# def main():
#     tasks = [
#         AsyncTask(example_task, {"name": "A", "duration": 2}, weight_func=lambda x: x["duration"]),
#         AsyncTask(example_task, {"name": "B", "duration": 4}, weight_func=lambda x: x["duration"]),
#         AsyncTask(example_task, {"name": "C", "duration": 1}, weight_func=lambda x: x["duration"]),
#         AsyncTask(example_task, {"name": "D", "duration": 3}, weight_func=lambda x: x["duration"]),
#         AsyncTask(example_task, {"name": "E", "duration": 5}, weight_func=lambda x: x["duration"]),
#         AsyncTask(example_task, {"name": "F", "duration": 2}, weight_func=lambda x: x["duration"]),
#         AsyncTask(example_task, {"name": "G", "duration": 1}, weight_func=lambda x: x["duration"]),
#     ]
#
#     split_tasks = TaskSplitter.split_evenly_by_weight(tasks, n_split=3)
#     for idx, task_list in enumerate(split_tasks):
#         print(f"Worker {idx + 1} will run tasks: {[task.params['name'] for task in task_list]}")
#
#     results = ParallelAsyncRunner.run(tasks, n_workers=3)
#
#     for idx, worker_results in enumerate(results):
#         print(f"Worker {idx + 1} results: {worker_results}")
#
#
# if __name__ == "__main__":
#     main()
