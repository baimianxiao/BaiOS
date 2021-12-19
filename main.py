import time

import BaiOS

bot_data_servers = {
    'host': '127.0.0.1',
    'port': '9999',
    'post': 'http://127.0.0.1:9998'

}
bot_data_arr = {
    'uin': '2127114208',
    'password': 'wyc18971346783',
    'servers': bot_data_servers

}
print('创建gocqhttp配置文件')
BaiOS.firststart.loadConfig(bot_data_arr).setConfig()
print('已创建gocqhttp配置文件\n三秒后启动gocqhttp')
time.sleep(5)
print('尝试启动gocqhttp')
try:
    BaiOS.firststart.start(bot_data_arr).startgocqhttp()
    print('启动成功！')
except:
    print('启动失败！')
