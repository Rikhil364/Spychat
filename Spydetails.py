
from datetime import datetime

class Spy:
    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.spy_is_online = True
        self.chats = []
        self.current_status_messages = None


spy = Spy('Rikhil', 'Mr.', 19, 7.5)

friend_one = Spy('Dev', 'Mr', 18,6.5)
friend_two = Spy('Dev', 'Mr', 18,6.5)
friend_three = Spy('Dev', 'Mr', 18,6.5)
friends = [friend_one, friend_two, friend_three]


class Chat:

  def __init__(self, message, sent_by_me):
    self.message = message
    self.time = datetime.now()
    self.sent_by_me = sent_by_me