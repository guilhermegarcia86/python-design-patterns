

class EmailSubject:

    def __init__(self):
        self.__subscribers = []

    def add_email(self, subject):
        self.notify_subscribers(subject)

    def subscribe(self, subscriber):
        self.__subscribers.append(subscriber)

    def unsubscribe(self, subscriber):
        return self.__subscribers.remove(subscriber)

    def subscribers(self):
        return self.__subscribers

    def notify_subscribers(self, subject):
        for sub in self.__subscribers:
            sub.update(subject)
