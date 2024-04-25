import os


class LocalPath:
    cookies_path = os.path.abspath(r'jsons\cookies.json')
    useragents_path = os.path.abspath(r'jsons\useragents.json')
    followers_path = os.path.abspath(r'jsons\followers.json')
    comment_path = os.path.abspath(r'jsons\comments.json')
