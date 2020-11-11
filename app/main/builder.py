from app.skypicker import Storage, Service, Parser


class Builder():
    def configure_storage(self):
        raise NotImplementedError()

    def configure_service(self):
        raise NotImplementedError()

    def configure_parser(self):
        raise NotImplementedError()

    def create_client(self):
        raise NotImplementedError()

    def __call__(self, cls):
        return self.create_client(cls)


class ClientBuilder(Builder):
    def configure_storage(self):
        return Storage()

    def configure_service(self):
        return Service()

    def configure_parser(self):
        return Parser()

    def create_client(self, Client):
        storage = self.configure_storage()
        service = self.configure_service()
        parser = self.configure_parser()
        return Client(storage, service, parser)
