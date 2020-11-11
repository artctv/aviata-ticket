import time

class Client():
    """Cient of concrete service"""
    def __init__(self, storage, service, parser):
        self._storage = storage
        self._service = service
        self._parser = parser

    @staticmethod
    def get_stamp():
        return hash(datetime.timestamp(datetime.today()))

    @staticmethod
    def days_in_month():
        today = datetime.today()
        year, month = today.year, today.month
        days = calendar.monthrange(year, month)
        return days[1]

    def something_storage(self):
        # self._storage.some_method()
        pass

    def something_service(self):
        # self._service.some_method()
        pass

    def something_parser(self):
        # self._parser.some_method()
        pass

    def __str__(self):
        return 'Client'

    def dirs_generator(self, obj):
        # if not hasattr(obj, '__iter__'):
        #     return TypeError()

        for value in obj:
            yield {'fly_from': value[0], 'fly_to': value[1]} #TODO

    def process_search(self):
        endpoint_data = self._storage.get_data('search')
        # directions = self._storage.get_various('directions')
        directions = self.dirs_generator(self._storage.get_various('directions'))
        prepared_data = self._service._operate_endpoint(endpoint_data)
        # print(prepared_data)
        response = self._service._make_request(prepared_data, directions)
        # for r in response:
        #     print(r.text)
        #     time.sleep(0.1)
