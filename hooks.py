
__version__ = '0.1.0'


class Hooks:
    """
    Simple implementation of the observer pattern
    """
    __slots__ = ('__hooks',)

    def __init__(self):
        self.__hooks = {}

    def add(self, hook_name, action_name, action):
        if hook_name not in self.__hooks:
            self.__hooks[hook_name] = {}
        if action_name in self.__hooks[hook_name]:
            raise Exception(f'{action_name} already exists in `{hook_name}` hook')
        self.__hooks[hook_name][action_name] = action

    def call(self, hook_name, *args, **kwargs):
        if hook_name not in self.__hooks:
            return
        for action in dict(self.hooks[hook_name]).values():
            action(*args, **kwargs)

    def remove(self, hook_name, action_name):
        if hook_name not in self.__hooks:
            raise Exception(f'{hook_name} hook not found')
        if action_name not in self.__hooks[hook_name]:
            raise Exception(f'{action_name} action not found in {hook_name} actions list')
        del self.__hooks[hook_name][action_name]

    @property
    def hooks(self):
        return dict(self.__hooks)
