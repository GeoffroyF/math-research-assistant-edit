from abc import *


class INotion(metaclass=ABCMeta):

    @abstractmethod
    def get_name(self) -> str:
        pass
