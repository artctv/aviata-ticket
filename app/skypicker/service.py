import requests
import calendar
from datetime import datetime, timedelta


class Service():
    """Service"""

    _r = requests
    _service_special = {}

    @staticmethod
    def get_stamp():
        return hash(datetime.timestamp(datetime.today()))

    @staticmethod
    def days_in_month():
        today = datetime.today()
        year, month = today.year, today.month
        days = calendar.monthrange(year, month)
        return days[1]

    def _get_r(self):
        return self._r

    def _create_dates(self, format):
        month_day = Service.days_in_month()
        date_from_obj = datetime.today().date()
        date_to_obj = date_from_obj + timedelta(days=month_day)
        date_from = datetime.strftime(date_from_obj, format)
        date_to = datetime.strftime(date_to_obj, format)
        dates = locals()
        _ = dates.pop('self')
        return dates

    def _save_special(self, key, value):
        self._service_special[key] = value

    def _get_special(self, data):
        value = self._service_special.get(data)
        if value is None:
            NameError()
        else:
            return value

    def _get_all_special(self):
        return self._service_special

    def _get_methods(self, methods):
        return tuple(getattr(self._r, method.lower()) for method in methods)

    def _prepare_dates(self, format):
        dates = {'dates': self._create_dates(format)}
        for key, value in dates.items():
            self._save_special(key, value)


    def _prepare_request(self, data):
        url = '{}/{}'.format(
            data.get('core'),
            data.get('endpoint'),
        )
        headers = data.get('headers')
        method = self._get_methods(data.get('methods'))
        args = dict.fromkeys(data.get('args'), )
        prepared_data = locals()
        _, _ = prepared_data.pop('self'), prepared_data.pop('data')
        return prepared_data


    def _operate_endpoint(self, data):
        self._prepare_dates(data.get('date_format'))
        return self._prepare_request(data)


    def _prepare_args(self, args):
        dates_data = self._get_special('dates')
        args_names = tuple(filter(lambda arg: True if arg in dates_data else False, args.keys()))
        args_values = tuple(dates_data.get(value) for value in args_names)
        return args_names, args_values


    def _make_request(self, data, directions):
        response = []
        date_keys, date_values = self._prepare_args(data.get('args'))
        dates = dict(zip(date_keys, date_values))
        url, method, headers = data.get('url'), data.get('method')[0], data.get('headers')
        # print(url, method, headers)
        for dirs in directions:
            params = dirs.copy()
            params.update(dates)
            params['partner'] = 'picky'
            # response = method(url=url, headers=headers, params=params)
            # yield response
            # print(response.text)




    # def make_request(self):
