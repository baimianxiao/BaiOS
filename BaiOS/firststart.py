# -*- coding: utf-8 -*-

import subprocess
import os


class loadConfig(object):
    def __init__(self, bot_data_arr):
        self.config_file_str = ''
        self.config_file_format = {}
        self.bot_data_arr = bot_data_arr

    def setConfig(self):
        self.config_file_str = (
            "account:\n"
            "  uin: {uin}\n"
            "  password: '{password}'\n"
            "  encrypt: false\n"
            "  status: 0\n"
            "  relogin:\n"
            "    disabled: false\n"
            "    delay: 3\n"
            "    interval: 0\n"
            "    max-times: 0\n"
            "  use-sso-address: true\n"
            "\n"
            "heartbeat:\n"
            "  disabled: false\n"
            "  interval: 5\n"
            "\n"
            "message:\n"
            "  post-format: string\n"
            "  ignore-invalid-cqcode: false\n"
            "  force-fragment: false\n"
            "  fix-url: false\n"
            "  proxy-rewrite: ''\n"
            "  report-self-message: false\n"
            "  remove-reply-at: false\n"
            "  extra-reply-data: false\n"
            "\n"
            "output:\n"
            "  log-level: info\n"
            "  debug: false\n"
            "\n"
            "default-middlewares: &default\n"
            "  access-token: ''\n"
            "  filter: ''\n"
            "  rate-limit:\n"
            "    enabled: false\n"
            "    frequency: 1\n"
            "    bucket: 1\n"
            "\n"
            "servers:\n"
            "  - http:\n"
            "      disabled: false\n"
            "      host: {servers-host}\n"
            "      port: {servers-port}\n"
            "      timeout: 60\n"
            "      middlewares:\n"
            "        <<: *default\n"
            "      post:\n"
            "       - url: '{servers-post-url}'\n"
            "\n"
            "database:\n"
            "  leveldb:\n"
            "    enable: true\n"
        )

        self.config_file_format['uin'] = str(self.bot_data_arr['uin'])
        self.config_file_format['password'] = self.bot_data_arr['password']
        self.config_file_format['servers-host'] = self.bot_data_arr['servers']['host']
        self.config_file_format['servers-port'] = str(self.bot_data_arr['servers']['port'])
        self.config_file_format['servers-post-url'] = str(self.bot_data_arr['servers']['post'])

        self.config_file_str = self.config_file_str.format(**self.config_file_format)
        if not os.path.exists('./conf/gocqhttp/' + str(self.bot_data_arr['uin'])):
            os.makedirs('./conf/gocqhttp/' + str(self.bot_data_arr['uin']))
        with open('./conf/gocqhttp/' + str(self.bot_data_arr['uin']) + '/config.yml', 'w+') as tmp:
            tmp.write(self.config_file_str)


class start:
    def __init__(self, bot_data_arr, title='BaiOS'):
        self.title = title
        self.bot_data_arr = bot_data_arr

    def start(self):
        os.system('.\\lib\\go-cqhttp.exe faststart')

    def startgocqhttp(self):
        start = True
        CWD = '.\\conf\\gocqhttp\\' + str(self.bot_data_arr['uin']) + '\\'
        while start:
            subprocess.call(
                'start cmd /K "title BaiOS' + self.title + '|..\\..\\lib\\go-cqhttp.exe faststart"',
                shell=True,
                cwd=CWD
            )
            start = False
