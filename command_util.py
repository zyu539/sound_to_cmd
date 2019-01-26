#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 18:09:46 2019

@author: lhy
"""

import yaml
import webbrowser
import sound_util
import subprocess 
import music_util
import urllib

_lang_map = {
        'english': 'en-US',
        'chinese': 'zh-CN',
        }
   
def go_to_url(url='https://www.google.com/search?q=', search_args='', encode=False):
    #os.environ["BROSWER"] = r"/Applications/Google Chrome.app"
    if search_args:
        if encode: search_args = urllib.parse.quote(search_args)
        url += '+'.join(search_args.split())
    webbrowser.open(url)

def open_app(url):
    subprocess.call(
        ["/usr/bin/open", "-n", "-a", str(url)]
    )
    
def play_music():
    text = sound_util.audio2text("爸爸要听英文歌还是中文歌？")
    language = _lang_map.get(text) if text in _lang_map else None
    text = sound_util.audio2text("爸爸要听什么歌？", language=language)
    url = music_util.youtube().get_audio(text.lower())
    go_to_url(url=url, encode=(language != 'en-US'))
   
_dispatch = {
    0 : go_to_url, # '0' means directly search on google / or go the the URL
    1 : open_app,
    2 : play_music,
}

def text2command(cmd):
    with open('command_map.yaml', 'r') as f:
        content = yaml.load(f)
        if cmd and cmd in content:
            func = _dispatch[content[cmd]['program']]
            if 'args' in content[cmd]:
                func(**content[cmd]['args']) # function need args
            else:
                func()
        else:
            go_to_url(search_args=str(cmd))
    f.close()