from random import Random

from domain.task import Task


class RandomJobsSource:
    def __init__(self, rnd: Random) -> None:
        self._rnd = rnd

    def get_tasks(self) -> list[Task]:
        raise NotImplementedError(
            'RandomJobsSource.get_tasks временно отключен: генератор задач '
            'ожидает обновления под новую схему Task'
        )
