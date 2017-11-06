# django-weasy-cache
Simple django cache decorator ready to use linke this:

## Install

pip install -U git+https://github.com/WRinnovation/django-weasy-cache.git

## Example

```
from djangoweasycache import cache_for

....

# very long task
@cache_for('my_fibonacci_task', time=60)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

>>> print([fib(n) for n in range(16)])
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
```

Set default_time to **True** if want to use timeout defined in Django settings:

```
@cache_for('my_fibonacci_task', default_time=True)
```