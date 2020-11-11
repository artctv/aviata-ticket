from . import Client, ClientBuilder

class App:

    def __init__(self, config):
        self.config = config
        self._instances = []

    def _app_factory(self):
        builder = ClientBuilder()
        client = builder(Client)
        self._instances.append((client, builder, client))
        return client

    def __call__(self):
        return self._app_factory()

    def run(self):
        print('Running')

        pass
