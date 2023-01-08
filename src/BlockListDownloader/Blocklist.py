class Blocklist:
    def __init__(self, name, url, filename):
        self.name: str = name
        self.url: str = url
        self.filename: str = filename

    def __iter__(self):
        yield from {
            "name": self.name,
            "url": self.url,
            "filename": self.filename
        }