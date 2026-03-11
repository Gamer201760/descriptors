from domain.error import StringValidationError


class String:
    def __init__(self, min_len: int = 1, max_len: int | None = None) -> None:
        self._min_len = min_len
        self._max_len = max_len

    def __set_name__(self, owner: type, name: str) -> None:
        self._attr = '_' + name

    def __get__(self, obj: object | None, objtype: type | None = None) -> object:
        if obj is None:
            return self
        return getattr(obj, self._attr)

    def __set__(self, obj: object, value: object) -> None:
        if not isinstance(value, str):
            raise StringValidationError(f'{self._attr[1:]} должно быть строкой')

        if self._max_len is not None and len(value) > self._max_len:
            raise StringValidationError(
                f'{self._attr[1:]} не должно превышать {self._max_len} символов'
            )

        if len(value) < self._min_len:
            raise StringValidationError(
                f'{self._attr[1:]} должно быть не менее {self._min_len} символов'
            )

        setattr(obj, self._attr, value)
