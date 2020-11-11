from app.main import WrongStorageMethod, ValueNotInStorage


class Storage():
    """Storage for data"""

    _storage = {}

    _DIRECTIONS_NAMES = {
         'ALA': 'Алматы',
         'TSE': 'Астана',
         'MOW': 'Москва',
         'LED': 'С-Петербург',
         'CIT': 'Шымкент',
    }

    _DIRECTIONS = (
        ('ALA','TSE'),
        ('TSE', 'ALA'),
        ('ALA', 'MOW'),
        ('MOW', 'ALA'),
        ('ALA', 'CIT'),
        ('CIT', 'ALA'),
        ('TSE', 'MOW'),
        ('MOW', 'TSE'),
        ('TSE', 'LED'),
        ('LED', 'TSE'),
    )

    _DATE_FORMAT = r'%d/%m/%Y'

    _ENDPOINT_CORE = r'https://api.skypicker.com'

    _ENDPOINT_NAMES = (
        'search',
    )

    _ENDPOINT_URLS = {
       'search': r'flights',
    }

    _ENDPOINT_METHODS = {
        'search': ('GET',)
    }

    _ENDPOINT_HEADERS = {
        'search':  {'Content-Type': 'application/json'}
    }

    _ENDPOINT_ARGS = {
        'search': ('fly_from','fly_to','date_from','date_to',),
    }

    _DATA_MAP = {
        'endpoint': _ENDPOINT_URLS,
        'methods': _ENDPOINT_METHODS,
        'headers': _ENDPOINT_HEADERS,
        'args': _ENDPOINT_ARGS,
    }

    _DATA_VARIOUS = {
        'directions': _DIRECTIONS,
        'date_format': _DATE_FORMAT,
    }

    def _check_data(self, data):
        if data in self._ENDPOINT_NAMES:
            return True
        else:
            return False

    def _check_attr(self, data):
        if hasattr(self, data):
            return True
        else:
            return False

    def _before_get(func):
        def wrapper(self, *args):
            data = func(self, *args)
            data['core'] = self._ENDPOINT_CORE
            data['date_format'] = self._DATE_FORMAT
            return data
        return wrapper

    @_before_get
    def _get_special(self, type_, data):
        obj = _DATA_MAP.get(type_)
        return obj.get(data)

    @_before_get
    def _get_all(self, data):
        list_ = []
        for key, obj in self._DATA_MAP.items():
            value = obj.get(data)
            list_.append((key, value))
        dict_ = {value[0]:value[1] for value in list_}
        list_.clear()

        return dict_

    def get_data(self, data, type_=None):
        if self._check_data(data):
            if type_ is None:
                return self._get_all(data)
            else:
                return self._get_special(type_, data)
        elif self._check_attr(data):
            return getattr(self, data)
        else:
            raise NameError()


    def get_various(self, type_):
        if type_ in self._DATA_VARIOUS:
            return self._DATA_VARIOUS.get(type_)
        else:
            return NameError()



    def handle_storage(self, type_, **kwargs):
        __l = locals()
        __methods = tuple(filter(lambda f: True if '_data' in f else False, locals().keys()))
        __funcs = tuple(map(lambda f: __l.get(f), __methods))
        __methods = tuple(map(lambda f: f.split('_')[1], __methods))
        map_ = dict(zip(__methods, __funcs))
        del __methods; del __funcs; del __l;

        def _get_data(self):
            pass

        def _set_data(self):
            pass

        def _update_data(self):
            pass

        def _del_data(self):
            pass

        if type_ not in map_.keys():
            raise WrongStorageMethod()
        else:
            map_.get(type_).__call__()



if __name__ == '__main__':
    k = Storage()
    k.handle_storage(None)
