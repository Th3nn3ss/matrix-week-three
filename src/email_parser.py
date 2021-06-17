import re


class EmailParser:
    def __init__(self):
        # regex pattern that validate email
        self.pattern = r'^[A-Za-z][A-Za-z0-9+]+@[A-Za-z][A-Za-z0-9]+\.com$'
        self.keys = ['username', 'domain']

    def parse(self, email):
        ''' parse email and return a dictionary of username and domain if valid and return None otherwise'''
        # Add implementation here ...
        if re.match(self.pattern, email):
            username, domain = email.split('@')
            return self.convert_to_dict(username, domain)
        else:
            return None

    def convert_to_dict(self, username, domain):
        '''
          Takes in two lists as params and return them as a dictionary.'''
        result = {}
        result[self.keys[0]], result[self.keys[1]] = username, domain
        return result
