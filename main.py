from conf import Config
from app import App


def main():
    app = App(Config)
    api = app()
    api.process_search()


if __name__ == '__main__':
    main()
