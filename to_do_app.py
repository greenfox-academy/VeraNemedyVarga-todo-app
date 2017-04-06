import sys
#import database
# content = open("database.txt", 'r')
# read_content = content.readlines()
# print(read_content)

class Controller():

    def __init__(self):
        self.list_argv = []
        self.arg_reader()
        self.controller()

    def arg_reader(self):
        if len(sys.argv) <= 1:
            self.list_argv = []
        else:
            self.list_argv = sys.argv[1:]

    def controller(self):
        if len(self.list_argv) == 0:
            view.print_usage()
        else:
            if self.list_argv[0] == "-l":
                view.print_list()

            #elif self.list_argv[0] == "a"
            #
            # if self.list_argv[0] == "-l":
            #     pass


class Model():
    pass
    # def database_open(self):
    #     self.content = open(database.txt, 'a+')
    #     self.read_content = self.content.read()
    #     print(self.read_content)


class View():
    def __init__(self):
        pass

    def print_usage(self):
        print("Python Todo application\n"
            "=======================\n\n"

            "Command line arguments:\n"
             "-l   Lists all the tasks\n"
             "-a   Adds a new task\n"
             "-r   Removes an task\n"
             "-c   Completes an task")

    def print_list(self):
            self.content = open("database.txt", "r")
            self.read_content = self.content.readlines()
            # self.todolist = []
            # self.todolist.append(self.read_content)
            #self.read_content.split('\n')
            for i in range(0, len(self.read_content)):
                result = ""
                result += str(i+1) + ". " + self.read_content[i].__str__()
                #return result
                print(result)



view = View()
model = Model()
controller = Controller()

controller.arg_reader()
#view.print_list()
#controller.controller("l")
#model.database_open()

#view.print_usage()
