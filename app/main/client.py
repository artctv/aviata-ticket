
class Client():
    """Cient of concrete service"""
    def __init__(self, storage, service, parser):
        self._storage = storage
        self._service = service
        self._parser = parser

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
        return self._name
