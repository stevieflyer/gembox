from typing import List

from .task import Task


class TaskSplitter:
    @staticmethod
    def split_by_max(tasks: List[Task], max_weight_per_partition: int) -> List[List[Task]]:
        """
        Partition the given tasks into groups based on a maximum weight constraint.

        Each group of tasks will have a combined weight that is less than or equal
        to the specified `max_weight_per_partition`. Tasks are added to a group
        sequentially until the weight constraint is reached.

        :param tasks: List of tasks to partition.
        :param max_weight_per_partition: Maximum combined weight for each group of tasks.
        :return: A list of task groups where each group respects the weight constraint.
        """
        partitions = []
        current_partition = []
        accumulated_weight = 0

        for task in tasks:
            if accumulated_weight + task.weight <= max_weight_per_partition:
                current_partition.append(task)
                accumulated_weight += task.weight
            else:
                partitions.append(current_partition)
                current_partition = [task]
                accumulated_weight = task.weight

        # Appending any remaining tasks.
        if current_partition:
            partitions.append(current_partition)

        return partitions

    @staticmethod
    def split_evenly_by_weight(tasks: List[Task], n_split: int) -> List[List[Task]]:
        """
        Partition the tasks into a specified number of groups based on their weights, distributing weights as evenly as possible.

        TODO: This method has O(n log(n) + n * m) time complexity, where n is the number of tasks and m is the number of partitions, this should be optimized later.

        :param tasks: List of tasks to partition.
        :param n_split: Number of desired partitions.
        :return: A list containing `num_partitions` groups of tasks.
        """
        # Sort the tasks by weight, so we can distribute the larger tasks first
        sorted_tasks = sorted(tasks, key=lambda task: task.weight, reverse=True)

        partitions = [[] for _ in range(n_split)]
        partition_weights = [0] * n_split

        for task in sorted_tasks:
            # Find the partition with the least weight
            lightest_partition_idx = partition_weights.index(min(partition_weights))
            partitions[lightest_partition_idx].append(task)
            partition_weights[lightest_partition_idx] += task.weight

        return partitions

    @staticmethod
    def split_evenly_by_count(tasks: List[Task], num_partitions: int) -> List[List[Task]]:
        """
        Partition the tasks into a specified number of groups, distributing tasks as evenly as possible.

        :param tasks: List of tasks to partition.
        :param num_partitions: Number of desired partitions.
        :return: A list containing `num_partitions` groups of tasks.
        """
        partitions = [[] for _ in range(num_partitions)]

        for i, task in enumerate(tasks):
            partitions[i % num_partitions].append(task)

        return partitions


__all__ = ["TaskSplitter"]
