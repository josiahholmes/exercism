class Phone(object):
    def __init__(self, phone_number):
        self.number = self.clean_phone_number(phone_number)
        self.area_code = self.number[:3]
        self.exchange_code = self.number[3:6]
        self.subscriber_number = self.number[6:10]

    def clean_phone_number(self, number: str) -> str:
        extras = ['(', ')', ' ', '.', '-', '+']

        for extra in extras:
            if extra in number:
                number = number.replace(extra, '')

        if len(number) > 11:
            raise ValueError('Phone number has more than 11 digits.')
        if len(number) == 11 and number[0] != '1':
            raise ValueError('Phone number does not begin with 1.')
        if len(number) == 11 and number[0] == '1':
            number = number[1:len(number)]
        if number[:3].startswith(('0', '1')):
            raise ValueError('Area code begins with 0 or 1.')
        if number[3:6].startswith(('0', '1')):
            raise ValueError('Exchange codes begins with 0 or 1.')

        return number

    def pretty(self) -> str:
        return f'({self.area_code}) {self.exchange_code}-{self.subscriber_number}'
