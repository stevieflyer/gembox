import asyncio
import multiprocessing

from typing import List

from gembox.multiprocess.task import Task
from gembox.multiprocess.task_spliter import TaskSplitter


class ParallelExecutor:
    @staticmethod
    def _worker_tasks(tasks: List[Task]):
        # 新建一个事件循环来运行异步任务
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        async def sequential_execution(_tasks: List[Task]):
            _results = []
            for task in _tasks:
                result = await task.run()
                _results.append(result)
            return _results

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
