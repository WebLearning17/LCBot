#coding:UTF-8
'''
token:
576906184:AAHGCJWmXTorMfuzZP5BNCDdQF57qPgUKnY

roadAheadBot
554056519:AAGz0Rc1gSiqxaPdjPhGcM6qU8CgTH42usM

curl -X POST "https://api.telegram.org/576906184:AAHGCJWmXTorMfuzZP5BNCDdQF57qPgUKnY/sendMessage" -d "chat_id=-groupTest&text=my sample text"

'''
#import telebot

from telebot import *

TOKEN="576906184:AAHGCJWmXTorMfuzZP5BNCDdQF57qPgUKnY"
bot=TeleBot(TOKEN)

#getUpdates
#updates = bot.get_updates()

print("bot getME:",bot.get_me())
#定义接受 / start 和命令的消息处理函数，如果多个命令都用这一个函数处理，就这样['start','help']
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, '大家好，我是机器人')

#定义接受所有消息的处理函数
@bot.message_handler()
def echo(message):
    print("11111")
    bot.send_message(message.chat.id, str(message.message_id)+" 发消息了！")
    bot.reply_to(message, message.text)

#另一种 reply_to
@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.send_message(reply_to_message_id=message.message_id, chat_id=message.chat.id, text='有什么可以帮您')

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    print("333333")
    bot.reply_to(message, message.text)

def listener(messages):
    for m in messages:
        print (str(m))
if __name__ == '__main__':

    print(bot.get_chat(chat_id=-1001180626953))  #groupTest  -1001180626953
    bot.set_update_listener(listener)
    #机器人发送消息
    #bot.send_message(-1001180626953, "机器人上线")
    ch = bot.get_chat(-1001180626953)

    print ("结束")
    bot.polling()
