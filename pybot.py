
'''
MIT License

Copyright (c) 2017 p4rrot

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

import json 
import requests

TOKEN = ''
try:
    TOKEN = open("token.config","r").read()
except:
    TOKEN = raw_input("[!] Enter your Token : ")
URL = "https://api.telegram.org/bot{}/".format(TOKEN)

def get(url,method):
    response = requests.get(url+method)
    decoded_content = response.content.decode("utf8")
    out_put = json.loads(decoded_content)
    return out_put

methods = {
    "getUpdates":['offset','limit','timeout','allowed_updates'],
    "setWebhook":[('url'),'certificate','max_connections','allowed_updates'],
    "deleteWebhook":True,
    "getWebhookInfo":True,
    "sendMessage":[('chat_id','text'),'parse_mode',
                                    'disable_web_page_preview',
                                    'disable_notification',
                                    'reply_to_message_id',
                                    'reply_markup'],
    "getMe":True,
    "forwardMessage":[('chat_id','from_chat_id','message_id'),
                                   'disable_notification'],
    "sendPhoto":[('chat_id','photo'),'caption',
                                    'disable_notification',
                                    'reply_to_message_id',
                                    'reply_markup'],
    "sendAudio":[('chat_id','audio'),'caption',
                                'duration','performer','title',
                                'disable_notification',
                                'reply_to_message_id','reply_markup'],
    "sendDocument":[('chat_id','document'),'caption',
                                   'disable_notification',
                                'reply_to_message_id','reply_markup'],
    'sendSticker':[('chat_id','sticker'),'caption',
                                   'disable_notification',
                                'reply_to_message_id','reply_markup'],
    'sendVideo':[('chat_id','video'),'caption',
                                    'duration','width','height',
                                    'disable_notification',
                                    'reply_to_message_id',
                                    'reply_markup'],
    'sendVoice':[('chat_id','voice'),'caption',
                                    'duration',
                                    'disable_notification',
                                    'reply_to_message_id',
                                    'reply_markup'],
    'sendVideoNote':[('chat_id','video_note'),'length',
                                    'duration',
                                    'disable_notification',
                                    'reply_to_message_id',
                                    'reply_markup'],
    'sendVideoNote':[('chat_id','video_note'),'length',
                                    'duration',
                                    'disable_notification',
                                    'reply_to_message_id',
                                    'reply_markup'],
    'sendLocation':[('chat_id','latitude','longitude'),
                                    'disable_notification',
                                    'reply_to_message_id',
                                    'reply_markup'],
    'sendVenue':[('chat_id','latitude','longitude',
                                    'title','address'),
                                    'foursquare_id',
                                    'disable_notification',
                                    'reply_to_message_id',
                                    'reply_markup'],
    'sendContact':[('chat_id','phone_number',
                                    'first_name'),
                                    'last_name',
                                    'disable_notification',
                                    'reply_to_message_id',
                                    'reply_markup'],
    'sendChatAction':[('chat_id','action')],
    'getUserProfilePhotos':[('user_id'),'offset','limit'],
    'getFile':[('file_id')],
    'kickChatMember':[('chat_id','user_id'),'until_date'],
    'unbanChatMember':[('chat_id','user_id')],
    'restrictChatMember':[('chat_id','user_id'),'until_date',
                          'can_send_messages','can_send_media_messages',
                          'can_send_other_messages','can_add_web_page_previews'],
    'promoteChatMember': [('chat_id','user_id'),'can_change_info',
                          'can_post_messages','can_edit_messages',
                          'can_delete_messages','can_invite_users',
                          'can_restrict_members','can_pin_messages',
                          'can_promote_members'],
    'exportChatInviteLink':[('chat_id')],
    'setChatPhoto':[('chat_id','photo')],
    'deleteChatPhoto':[('chat_id')],
    'setChatTitle':[('chat_id','title')],
    'setChatDescription':[('chat_id'),'description'],
    'pinChatMessage':[('chat_id','message_id'),'disable_notification'],
    'unpinChatMessage':[('chat_id')],
    'leaveChat':[('chat_id')],
    'getChat':[('chat_id')],
    'getChatAdministrators':[('chat_id')],
    'getChatMembersCount':[('chat_id')],
    'getChatMember':[('chat_id','user_id')],
    'editMessageText':[('text'),'chat_id','message_id','inline_message_id',
                       'parse_mode','disable_web_page_preview','reply_markup'],
    'editMessageCaption':['chat_id','message_id','inline_message_id','caption',
                          'reply_markup'],
    'editMessageReplyMarkup':['chat_id','message_id','inline_message_id',
                          'reply_markup'],
    'deleteMessage':[('chat_id','message_id')]
    }
def list_of_available_methods():
    list_ = ''
    for method in methods:
        list_ += method +' - '+str(methods[method])+'\n'
    list_+= """
    [*] In parentheses fields are requiered 
    [*] Methods and their values are seprated by " -" 
    Example : sendMessage -text -hello world -chat_id -17890345
    """
    return list_
def make_method_available_to_get(method):
    method = method.split(' -')
    root_method = method[0]+'?'
    args = method[1:]
    args = dict(zip(*[iter(args)]*2))
    final_method = root_method
    for arg in args:
        final_method+=arg+"="+args[arg]+'&'
    return final_method
def run(command):
    method = make_method_available_to_get(command)
    print get (URL,method)
def execute(file='commands.exec'):
    SUCCESS = False
    while SUCCESS!=True:
        try:
            commands = open(file,'r').readlines()
            SUCCESS = True
            for command in commands:
                run (command)
        except:file=raw_input("[!] enter name of the file : ")
def try_to_config(token):
    url = "https://api.telegram.org/bot{}/".format(token)
    conf = get(url,'getUpdates')
    if conf['ok']==False:
        while conf['ok']!=True:
            print "[!] Token Invalid ."
            token = raw_input("[!] Enter your Token : ")
            url = "https://api.telegram.org/bot{}/".format(token)
            conf = get(url,'getUpdates')
def main():
    try_to_config (TOKEN)
    while True:
        command = raw_input("*pybot*: ")
        if command=="exit":break
        elif not command or command=='\n':pass
        elif command=="list":print list_of_available_methods ()
        elif command[:7]=="execute":
            if len(command)>9:
                execute(file=command.split(' -')[1])
            else:
                execute()
        else:
            run (command)
            if out_put['ok']==False:
                "[!] instruction was wrong . Enter 'list' to see commands ."
if __name__=="__main__":
    main()