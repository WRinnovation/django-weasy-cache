import hashlib
import logging
try:
    from django.core.cache import caches
except ImportError:
    from diskcache import Cache as caches


logger = logging.getLogger(__name__)


# stringify function args
def join_(*args):
    rv = ""
    for _string in args:
        rv += ' ' + str(_string)
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


# define cache key structure
def cache_define_key(fn, override_key=None, override_key_for_self=None, *args, **kwargs):
    if override_key_for_self is not None:
        # use property of object - pulling out self as args[0]
        new_args = [getattr(args[0], override_key_for_self, override_key_for_self)] + list(args[1:]) if len(args) > 1 else [getattr(args[0], override_key_for_self, override_key_for_self)]
        key = cache_get_key(fn.__name__, new_args, **kwargs)
    elif override_key is not None:
        # use custom string
        key = cache_get_key(fn.__name__, [override_key], **{})
    else:
        # default - use mix of args and kwargs
        key = cache_get_key(fn.__name__, *args, **kwargs)
    return key


# get cache by its label - path
def get_cache(cache_label, use_diskcache=False):
    if not use_diskcache:
        return caches[cache_label]
    else:
        return caches(cache_label)


# decorator for caching functions
def cache_for(cache_label, time=None, override_key=None, override_key_for_self=None, use_diskcache=False):
    """
        :param cache_label: key for django cache
        :param time: timeout in seconds
        :param override_key: if not None defines cache key
        :param override_key_for_self: if not None defines self properties as first part of cache key
        :param use_diskcache: if True uses diskcache lib instead of django cache framework
        :return: result of decorated function
        """
    def decorator(fn):
        def wrapper(*args, **kwargs):
            cache = get_cache(cache_label, use_diskcache)
            key = cache_define_key(fn, override_key, override_key_for_self, *args, **kwargs)
            result = cache.get(key)
            if result is None:
                result = fn(*args, **kwargs)
                cache.set(key, result, time) if time is not None else cache.set(key, result)
                print('Cache {} set {}'.format(cache_label, join_(*args)))
            else:
                print('Cache {} hit {}'.format(cache_label, join_(*args)))
            return result

        return wrapper

    return decorator



