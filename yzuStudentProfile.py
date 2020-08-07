#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2020-08-07 23:46:50
# @Author  : Racter Liu (racterub) (racterub@gmail.com)
# @Link    : https://racterub.me
# @License : MIT

def gen_token(uid):
    import datetime
    import base64
    payload = ['Y', 'Z']
    time = datetime.date.today()
    tmp = str(time.year) + '/' + str(time.month).rjust(2, '0') +'/' + str(time.day).rjust(2, '0')
    payload += list(tmp) + list('s' + str(uid))
    return 'https://portalx.yzu.edu.tw/PortalSocialVB/FMain/PostWall.aspx?Menu=User&UserAccount=' + base64.b64encode(('\x00'.join(payload) + '\x00').encode()).decode()

def dec_token(token):
    import base64
    data = ''.join(base64.b64decode(token[84:]).decode().split('\x00'))
    return data[12:]
