# #coding:utf-8

# import ampalibe
# from conf import Configuration
# from ampalibe import Payload
# from ampalibe.ui import Button,QuickReply
# from eval import isMatched
# import requests
# import json
# from converters import *
# from utils import *
# bot = ampalibe.init(Configuration())
# chat = bot.chat
# query = bot.query


# @ampalibe.command('/')
# def main(sender_id, cmd, **extends):
#     chat.get_started()
#     main_menu = [
#         QuickReply(
#             title="Rechercher",
#             payload="/search",
#             image_url="https://png.pngtree.com/element_our/20190528/ourlarge/pngtree-magnifying-glass-icon-image_1128382.jpg"
#         ),
#         QuickReply(
#             title="Parcourir",
#             payload="/browse",
#             image_url="https://as1.ftcdn.net/v2/jpg/02/22/48/10/1000_F_222481041_rgdvImQWWbxt8TCivbt8hwspuQ11uOQc.jpg"

#         )
#     ]
#     chat.send_quick_reply(sender_id, main_menu, "Tongasoa")
# # vita 

# @ampalibe.command("/search")
# def search(sender_id, cmd, **extends):
#     render_search_syntax(sender_id, chat)
#     query.set_action(sender_id, "/retrieve_search")

# @ampalibe.command("/browse")
# def goto(sender_id, cmd, **extends):
#     buttons = [
#         Button(
#             type='postback',
#             title='Testameta taloha',
#             payload= Payload('/testament', type="ancient")
#         ),
#         Button(
#             type='postback',
#             title='Testameta vaovao',
#             payload= Payload('/testament', type="new")
#         ),   
#     ]  
#     chat.send_button(sender_id, buttons, "Testameta") 

# @ampalibe.command("/testament")
# def get_ancient_list(sender_id, cmd, type, **extends):
#     response = requests.get("http://127.0.0.1:7000/mg/get/"+type)
#     data = response.text
#     data_dict = json.loads(data)
#     showlist(sender_id, chat, data_dict)

# @ampalibe.command("/showasmessage")
# def showmessage(sender_id, cmd, versets, **extends):
#     chat.send_message(sender_id, versets)

# @ampalibe.command("/showaspdf")
# def getpdf(sender_id, cmd, versets, **extends):
#     name = query.get_temp(sender_id, "versets")
#     path = storeaspdf(name, versets)
#     chat.send_file(sender_id, path)

# @ampalibe.command("/showastextfile")
# def gettextfile(sender_id, cmd, versets, **extends):
#     name = query.get_temp(sender_id, "versets")
#     path = storeastext(name, versets)
#     chat.send_file(sender_id, path[0])

# @ampalibe.command("/showaspng")
# def getpng(sender_id, cmd, versets, **extends):
#     name = query.get_temp(sender_id, "versets")
#     if not findtextfile(name):
#         new_file = storeastext(name, versets)
#         name = new_file[1]
#     path = storeaspng(name, versets)
#     chat.send_file(sender_id, path)

# @ampalibe.action("/retrieve_search")
# def retrieve_search(sender_id, cmd, **extends):
#     query.set_action(sender_id, None)
#     if not isMatched(cmd):
#         chat.send_message(sender_id, "verifier bien la syntaxe")
#         give_back_way(sender_id, chat)
#     else:
#         query.set_temp(sender_id, "versets", cmd.replace(" ",""))
#         response = requests.get("http://127.0.0.1:7000/mg/"+cmd)
#         data = response.text
#         data_dict = json.loads(data)
#         versetstext = ""
#         for toko in data_dict:
#             versetstext = versetstext + toko+". "+data_dict[toko]
#         options_upload(sender_id, chat, versetstext)
        
    

from controller.app import *