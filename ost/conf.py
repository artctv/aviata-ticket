from datetime import datetime

class Config:
   '''Config class.'''

   __DIRECTIONS_NAMES = {
        'ALA': 'Алматы',
        'TSE': 'Астана',
        'MOW': 'Москва',
        'LED': 'С-Петербург',
        'CIT': 'Шымкент',
   }

   _DIRECTIONS = {
      'ALA': 'TSE',
      'TSE': 'ALA',
      'ALA': 'MOW',
      'MOW': 'ALA',
      'ALA': 'CIT',
      'CIT': 'ALA',
      'TSE': 'MOW',
      'MOW': 'TSE',
      'TSE': 'LED',
      'LED': 'TSE',
   }

   _API_URLS = {
      'search': {
         'url': r'https://api.skypicker.com/flights?{}',
         'method': 'GET',
         'headers': {'Content-Type': 'application/json'}
      },
   }

   _ARGS_REQUEST = {
      'fly_from': '',
      'fly_to': '',
      'date_from': '',
      'date_to': '',
   }

   __shared_state = {
      'API': _API_URLS,
      'directions': _DIRECTIONS,
      'current_date': {},
      }


   def __init__(self):
      self.__dict__ = self.__shared_state
      self._date_format = r'%d/%m/%Y'
      self._current_datetime = datetime.today()
      self._current_date = datetime.strftime(self._current_datetime.date(), self._date_format)
      self.__shared_state['current_date'] = self._current_date



#
# if __name__ == '__main__':
#     config = Config()
#     print(config._current_date)
#     # print(config.__shared_state)
