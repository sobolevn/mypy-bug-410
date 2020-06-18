from typing import Generic, TypeVar

from returns.curry import curry

_ValueType = TypeVar('_ValueType')


class Result(Generic[_ValueType]):
    @classmethod
    def from_value(self, inner_value: _ValueType) -> 'Result[_ValueType]':
        return Result(inner_value)


# Works correctly:

@curry
def first(a: int, b: int) -> int:
    ...

reveal_type(first)
reveal_type(
    Result.from_value(first),
)


# Fails:

@curry
def second(a: int, b: int, c: int) -> int:
    ...

reveal_type(second)
reveal_type(
    Result.from_value(second),
)
