from random import choice


class Intent():

    def __init__(self, tag, patterns, responses):
        self.tag = tag
        self.patterns = patterns
        self.responses = responses

    def response(self):
        return choice(self.responses)
