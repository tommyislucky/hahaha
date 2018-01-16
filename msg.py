# coding: utf-8
from wechat_sender import Sender

ff = open('friends.txt')
aaa=ff.read()

Sender(receivers=aaa,port=10005).send("13、17、19、21点自动推送，注意设置微信消息弹出")
