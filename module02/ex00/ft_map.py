def ft_map(function_to_apply, iterable):
    """Map the function to all elements of the iterable.
    Args:
        function_to_apply: a function taking an iterable.
        iterable: an iterable object (list, tuple, iterator).
    Returns:
        An iterable.
        None if the iterable can not be used by the function.
    """
    try:
        iter(iterable)
    except TypeError as err:
        raise err
    if callable(function_to_apply) is False:
        raise TypeError("'{}' object is not callable"
                        .format(type(function_to_apply).__name__))
    for elem in iterable:
        yield function_to_apply(elem)
