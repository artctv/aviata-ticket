class App:

    def __init__(self, config):
        self.config = config

    def _app_factory(config):
        app = self.builder(self.client)
        return app

    def __call__(self):
        return self._app_factory()
