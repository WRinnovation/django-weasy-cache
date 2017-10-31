import hashlib
import logging
from django.core.cache import caches

logger = logging.getLogger(__name__)


# stringify function args
def join_(*args):
    rv = ""
    for _string in args:
        rv += ' ' + _string
    return rv.lstrip()


# get cache key for storage
def cache_get_key(*args, **kwargs):
    serialise = []
    for arg in args:
        serialise.append(str(arg))
    for key, arg in kwargs.items():
        serialise.append(str(key))
        serialise.append(str(arg))
    key = hashlib.md5("".join(serialise).encode('utf-8')).hexdigest()
    return key


# decorator for caching functions
def cache_for(cache_label, time=None):
    def decorator(fn):
        def wrapper(*args, **kwargs):
            cache = caches[cache_label]
            key = cache_get_key(fn.__name__, *args, **kwargs)
            result = cache.get(key)
            if not result:
                result = fn(*args, **kwargs)
                cache.set(key, result, time)
                logger.debug('Cache {} set {}'.format(cache_label, join_(*args)))
            else:
                logger.debug('Cache {} hit {}'.format(cache_label, join_(*args)))
            return result

        return wrapper

    return decorator
