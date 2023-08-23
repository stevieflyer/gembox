import asyncio
import multiprocessing

from typing import List

from gembox.multiprocess.mp_async import Task
from gembox.multiprocess.mp_async.task_spliter import TaskSplitter


class ParallelExecutor:

    # @staticmethod
    # def _worker_tasks(tasks: List[Task]):
    #     # 新建一个事件循环来运行异步任务
    #     loop = asyncio.new_event_loop()
    #     asyncio.set_event_loop(loop)
    #
    #     # 在这个事件循环上运行所有的任务并收集结果
    #     results = loop.run_until_complete(asyncio.gather(*(task.run() for task in tasks)))
    #     loop.close()
    #
    #     return results

    @staticmethod
    def _worker_tasks(tasks: List[Task]):
        # 新建一个事件循环来运行异步任务
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        async def sequential_execution(tasks: List[Task]):
            results = []
            for task in tasks:
                result = await task.run()
                results.append(result)
            return results

        # 在这个事件循环上运行所有的任务并收集结果
        results = loop.run_until_complete(sequential_execution(tasks))
        loop.close()

        return results

    @classmethod
    async def run(cls, tasks: List[Task], n_workers: int = 1):
        # 使用 TaskSplitter 按权重均匀地划分任务
        split_tasks = TaskSplitter.split_evenly_by_weight(tasks, n_workers)

        with multiprocessing.Pool(n_workers) as pool:
            # 使用 map 方法来启动多个进程
            results = pool.map(cls._worker_tasks, split_tasks)

        # 将所有的结果从不同的进程合并到一个列表中
        all_results = [item for sublist in results for item in sublist]
        return all_results


__all__ = ["ParallelExecutor"]

# @deprecated
# import asyncio
# from typing import List
#
# from .task import Task
# from .task_spliter import TaskSplitter
#
#
# class ParallelAsyncRunner:
#     @staticmethod
#     async def _run_task_list(task_list: List[Task]):
#         """
#         Run a list of tasks sequentially.
#
#         :param task_list: A list of tasks to run sequentially.
#         :return: The results of the tasks.
#         """
#         results = []
#         for task in task_list:
#             try:
#                 result = await task.run()
#                 results.append(result)
#             except Exception as e:
#                 print(f"Error while executing task: {e}")
#                 results.append(None)
#         return results
#
#     @classmethod
#     async def _run_chunks(cls, tasks_lists: List[List[Task]]):
#         """
#         Run multiple lists of tasks in parallel, but each list is processed sequentially.
#
#         :return: The results of the tasks.
#         """
#         return await asyncio.gather(*[cls._run_task_list(task_list) for task_list in tasks_lists])
#
#     @classmethod
#     async def run(cls, tasks: List[Task], n_workers: int = 1):
#         """
#         Run a list of tasks in parallel, but each list is processed sequentially.
#
#         :param tasks: A list of tasks to run.
#         :param n_workers: Number of workers to use.
#         :return: The results of the tasks.
#         """
#         tasks_lists = TaskSplitter.split_evenly_by_weight(tasks, n_split=n_workers)
#         return await cls._run_chunks(tasks_lists=tasks_lists)
#
#
# __all__ = ["ParallelAsyncRunner"]

