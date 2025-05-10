class Secret:
    def __init__(self):
        self.__password = "12345"  # Private attribute #ABC


s = Secret()
# print(s.__password)  # This will raise an AttributeError because __password is private