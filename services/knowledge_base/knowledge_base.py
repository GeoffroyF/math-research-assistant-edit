from abc import *

from services.knowledge_base.math_object import IMathObject


class IKnowledgeBase(metaclass = ABCMeta):

    @abstractmethod
    def find_obj(self, obj_name : str) -> IMathObject:
        pass

    def add_obj(self, obj_name: str, obj_description : str):
        pass
