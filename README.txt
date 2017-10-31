===========
Django WEasy Cache
===========

Django WEasy Cache provides very simple cache decorator
it most useful for tasks involving <x> and also <y>. Typical usage
often looks like this::

    from djangoweasycache import cache_for

    @cache_for(cache_label='long_api_call', time=500)
    def long_api_call(region_slug):
	    result = api.call(region_slug)
	    return result

