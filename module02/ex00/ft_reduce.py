def ft_reduce(function_to_apply, iterable):
    """Apply function of two arguments cumulatively.
    Args:
        function_to_apply: a function taking an iterable.
        iterable: an iterable object (list, tuple, iterator).
    Returns:
        A value, of same type of elements in the iterable parameter.
        None if the iterable can not be used by the function.
    """
    if callable(function_to_apply) is False:
        raise TypeError("'{}' object is not callable"
                        .format(type(function_to_apply).__name__))
    try:
        iter(iterable)
    except TypeError as err:
        raise err
    if len(iterable) == 0:
        return None
    ret = iterable[0]
    for i in range(1, len(iterable)):
        ret = function_to_apply(ret, iterable[i])
    return ret
