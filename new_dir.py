import os


class NewDirectory:
    def __init__(self, dir_name):
        self.dir_name = dir_name

    def create_new_dir(self):
        try:
            os.makedirs(self.dir_name)
        except FileExistsError:
            pass

    def new_dir_path(self):
        path = f'{os.getcwd()}\\{self.dir_name}'
        return path

    @staticmethod
    def delete_dir(path_to_dir):
        os.rmdir(path_to_dir)

