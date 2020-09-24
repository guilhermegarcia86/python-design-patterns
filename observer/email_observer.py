class EmailObserver:

    def __init__(self, email):
        self.__email = email

    def update(self, invoice):
        print(f'For {self.__email}, send report about {invoice}')
