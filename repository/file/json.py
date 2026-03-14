from pathlib import Path

from domain.task import Task


class TaskJsonSource:
    def __init__(self, path: Path | str) -> None:
        self._path = Path(path)

    def get_tasks(self) -> list[Task]:
        raise NotImplementedError(
            'TaskJsonSource.get_tasks временно отключен: JSON-репозиторий '
            'находится в миграции к новой схеме Task'
        )
