from services.knowledge_base.knowledge_base import IKnowledgeBase
from services.knowledge_base.math_object import *


class KnowledgeBase(IKnowledgeBase):
    def __init__(self, obj_dict):
        self.__obj_dict = obj_dict

    def find_obj(self, obj_name):
        if obj_name in self.__obj_dict:
            return self.__obj_dict[obj_name]
        return None

    def add_obj(self, obj_name: str, obj_description: str):
        self.__obj_dict[obj_name] = GenericMathObject(obj_name, obj_description)


def make_objects_dict_impl(obj_list):
    obj_dict = dict()
    for obj in obj_list:
        obj_dict[obj.get_name()] = obj
    return obj_dict


def make_objects_dict():
    return make_objects_dict_impl(
        [GenericMathObject("Prime", "Prime number")
            , GenericMathObject("Natural", "Natural number")
            , GenericMathObject("Number", "Number notion")
         ])
