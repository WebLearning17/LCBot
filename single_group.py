#!/usr/bin/env python3
# coding: utf-8
"""
功能说明：
1. 用户无需发送关键词，添加好友后，自动发送邀请消息
2. 添加好友后，会自动发送回复语（下方可修改）
3. 用户进群后，自动发送相关的邀请信息。
"""
"""
定义区，下方数据修改为你自己对应的内容
"""
# 欢迎语，{} 会变成新入群用户的昵称
welcome_text = '''🎉 欢迎 @{} 的加入！
😃 有问题请私聊 @Linux中国
'''

# 回复语，在发送群邀请后会回复这个
reply_text = """你好，欢迎加入我们群XXX
群规是XXX
"""

# 群名
group_name = '酒井测试'

"""
代码区，下方的内容不要修改
"""
from wxpy import *
import time
import re
import os
from wxpy.utils import start_new_thread
import platform
console_qr=(False if platform.system() == 'Windows' else True)
bot = Bot('bot.pkl', console_qr=console_qr)

target_group = bot.groups().search(group_name)[0]

print(group_name+" 群找到>>>")
print("targer_group",target_group)
# 打印所有群成员
for member in target_group:
    print(member)

def get_time():
    return str(time.strftime("%Y-%m-%d %H:%M:%S"))

def status():
    '''
    状态汇报
    '''
    status_text = get_time() + " 机器人目前在线,共有好友 【" + str(len(
        bot.friends())) + "】 群 【" + str(len(bot.groups())) + "】"
    return status_text
def _restart():
    '''
    重启机器人
    '''
    os.execv(sys.executable, [sys.executable] + sys.argv)

def heartbeat():
    '''
    定时报告进程状态
    '''
    while bot.alive:
        time.sleep(3600)
        # noinspection PyBroadException
        try:
            #logger.error(status())
            print(status())
        except ResponseError as e:
            if 1100 <= e.err_code <= 1102:
                _restart()

start_new_thread(heartbeat)

'''
邀请消息处理
'''
def get_new_member_name(msg):
    # itchat 1.2.32 版本未格式化群中的 Note 消息
    from itchat.utils import msg_formatter
    msg_formatter(msg.raw, 'Text')

    for rp in rp_new_member_name:
        match = rp.search(msg.text)
        if match:
            return match.group(1)
'''
邀请信息处理
'''
rp_new_member_name = (
    re.compile(r'^"(.+)"通过'),
    re.compile(r'邀请"(.+)"加入'),
)

'''
处理加好友请求信息。
如果验证信息文本是字典的键值之一，则尝试拉群。
'''
@bot.register(msg_types=FRIENDS)
def new_friends(msg):
    user = msg.card.accept()
    target_group.add_members(user,use_invitation=True)
    user.send(reply_text)

@bot.register(target_group, NOTE)
def welcome(msg):
    name = get_new_member_name(msg)
    if name:
        return welcome_text.format(name)

# 打印出所有群聊中@自己的文本消息，并自动回复相同内容
# 这条注册消息是我们构建群聊机器人的基础
# 打印所有*群聊*对象中的*文本*消息
@bot.register(target_group, TEXT)
def print_group_msg1(msg):
    print(msg)
    msg.reply("机器人发送的消息：" + get_time())
    if msg.is_at:
        print(msg)
        msg.reply(msg.text)


embed()
