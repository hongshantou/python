#!/usr/bin/env python
# coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding( "utf8" )

import itchat
from itchat.content import *

#@itchat.msg_register(itchat.content.TEXT)
#def text_reply(msg):
#    return msg['Text']


# �Զ��ظ��ı��������Ϣ
# isGroupChat=False��ʾ��Ⱥ����Ϣ
@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING], isGroupChat=False)
def text_reply(msg):
	#print "here we are!"
	itchat.send('�Ժ������ظ�!', msg['FromUserName'])

# �Զ��ظ�ͼƬ�������Ϣ
# isGroupChat=False��ʾ��Ⱥ����Ϣ
@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO], isGroupChat=False)
def download_files(msg):
	itchat.send('�Ժ������ظ���', msg['FromUserName'])

# �Զ�������Ӻ�������
@itchat.msg_register(FRIENDS)
def add_friend(msg):
	itchat.add_friend(**msg['Text']) # �ò������Զ����º��ѵ���Ϣ¼�룬����Ҫ����ͨѶ¼
	itchat.send_msg(u'����', msg['RecommendInfo']['UserName'])
    
# �Զ��ظ��ı�������Ⱥ����Ϣ
# isGroupChat=True��ʾΪȺ����Ϣ
@itchat.msg_register([TEXT, SHARING], isGroupChat=True)
def group_reply_text(msg):
	# ��Ϣ�������ĸ�Ⱥ��
	chatroom_id = msg['FromUserName']

	# ��Ϣ��������������Ҫͬ����Ⱥ
	if not chatroom_id in chatroom_ids:
		return

	#print "chatroom_id" + chatroom_id
	# �����ߵ��ǳ�
	username = msg['ActualNickName']
	#print "username",username
	#��ȡȺ��
	#print 11111, chatrooms_rename
	group_name= chatrooms_rename.get(chatroom_id)
	#print group_name

	if msg['Type'] == TEXT:
		content = msg['Content']
		#print 1
	elif msg['Type'] == SHARING:
		content = msg['Text']
		#print 2

	# ������Ϣ����ת����������Ҫͬ����Ϣ��Ⱥ��
	if msg['Type'] == TEXT:
		for item in chatrooms:
			#print 3
			if not item['UserName'] == chatroom_id:
				#print 4
				itchat.send('%s��%s ˵:\n%s' % (group_name,username, msg['Content']), item['UserName'])
	elif msg['Type'] == SHARING:
		#print 5
		for item in chatrooms:
			if not item['UserName'] == chatroom_id:
				itchat.send('%s-%s ����\n%s\n%s' % (group_name,username, msg['Text'], msg['Url']), item['UserName'])

# �Զ��ظ�ͼƬ������Ⱥ����Ϣ
# isGroupChat=True��ʾΪȺ����Ϣ          
@itchat.msg_register([PICTURE, ATTACHMENT, VIDEO], isGroupChat=True)
def group_reply_media(msg):
	# ��Ϣ�������ĸ�Ⱥ��
	chatroom_id = msg['FromUserName']
	# �����ߵ��ǳ�
	username = msg['ActualNickName']

	# ��Ϣ��������������Ҫͬ����Ⱥ
	if not chatroom_id in chatroom_ids:
		return

	# ���ΪgifͼƬ��ת��
	if msg['FileName'][-4:] == '.gif':
		return

	# ����ͼƬ���ļ�
	msg['Text'](msg['FileName'])
	# ת����������Ҫͬ����Ϣ��Ⱥ��
	for item in chatrooms:
		if not item['UserName'] == chatroom_id:
			itchat.send('@%s@%s' % ({'Picture': 'img', 'Video': 'vid'}.get(msg['Type'], 'fil'), msg['FileName']), item['UserName'])

# ɨ��ά���¼
#itchat.auto_login(hotReload=False)
itchat.auto_login(hotReload=True)
# ��ȡ����ͨѶ¼�е�Ⱥ��
# ��Ҫ��΢���н���Ҫͬ����Ⱥ�Ķ�������ͨѶ¼
chatrooms = itchat.get_chatrooms(update=True, contactOnly=True)
chatroom_ids = [c['UserName'] for c in chatrooms]
#chatroom_rename={}
print '���ڼ���Ⱥ�ģ�', len(chatrooms), '��'
#����Ⱥ�� ��  ����Ⱥ+i
i=2
#for k in chatrooms.keys():
chatrooms_rename={}
for item in chatrooms:
	chatrooms_rename[str(item['UserName'])]="Group"+str(i)
	#print item['NickName']
	#print item['UserName']
	#print "����Ⱥ"+str(i)
	#item['Nickname']=str(i)


	i=i-1
	print item['NickName']
	print chatrooms_rename[item['UserName']]
#��������֮���Ⱥ��
print str(chatrooms_rename)
#ԭʼȺ��
print ' '.join([item['NickName'] for item in chatrooms])
# ��ʼ���
itchat.run()