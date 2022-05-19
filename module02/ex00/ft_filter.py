def ft_filter(function_to_apply, iterable):
    """Filter the result of function apply to all elements of the iterable.
    Args:
        function_to_apply: a function taking an iterable.
        iterable: an iterable object (list, tuple, iterator).
    Returns:
        An iterable.
        None if the iterable can not be used by the function.
    """
    if function_to_apply is None:
        for elem in iterable:
            if elem:
                yield elem
    else:
        for elem in iterable:
            if function_to_apply(elem):
                yield elem
