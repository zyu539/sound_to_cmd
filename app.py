#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 19:58:07 2019

@author: lhy
"""

import sound_util, command_util

def main():
    active = False
    while True:
        text = sound_util.audio2text("", 'zh-CN')
        try:
            if '儿子' in text:
                active = True
            elif '关闭' in text or '退出' in text or '没事' in text:
                active = False
            elif '滚蛋' in text:
                break
            if active:
                text = sound_util.audio2text("爸爸要干什么？")
                command_util.text2command(text)
        except Exception:
            pass
            
if __name__ == '__main__':
    main()