import os


class LocalPath:
    try:
        cookies_path = os.path.abspath(r'jsons\cookies.json')
    except:
        with open(r'jsons\cookies.json', 'w'):
            pass
        
    try:
        useragents_path = os.path.abspath(r'jsons\useragents.json')
    except:
        with open(r'jsons\useragents.json', 'w'):
            pass
        
    try:
        followers_path = os.path.abspath(r'jsons\followers.json')
    except:
        with open(r'jsons\followers.json', 'w'):
            pass
        
    try:   
        comment_path = os.path.abspath(r'jsons\comments.json')
    except:
        with open(r'jsons\comments.json', 'w'):
            pass
