# -*- coding: utf-8 -*-
import asyncio
from .decorator import decorate
from .assertions import assert_corofunction


@decorate
def partial(coro, *args, **kw):
    """
    Partial function implementation designed
    for coroutines, allowing variadic input arguments.

    This function can be used as decorator.

    arguments:
        coro (coroutinefunction): coroutine function to wrap.
        *args (mixed): mixed variadic arguments for partial application.

    Raises:
        TypeError: if ``coro`` is not a coroutine function.

    Returns:
        coroutinefunction

    Usage::

        task = paco.partial(coro, 1, foo='bar')
        await task(2, bar='foo')
    """
    assert_corofunction(coro=coro)

    @asyncio.coroutine
    def wrapper(*_args, **_kw):
        call_args = args + _args
        kw.update(_kw)
        return (yield from coro(*call_args, **kw))

    return wrapper
