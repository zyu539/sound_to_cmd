#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 21:43:25 2019

@author: lhy
"""
from __future__ import unicode_literals
import requests
import re
import youtube_dl
import os.path
import urllib

AUDIO_PATH = '/Users/lhy/Downloads/musics'

class music:
    
    def __init__(self):
        self.ext = 'webm'
    
    def get_audio(self, search_text):
        pass
    
    

class youtube(music):
    
    def __init__(self):
        music.__init__(self)
        self.base_url = 'https://www.youtube.com/results?search_query={}'
        
    def get_audio(self, search_text, encode=False):
        fname = urllib.parse.quote('{}/{}.{}'.format(AUDIO_PATH, search_text, self.ext))
        if os.path.isfile(fname):
            return 'file://' + fname
        url = self.base_url.format(search_text)
        html = self.get_html(url)
        return 'file://' + urllib.parse.quote(self.download_audio(self.get_url(html), search_text))
        
    
    def get_html(self, url):
        page = requests.get(url)
        html = page.text
        return html
      
    def get_url(self, html, num=5):
        reg = r"(?<=a\shref=\"/watch).+?(?=\")"
        urlre = re.compile(reg)
        urllist = re.findall(urlre,html)
        url_format = "https://www.youtube.com/watch{}"
        top_songs = []
        for url in urllist:
            if num > 0:
                top_songs.append(url_format.format(url))
            else:
                break
            num -= 1
        return top_songs
    
    def download_audio(self, songs, text):
        path = None
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': AUDIO_PATH + '/{}.%(ext)s'.format(text)
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([songs[0]])
            path = '{}/{}.{}'.format(AUDIO_PATH, text, self.ext)
        if path:
            print(path)
            return path
        raise Exception('爸爸我错了。。下载失败')

    