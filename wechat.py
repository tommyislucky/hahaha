

from __future__ import unicode_literals

from wxpy import *
from wechat_sender import listen
bot = Bot(console_qr=True,cache_path=True)
my = bot.friends()
'''
my1 = bot.friends().search('吴震')[0]
my2 = bot.friends().search('吴明')[0]
my3 = bot.friends().search('朱依心')[0]
'''
@bot.register(Friend)
def reply_test(msg):
    msg.reply('欢迎关注，更多内容请关注公众号--SQuant')

@bot.register(msg_types=FRIENDS)
def auto_accept_friends(msg):
    if 'sigma' in msg.text.lower():
        new_friend = bot.accept_friend(msg.card)
        new_friend.send('sigma小助手为您服务')

listen(bot,receivers=my,port=10001)
