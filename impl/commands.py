from services.command import IUserCommand
from services.knowledge_base.knowledge_base import IKnowledgeBase


class Finish(IUserCommand):
    def get_command_tag(self):
        return "finish"

    def get_args_count(self):
        return 0

    def evaluate(self, state, args, base: IKnowledgeBase):
        return True, state, "Finished."


class Describe(IUserCommand):
    def get_command_tag(self):
        return "describe"

    def get_args_count(self):
        return 1

    def evaluate(self, state, args, base: IKnowledgeBase):
        if len(args) != 1:
            raise Exception("Invalid number of arguments.")

        found = base.find_obj(args[0])
        if found != None:
            return False, state, found.get_description()

        return False, state, "Object not found in DB: " + args[0]


class DescribeShort(Describe):
    def get_command_tag(self):
        return "d"


class Add(IUserCommand):
    def get_command_tag(self):
        return "add"

    def get_args_count(self):
        return 2

    def evaluate(self, state, args, base: IKnowledgeBase):
        if len(args) != 2:
            raise Exception("Invalid number of arguments : add NAME DESCRIPTION")

        found = base.find_obj(args[0])
        if found != None:
            return False, state, "Object already in DB"

        base.add_obj(args[0], args[1])

        return False, state, "Successfully added the object : " + args[0] + " / " + args[1]
