def function_with_uncommon_error_solution(x):
    try:
        return 1 / x
    except ZeroDivisionError:
        return float('inf')  # Or handle the error differently, like returning a default value