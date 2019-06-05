# -*- coding: utf-8 -*-
from __future__ import absolute_import

__all__ = ['celery_app', 'RUN_VER', 'APP_CODE', 'SECRET_KEY', 'BK_URL', 'BASE_DIR']

import os

# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from blueapps.core.celery import celery_app

# app 基本信息

# SaaS运行版本，如非必要请勿修改
RUN_VER = 'open'
# SaaS应用ID
APP_CODE = 'tegs'
# SaaS安全密钥，注意请勿泄露该密钥
SECRET_KEY = '70024183-ab60-4faa-b53d-8660974fb21a'
# SECRET_KEY = '81c79f48-37fa-486d-9831-e1cee5d79654' # 早鸟
# 蓝鲸SaaS平台URL, 如 https://paas.blueking.com/
BK_URL = 'http://paasce-b.o.qcloud.com'
# BK_URL = 'http://paas.class.o.qcloud.com'

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(
    __file__)))
