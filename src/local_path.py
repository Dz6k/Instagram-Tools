import os
from colorama import Fore


class LocalPath:
    cookies_path = os.path.abspath(r'jsons\cookies.json')
    useragents_path = os.path.abspath(r'jsons\useragents.json')
    followers_path = os.path.abspath(r'jsons\followers.json')
    comment_path = os.path.abspath(r'jsons\comments.json')


for attr_name in dir(LocalPath):
    attr = getattr(LocalPath, attr_name)
    if isinstance(attr, str) and attr.endswith('.json') and not os.path.exists(attr):
        with open(attr, 'w'):
            ...
        print(Fore.GREEN + 'Folders Created: ' +
              Fore.LIGHTMAGENTA_EX + f'{attr}{os.linesep}' + Fore.RESET)
