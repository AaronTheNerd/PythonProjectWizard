from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Generic, Optional, TypeVar


T = TypeVar('T')

@dataclass
class Input(ABC, Generic[T]):
    id: str
    prompt: str
    default_value: str = ""
    __value: str = ""

    @property
    def value(self) -> Optional[T]:
        if self.valid(self.__value):
            return self.parse(self.__value)
        return None

    @value.setter
    def value(self, value: str) -> None:
        self.__value = value
        if self.__value == "":
            self.__value = self.default_value

    @abstractmethod
    def valid(self, value: str) -> bool:
        ...

    @abstractmethod
    def parse(self, value: str) -> T:
        ...
