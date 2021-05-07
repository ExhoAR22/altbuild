import os

SDK_DIR = os.path.expanduser('~/.altbuild/sdks')


def sdk_list():
    if not os.path.isdir(SDK_DIR):
        os.makedirs(SDK_DIR)