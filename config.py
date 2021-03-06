#!/usr/bin/env python3
# coding: utf-8
'''
定义管理员群的名称

在该群内的人都将被设为管理员，
管理员在被管理的群中享有高级管理权限，可进行如踢人等的操作
注：群名为部分匹配，请尽量输入全名以保证搜索到的群的唯一性
'''
admin_group_name = '酒井测试'#'机器人管理群'

'''
定义被管理群的群名前缀
所有以此为前缀的群都将设为被管理的群
注：前缀大小写敏感

如：设定为'Linux中国◆'，则将自动搜索到
「Linux中国◆微信机器人群」「Linux中国◆LFS群」等以其为开头的群，
并将其设为被管理的群
'''
#group_prefix = '机器人'
group_prefix="酒井测试"   #被管理的群
'''
定义非特定前缀的群

注：必须输入完整名称
'''
additional_groups = ('另一个机器人群', )

# 新人入群的欢迎语
welcome_text = '''🎉 欢迎 @{} 的加入！
😃 有问题请私聊我。
'''

invite_text = """欢迎您，我是测试微信群助手，您现在收到的是来自机器人的消息"""


'''
设置群组关键词和对应群名
* 关键词必须为小写，查询时会做相应的小写处理

关于随机加群功能：
针对同类的群有多个的场景，例如群名 LFS群1、LFS群2、LFS群3...
设置关键词字典如下：
keyword_of_group = {
    "lfs":"LFS群",
}
机器人会以"LFS群"为群名搜索，搜索结果为同类群名的列表，
再从列表中随机选取一个发出加群邀请。
'''
keyword_of_group = {
    "测试": "酒井测试",
}

'''
地区群
'''
city_group = {
    "北京": "酒井测试",
}

#keyword_of_group.update(city_group)

female_group = "机器人测试群"

alert_group = '酒井测试'#"机器人测试群"

turing_key = ''

# 以下为功能配置选项
'''
全局静默开关
'''
silence_mode = False
