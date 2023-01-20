import typing as t

import hikari
import functools

P = t.ParamSpec("P")
T = t.TypeVar("T")


def consume_event(callback: t.Callable[P, T]) -> t.Callable[t.Concatenate[hikari.Event, P], T]:
    @functools.wraps(callback)
    def inner(_: hikari.Event, *args: P.args, **kwargs: P.kwargs) -> T:
        return callback(*args, **kwargs)

    return inner
