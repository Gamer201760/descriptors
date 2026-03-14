from domain.task import Task


class MockExternalSource:
    def get_tasks(self) -> list[Task]:
        raise NotImplementedError(
            'MockExternalSource.get_tasks временно отключен: источник-мок '
            'ожидает обновления под новую схему Task'
        )
