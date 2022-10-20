import requests


class Formatter:
    def __init__(self, code="", lexer="python", style="monokai", divstyles=""):
        self.url = "http://hilite.me/api"
        self.keys = ['code', 'lexer', 'style', 'divstyles']
        self.params = {}
        self.set(code=code, lexer=lexer, style=style, divstyles=divstyles)

    def set(self, **kwargs):
        for key in self.keys:
            if key in kwargs:
                self.params[key] = kwargs[key]

    def format_code(self):
        r = requests.post(url=self.url, data=self.params)
        formatted_code = r.text
        r.close()
        return formatted_code
