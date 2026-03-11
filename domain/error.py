class TaskError(Exception):
    """Базовая ошибка доменной модели задачи"""


class TaskValidationError(TaskError):
    """Ошибка валидации атрибута задачи"""


class StringValidationError(TaskValidationError):
    """Ошибка валидации строкового атрибута"""
