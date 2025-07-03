from typing import Callable


def cache(func: Callable) -> Callable:
    result_func_dict = {}

    def wrapper(*args, **kwargs) -> None:
        key = (func, args, tuple(sorted(kwargs.items())))
        if key in result_func_dict:
            result = result_func_dict[key]
            print("Getting from cache")
            return result
        else:
            result = func(*args, **kwargs)
            result_func_dict[key] = result
            print("Calculating new result")
            return result
    return wrapper
