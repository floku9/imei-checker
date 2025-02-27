from enum import Enum


class Messages(str, Enum):
    USER_SUCCESSFULLY_REGISTERED = "Вы были успешно зарегистрированы в нашем сервисе!"
    USER_ALREADY_REGISTERED = "Вы уже зарегистрированы в нашем сервисе, приятного пользования!"
