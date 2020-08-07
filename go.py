#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2020-08-07 23:51:30
# @Author  : Racter Liu (racterub) (racterub@gmail.com)
# @Link    : https://racterub.me
# @License : MIT

import yzuStudentProfile as ysp

## Generate Profile Url
print(ysp.gen_token()) #token as parameter (int)

## Decode Profile Url to student ID
print(ysp.dec_token()) #url as parameter (string)