# -*- coding: utf-8 -*-
import json
import requests


class BaiApi:
    """go_cqhttp主动Api"""

    def __init__(self, host="http://127.0.0.1:", port=5700):
        self.headers = {'Content-Type': 'application/json'}
        self.url = host + str(port) + "/"

    def send_private_msg(self, user_id, group_id, message, auto_escape=None):
        """发送私聊消息"""
        post_road = "send_private_msg"
        data = json.dumps({"user_id": user_id, "group_id": group_id, "message": message,
                           "auto_escape": auto_escape})
        return_message = requests.post(self.url + post_road, data=data, headers=self.headers)
        return return_message.text

    def send_group_msg(self, group_id, message, auto_escape=None):
        """发送群消息"""
        post_road = "send_group_msg"
        data = json.dumps(
            {"group_id": group_id, "message": message, "auto_escape": auto_escape})
        return_message = requests.post(self.url + post_road, data=data, headers=self.headers)
        return return_message.text

    def send_group_forward_msg(self, group_id, message):
        """发送合并转发 (群)"""
        post_road = "send_group_forward_msg"
        data = json.dumps({"group_id": group_id, "message": message})
        requests.post(self.url + post_road, data=data, headers=self.headers)

    def send_message(self, message_type, user_id, group_id, message, auto_escape=None):
        """发送消息"""
        post_road = "send_msg"
        data = json.dumps({"message_type": message_type, "user_id": user_id, "group_id": group_id, "message": message,
                           "auto_escape": auto_escape})
        return_message = requests.post(self.url + post_road, data=data, headers=self.headers)
        return return_message.text

    def delete_msg(self, message_id):
        """撤回消息"""
        post_road = "delete_msg"
        data = json.dumps({"message_id": message_id})
        return_message = requests.post(self.url + post_road, data=data, headers=self.headers)
        return return_message.text

    def get_msg(self, message_id):
        """获取消息"""
        post_road = "get_msg"
        data = json.dumps({"message_id": message_id})
        return_message = requests.post(self.url + post_road, data=data, headers=self.headers)
        return return_message.text

    def get_forward_msg(self, message_id):
        """获取合并转发内容"""
        post_road = "get_forward_msg"
        data = json.dumps({"message_id": message_id})
        return_message = requests.post(self.url + post_road, data=data, headers=self.headers)
        return return_message.text

    def get_image(self, message_id):
        """获取图片信息"""
        post_road = "get_image"
        data = json.dumps({"message_id": message_id})
        return_message = requests.post(self.url + post_road, data=data, headers=self.headers)
        return return_message.text

    def set_group_kick(self, group_id, user_id, reject_add_request=None):
        """群组踢人"""
        post_road = "set_group_kick"
        data = json.dumps({"group_id": group_id, "user_id": user_id, "reject_add_request": reject_add_request})
        requests.post(self.url + post_road, data=data, headers=self.headers)

    def set_group_ban(self, group_id, user_id, duration=0):
        """群组单人禁言"""
        post_road = "set_group_ban"
        data = json.dumps({"group_id": group_id, "user_id": user_id, "duration": duration})
        requests.post(self.url + post_road, data=data, headers=self.headers)

    def set_group_anonymous_ban(self, group_id, user_id, anonymous_flag, duration=0):
        """群组匿名用户禁言"""
        post_road = "set_group_anonymous_ban"
        data = json.dumps(
            {"group_id": group_id, "user_id": user_id, "anonymous_flag": anonymous_flag, "duration": duration})
        requests.post(self.url + post_road, data=data, headers=self.headers)

    def set_group_whole_ban(self, group_id, enable=None):
        """群组全员禁言"""
        post_road = "set_group_whole_ban"
        data = json.dumps({"group_id": group_id, "enable": enable})
        requests.post(self.url + post_road, data=data, headers=self.headers)

    def set_group_admin(self, group_id, user_id, enable=None):
        """群组设置管理员"""
        post_road = "set_group_admin"
        data = json.dumps({"group_id": group_id, "user_id": user_id, "enable": enable})
        requests.post(self.url + post_road, data=data, headers=self.headers)

    def set_group_card(self, group_id, user_id, card=None):
        """设置群名片 (群备注)"""
        post_road = "set_group_card"
        data = json.dumps({"group_id": group_id, "user_id": user_id, "card": card})
        requests.post(self.url + post_road, data=data, headers=self.headers)

    def set_group_name(self, group_id, group_name):
        """设置群名"""
        post_road = "set_group_name"
        data = json.dumps({"group_id": group_id, "group_name": group_name})
        requests.post(self.url + post_road, data=data, headers=self.headers)

    def set_group_leave(self, group_id, is_dismiss=None):
        """退出群组"""
        post_road = "set_group_leave"
        data = json.dumps({"group_id": group_id, "is_dismiss": is_dismiss})
        requests.post(self.url + post_road, data=data, headers=self.headers)

    def set_group_special_title(self, group_id, user_id, special_title=None, duration=None):
        """设置群组专属头衔"""
        post_road = "set_group_special_title"
        data = json.dumps(
            {"group_id": group_id, "user_id": user_id, "special_title": special_title, "duration": duration})
        requests.post(self.url + post_road, data=data, headers=self.headers)

    def set_friend_add_request(self, flag, approve=None, remark=None):
        """处理加好友请求"""
        post_road = "set_friend_add_request"
        data = json.dumps({"flag": flag, "approve": approve, "remark": remark})
        requests.post(self.url + post_road, data=data, headers=self.headers)

    def set_group_add_request(self, flag, type, approve=None, reason=None):
        """处理加群请求／邀请"""
        post_road = "set_group_add_request"
        data = json.dumps({"flag": flag, "type": type, "approve": approve, "reason": reason})
        requests.post(self.url + post_road, data=data, headers=self.headers)

    def get_login_info(self):
        """获取登录号信息"""
        post_road = "get_login_info"
        return_message = requests.post(self.url + post_road, headers=self.headers)
        return return_message.text

    def get_stranger_info(self, user_id, no_cache=None):
        """获取陌生人信息"""
        post_road = "get_stranger_info"
        data = json.dumps({"user_id": user_id, "no_cache": no_cache})
        return_message = requests.post(self.url + post_road, data=data, headers=self.headers)
        return return_message.text

    def get_friend_list(self):
        """获取好友列表"""
        post_road = "get_friend_list"
        return_message = requests.post(self.url + post_road, headers=self.headers)
        return return_message.text

    def delete_friend(self, friend_id):
        """删除好友"""
        post_road = "delete_friend"
        data = json.dumps({"friend_id": friend_id})
        requests.post(self.url + post_road, data=data, headers=self.headers)

    def get_group_info(self, group_id, no_cache=None):
        """获取群信息"""
        post_road = "get_group_info"
        data = json.dumps({"group_id": group_id, "no_cache": no_cache})
        return_message = requests.post(self.url + post_road, data=data, headers=self.headers)
        return return_message.text

    def get_group_list(self):
        """获取群列表"""
        post_road = "get_group_list"
        return_message = requests.post(self.url + post_road, headers=self.headers)
        return return_message.text

    def get_group_member_info(self, group_id, user_id, no_cache=None):
        """获取群成员信息"""
        post_road = "get_group_member_info"
        data = json.dumps({"group_id": group_id, "user_id": user_id, "no_cache": no_cache})
        return_message = requests.post(self.url + post_road, data=data, headers=self.headers)
        return return_message.text

    def get_group_member_list(self, group_id):
        """获取群成员列表"""
        post_road = "get_group_member_list"
        data = json.dumps({"group_id": group_id})
        return_message = requests.post(self.url + post_road, data=data, headers=self.headers)
        return return_message.text

    def get_group_honor_info(self, group_id, type):
        """获取群荣誉信息"""
        post_road = "get_group_honor_info"
        data = json.dumps({"group_id": group_id, "type": type})
        return_message = requests.post(self.url + post_road, data=data, headers=self.headers)
        return return_message.text

    def get_version_info(self):
        """获取版本信息"""
        post_road = "get_version_info"
        return_message = requests.post(self.url + post_road, headers=self.headers)
        return return_message.text

    def set_restart(self, delay=None):
        """重启 go-cqhttp"""
        post_road = "set_restart"
        data = json.dumps({"delay": delay})
        requests.post(self.url + post_road, data=data, headers=self.headers)

    def set_group_portrait(self, group_id, file, cache):
        """设置群头像"""
        post_road = "set_group_portrait"
        data = json.dumps({"group_id": group_id, "file": file, "cache": cache})
        requests.post(self.url + post_road, data=data, headers=self.headers)

    def get_group_system_msg(self):
        """获取群系统消息"""
        post_road = "get_group_system_msg"
        requests.post(self.url + post_road, headers=self.headers)

    def upload_group_file(self, group_id, file, name, folder):
        """上传群文件\n在不提供 folder 参数的情况下默认上传到根目录\n只能上传本地文件, 需要上传 http 文件的话请先调用 download_file API下载"""
        post_road = "upload_group_file"
        data = json.dumps({"group_id": group_id, "file": file, "name": name, "folder": folder})
        requests.post(self.url + post_road, data=data, headers=self.headers)

    def get_group_file_system_info(self, group_id):
        """获取群文件系统信息"""
        post_road = "get_group_file_system_info"
        data = json.dumps({"group_id": group_id})
        return_message = requests.post(self.url + post_road, data=data, headers=self.headers)
        return return_message.text

    def send_group_notice(self, group_id, content):
        r"""获取群文件系统信息
            :param group_id:群号
            :param content:公告内容
            """
        post_road = "_send_group_notice"
        data = json.dumps({"group_id": group_id, "content": content})
        requests.post(self.url + post_road, data=data, headers=self.headers)


if __name__ == "__main__":
    test = BaiApi()

    test.send_group_notice('822417015', "测试试一试bot可不可以发公告")
