import random

class HeaderSwitch:
    def __init__(self, orginal_header: dict):
        self.orginal_header = orginal_header
    
    def change_header(self):
        no_random_variables = random.randint(4, 14)
        random_keys = random.sample(list(self.orginal_header.keys()), no_random_variables)
        new_header = {key: self.orginal_header[key] for key in random_keys}
        return new_header
