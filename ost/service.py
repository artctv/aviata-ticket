import requests
import json
from datetime import datetime, timedelta
import calendar
from collections import namedtuple
from conf import Config


class ServiceBase(object):
   """Abstract service with API."""

   _r = requests
   _storage = {}

   @staticmethod
   def get_stamp():
      return hash(datetime.timestamp(datetime.today()))

   @staticmethod
   def days_in_month():
      today = datetime.today()
      year, month = today.year, today.month
      days = calendar.monthrange(year, month)
      return days[1]


   def configure_service(self, config):
      raise NotImplementedError()

   def construct_url(self, *args, **kwargs):
      raise NotImplementedError()

   def make_request(self, endpoint, method, *args, **kwargs):
      raise NotImplementedError()


class SkypickerService(ServiceBase):
   """Skypicker Ticket API service."""

   # def __init__(self):
   #    self._date_format = r'%d/%m/%Y'
   #    self._current_datetime = datetime.today()
   #    self._current_date = datetime.strftime(self._current_datetime.date(), self._date_format)

   # IATA_code names
   _IATA_NAMES = {
      'ALA': 'Алматы',
      'TSE': 'Астана',
      'MOW': 'Москва',
      'LED': 'С-Петербург',
      'CIT': 'Шымкент',
   }

   # IATA_code flight routes
   _FLY_DIRECTIONS = {
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

   _DATE_FORMAT = r'%d/%m/%Y'

   _CORE = r'https://api.skypicker.com{}'

   _STRUCTURE = namedtuple('endpoint', ['url','method','headers','params','data'])

   _ENDPOINTS = ('flights',)

   _ARGS = {
      'flights': {
         'url': '/flights', 'method': 'GET',
         'headers': {'Content-Type': 'application/json'},
         'params': {'fly_from': '{IATA}', 'fly_to': '{IATA}',
         'date_from': '{date}', 'date_to': '{date}', 'partner': 'picky'}, # date str %d/%m/%Y
         'data': None,
      }
   }

   def _create_dates(self):
      month_day = ServiceBase.days_in_month()
      now = datetime.today().date()
      after = now + timedelta(days=month_day)
      now_in_f = datetime.strftime(now, self._DATE_FORMAT)
      after_in_f = datetime.strftime(after, self._DATE_FORMAT)
      for key, value in locals().items():
         if key != 'self':
            setattr(self, '_'+key, value)




   def configure_service(self, config):
      pass

   def _construct_data(self, endpoint):
      data = self._ARGS.get(endpoint)
      data['params']['date_from'] = self._now_in_f
      data['params']['date_to'] = self._after_in_f
      data['params']['fly_from'] = 'ALA'
      data['params']['fly_to'] = 'CIT'
      # return self._STRUCTURE(**self._ARGS.get(endpoint))
      return data


   def construct_url(self, endpoint):
      data = self._construct_data(endpoint)
      url = self._CORE.format(data.get('url'))
      return data, url
      # print(data)
      # print(url)

   def make_request(self):
      data, url = self.construct_url('flights')
      method = getattr(self._r, data.get('method').lower())
      response = method(url=url, headers=data.get('headers'), params=data.get('params'))
      # response = get(url, params=data._asdict())
      # print(response.text)
      with open('data.json', 'w') as f:
         json.dump(response.json(), f)



class RequestControlBase(object):
    """Abstract request sender."""

    def __init__(self):
        self._service = self.get_service()
        # self._tv = self.get_tv()

    # def get_tv(self):
    def get_service(self):
        raise NotImplementedError()

    # def tune_channel(self, channel):
        # self._tv.tune_channel(channel)
    def configure_service(self, config):
        self._service.configure_service(config)



class RequestSkypicker(RequestControlBase):
    """Skypicker API client."""

    def __init__(self):
        super(RequestSkypicker, self).__init__()
        # self._config = 0

    def get_service(self):
        return SkypickerService()

    def configure_service(self, config):
        super(RequestSkypicker, self).configure_service(config)
        self._config = config





if __name__ == '__main__':
   o = RequestSkypicker()
   ServiceBase.days_in_month()
   serv = o.get_service()
   serv._create_dates()
   serv.make_request()




    # def get_tv(self):
        # return SharpTV()


    # def tune_channel(self, channel):
        # super(RemoteControl, self).tune_channel(channel)
        # self._channel = channel


    # def next_channel(self):
    #     self._channel += 1
    #     self.tune_channel(self._channel)
    #
    # def previous_channel(self):
    #     self._channel -= 1
    #     self.tune_channel(self._channel)


# remote_control = RemoteControl()
# remote_control.tune_channel(5)  # Sharp TV: выбран 5 канал
# remote_control.next_channel()
