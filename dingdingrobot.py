from dingtalkchatbot.chatbot import DingtalkChatbot
import time
import sys

time.strftime('%Y-%m-%d %H:%M:%S')
# WebHook地址
webhook = 'https://oapi.dingtalk.com/robot/send?access_token=19caf6fcaef3969d597493a15c42bebe31ccc2b8989a08534a8ff642f462cc9a'
# 初始化机器人小丁
xiaoding = DingtalkChatbot(webhook)
# Text消息@所有人
xiaoding.send_text(msg=sys.argv[1]+time.strftime('%Y-%m-%d %H:%M:%S'), is_at_all=True)
xiaoding.send_text(msg='大家好，周四例会请提前准备 '+'北京时间：'+time.strftime('%Y-%m-%d %H:%M:%S'), is_at_all=True)