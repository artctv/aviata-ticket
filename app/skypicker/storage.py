
class Storage():
    """Storage for data"""

        __shared_state = {
           'API': _API_URLS,
           'directions': _DIRECTIONS,
           'current_date': {},
           }

    __DIRECTIONS_NAMES = {
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

    _ENDPOINTS = {
       'search': r'https://api.skypicker.com/flights?{}',
          'url':
          'method': 'GET',
          'headers': {'Content-Type': 'application/json'}
       },
    }

    _ENDPOINT_METHODS = {
        'search': ('GET',)
    }

    _ENDPOINT_HEADERS = {
        'search':  {'Content-Type': 'application/json'}
    }

    _ENDPOINT_ARGS = {
        'search': {
            'fly_from': '',
            'fly_to': '',
            'date_from': '',
            'date_to': '',
        }
