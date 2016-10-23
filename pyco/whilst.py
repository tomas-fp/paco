# -*- coding: utf-8 -*-
import asyncio
from .filter import assert_true
from .assertions import assert_corofunction


@asyncio.coroutine
def whilst(coro, coro_test, assert_coro=None, *args, **kw):
    """
    Repeatedly call `coro` coroutine function while `coro_test` returns `True`.

    This function is the inverse of `pyco.until()`.

    This function is a coroutine.

    Arguments:
        coro (coroutinefunction): coroutine function to execute.
        coro_test (coroutinefunction): coroutine function to test.
        assert_coro (coroutinefunction): optional assertion coroutine used
            to determine if the test passed or not.
        *args (mixed): optional variadic arguments to pass to `coro` function.

    Raises:
        TypeError: if input arguments are invalid.

    Returns:
        list: result values returned by `coro`.

    Usage::

        await pyco.whilst(coro, [1, 2, 3, 4, 5])
    """
    assert_corofunction(coro=coro, coro_test=coro_test)

    # Store yielded values by coroutine
    results = []

    # Set assertion coroutine
    assert_coro = assert_coro or assert_true

    # Execute coroutine until a certain
    while (yield from assert_coro((yield from coro_test()))):
        results.append((yield from coro(*args, **kw)))

    return results
