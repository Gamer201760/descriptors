from datetime import datetime, timezone
from uuid import UUID

from domain.descriptor import Int, String
from domain.error import TaskIdValidationError, TaskStatusValidationError
from domain.task_status import TaskStatus


class Task:
    description = String(min_len=1)
    priority = Int(min_value=1)

    def __init__(
        self,
        id: str | UUID,
        description: str,
        priority: int,
        status: TaskStatus | str = TaskStatus.NEW,
        created_at: datetime | None = None,
    ) -> None:
        self._id = self._normalize_id(id)
        self.description = description
        self.priority = priority
        self.status = status
        self._created_at = self._normalize_created_at(created_at)

    @property
    def id(self) -> UUID:
        return self._id

    @property
    def status(self) -> TaskStatus:
        return self._status

    @status.setter
    def status(self, value: TaskStatus | str) -> None:
        self._status = self._normalize_status(value)

    @property
    def created_at(self) -> datetime:
        return self._created_at

    @property
    def is_ready(self) -> bool:
        return self._status is TaskStatus.NEW

    @staticmethod
    def _normalize_id(value: str | UUID) -> UUID:
        if isinstance(value, UUID):
            return value
        if isinstance(value, str):
            try:
                return UUID(value)
            except ValueError as err:
                raise TaskIdValidationError('id должно быть валидным UUID') from err
        raise TaskIdValidationError('id должно быть строкой UUID или UUID')

    @staticmethod
    def _normalize_status(value: TaskStatus | str) -> TaskStatus:
        if isinstance(value, TaskStatus):
            return value
        if isinstance(value, str):
            try:
                return TaskStatus(value)
            except ValueError as err:
                raise TaskStatusValidationError(
                    f'status должно быть одним из: {", ".join(item.value for item in TaskStatus)}'
                ) from err
        raise TaskStatusValidationError('status должно быть строкой или TaskStatus')

    @staticmethod
    def _normalize_created_at(value: datetime | None) -> datetime:
        if value is None:
            return datetime.now(timezone.utc)
        if isinstance(value, datetime):
            if value.tzinfo is None:
                raise ValueError('created_at должно быть timezone-aware datetime')
            return value
        raise TypeError('created_at должно быть datetime или None')
