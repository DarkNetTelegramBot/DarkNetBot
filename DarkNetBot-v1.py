# BackTrack
# python3
# DarkNetTelegramBot ID = @Dark_net_program_bot

import telebot
import socket
import time 
import requests
from pyfiglet import figlet_format as fig
import builtwith
import base64
import random

token = "6103970028:AAEJKOuhzvR2s0S9cPEnVtyCtY42mvT9lHQ"
bot_time = time.strftime("%H:%M:%S  %y-%m-%d")
bot = telebot.TeleBot(token)
t = time.strftime("%H:%M:%S  %y-%m-%d")
user_token, user_chat_id, user_msg, ht = [],[],[],[]
print(f"launching bot with {token}\nat {t}")



@bot.message_handler(commands=['start'])
def start(msg):
    user_name = msg.from_user.username
    name = msg.from_user.first_name
    chat = msg.from_user.id
    bot.send_message(msg.chat.id, f"[*] Welcome to DarkNet Bot at {bot_time}\n\nYour Name => {name}\nuser name => {user_name}\nchat id => {chat}\n\n[!] for see options type /help ✅")
    
@bot.message_handler(commands=['help'])
def help_bot(msg):
    bot.send_message(msg.chat.id, f"ok we have some options in DarkNet Bot 🗿\n/start\n/help\n/time\nsay [anything]\nfont [text]\n\nuser factory : 👮‍♂️👮‍♀️\nmy info\nmy id / my chat id\nmy name / my first name \nmy username\nmy last name\n\nnetwork factory : 🌎\nget ip [domain name]\nscan site [https://example.com]\nbanner [text]\n\nencrypt factory : 🗯️\nb85encode [text]\nb64encode [text]\nb32encode [text]\nb16encode [text]\n\ndecrypt factory : 💬\nb85decode [text]\nb64decode [text]\nb32decode [text]\nb16decode [text]\n\ntelegram factory : 📱\nset token [bot token]\nset chat id [chat id]\nset message [text]\nrun / start for sending message\nclear token\nclear chat id\nclear message\nclear all\nshow token\nshow chat id\nshow message\nshow all\n\nPassword Creator Factory : 🔐\n/CreateKey or /Createkey or /createkey")
    
@bot.message_handler(commands=['time', 'date'])
def timer(msg):
    time_in_bot = time.strftime("%H:%M:%S  %y-%m-%d")
    bot.send_message(msg.chat.id, time_in_bot)
    
@bot.message_handler(commands=['CreateKey', 'Createkey', 'createkey'])
def create_key(msg):
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number = "0123456789"
    symbols = "@#$%&/\?"
    User_for = lower_case + upper_case + number + symbols
    nums = [7, 8, 9, 10 ,11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
    password = "".join(random.sample(User_for, random.choice(nums)))
    bot.send_message(msg.chat.id, password)
    
@bot.message_handler(content_types=['text'])
def say_to_me(msg):
    if msg.text.startswith("say"):
        say = str(msg.text).replace("say ", "")
        bot.send_message(msg.chat.id, say)
        
    elif msg.text.startswith("get ip"):
        target = str(msg.text).replace("get ip ","")
        try:
            start_time = time.time()
            site = socket.gethostbyname(target)
            end_time = time.time()
            bot.send_message(msg.chat.id, text=f"[+] domain name = {target}\n[+] host = {site}\n[+] mission end in = {end_time-start_time:.2f}")
        except:
            bot.send_message(msg.chat.id, text="[!] cannot connect to the server ! Please Try Again")
               
    elif msg.text.startswith("scan site"):
        sitea = str(msg.text).replace("scan site ", "")
        try:
            start = time.time()
            _info = builtwith.builtwith(sitea)
            end = time.time()
            bot.send_message(msg.chat.id, _info)
            bot.send_message(msg.chat.id ,"\n"+str(req)+f"mission end in : {end-start:.2f}")
        except:
            bot.send_message(msg.chat.id, text="[!] cannot connect to the server ! Please Try Again")
                
    elif msg.text.startswith("banner"):
        text = str(msg.text).replace("banner ", "")
        bot.send_message(msg.chat.id, text=fig(text=text))
        
    elif msg.text.startswith("font"):
        new_text = str(msg.text).replace("font ", "")
        def font(txt : str):
            txt = txt.lower()
            t_1 = txt.translate(txt.maketrans("qwertyuiopasdfghjklzxcvbnm", "Qᴡᴇʀᴛʏᴜɪᴏᴘᴀꜱᴅꜰɢʜᴊᴋʟᴢxᴄᴠʙɴᴍ"))
            t_2 = txt.translate(txt.maketrans("qwertyuiopasdfghjklzxcvbnm", "𝖖𝖜𝖊𝖗𝖙𝖞𝖚𝖎𝖔𝖕𝖆𝖘𝖉𝖋𝖌𝖍𝖏𝖐𝖑𝖟𝖝𝖈𝖛𝖇𝖓𝖒"))
            t_3 = txt.translate(txt.maketrans("qwertyuiopasdfghjklzxcvbnm", "𝔮𝔴𝔢𝔯𝔱𝔶𝔲𝔦𝔬𝔭𝔞𝔰𝔡𝔣𝔤𝔥𝔧𝔨𝔩𝔷𝔵𝔠𝔳𝔟𝔫𝔪"))
            t_4 = txt.translate(txt.maketrans("qwertyuiopasdfghjklzxcvbnm", "𝓺𝔀𝓮𝓻𝓽𝔂𝓾𝓲𝓸𝓹𝓪𝓼𝓭𝓯𝓰𝓱𝓳𝓴𝓵𝔃𝔁𝓬𝓿𝓫𝓷𝓶"))
            t_5 = txt.translate(txt.maketrans("qwertyuiopasdfghjklzxcvbnm", "🅀🅆🄴🅁🅃🅈🅄🄸🄾🄿🄰🅂🄳🄵🄶🄷🄹🄺🄻🅉🅇🄲🅅🄱🄽🄼"))
            t_6 = txt.translate(txt.maketrans("qwertyuiopasdfghjklzxcvbnm", "𝐪𝐰𝐞𝐫𝐭𝐲𝐮𝐢𝐨𝐩𝐚𝐬𝐝𝐟𝐠𝐡𝐣𝐤𝐥𝐳𝐱𝐜𝐯𝐛𝐧𝐦"))
            t_7 = txt.translate(txt.maketrans("qwertyuiopasdfghjklzxcvbnm", "𝗾𝘄𝗲𝗿𝘁𝘆𝘂𝗶𝗼𝗽𝗮𝘀𝗱𝗳𝗴𝗵𝗷𝗸𝗹𝘇𝘅𝗰𝘃𝗯𝗻𝗺"))
            t_8 = txt.translate(txt.maketrans("qwertyuiopasdfghjklzxcvbnm", "𝚚𝚠𝚎𝚛𝚝𝚢𝚞𝚒𝚘𝚙𝚊𝚜𝚍𝚏𝚐𝚑𝚓𝚔𝚕𝚣𝚡𝚌𝚟𝚋𝚗𝚖"))
            t_9 = txt.translate(txt.maketrans("qwertyuiopasdfghjklzxcvbnm", "QЩΣЯƬYЦIӨPΛƧDFGΉJKᄂZXᄃVBПM"))
            return (t_1, t_2, t_3, t_4, t_5, t_6, t_7, t_8, t_9)
        bot.send_message(msg.chat.id, font(txt=new_text))
    
        
    elif msg.text.startswith("b85encode"):
        txt = str(msg.text).replace("b85encode ","")
        main = base64.b85encode(txt.encode("ascii"))
        bot.send_message(msg.chat.id, main)
        
    elif msg.text.startswith("b64encode"):
        txt = str(msg.text).replace("b64encode ","")
        main = base64.b64encode(txt.encode("ascii"))
        bot.send_message(msg.chat.id, main)
    
    elif msg.text.startswith("b32encode"):
        txt = str(msg.text).replace("b32encode ","")
        main = base64.b32encode(txt.encode("ascii"))
        bot.send_message(msg.chat.id, main)
        
    elif msg.text.startswith("b16encode"):
        txt = str(msg.text).replace("b16encode ","")
        main = base64.b16encode(txt.encode("ascii"))
        bot.send_message(msg.chat.id, main)
        
    elif msg.text.startswith("b85decode"):
        txt = str(msg.text).replace("b85decode ","")
        main = base64.b85decode(txt.encode("utf-8"))
        bot.send_message(msg.chat.id, main)
        
    elif msg.text.startswith("b64decode"):
        txt = str(msg.text).replace("b64decode ","")
        main = base64.b64decode(txt.encode("utf-8"))
        bot.send_message(msg.chat.id, main)
        
    elif msg.text.startswith("b32decode"):
        txt = str(msg.text).replace("b32decode ","")
        main = base64.b32decode(txt.encode("utf-8"))
        bot.send_message(msg.chat.id, main)
    
    elif msg.text.startswith("b16decode"):
        txt = str(msg.text).replace("b16decode ","")
        main = base64.b16decode(txt.encode("utf-8"))
        bot.send_message(msg.chat.id, main)
    
    elif msg.text.startswith("set token"):
        tk = str(msg.text).replace("set token ", "")
        user_token.append(tk)
        bot.send_message(msg.chat.id, f"[+] token = {tk}\n[+] save in memory")
    
    elif msg.text.startswith("set chat id"):
        cht = str(msg.text).replace("set chat id ", "")
        user_chat_id.append(cht)
        bot.send_message(msg.chat.id, f"[+] chat id = {cht}\n[+] save in memory")
        
    elif msg.text.startswith("set message"):
        m = str(msg.text).replace("set message ", "")
        user_msg.append(m)
        bot.send_message(msg.chat.id, f"[+] message = {m}\n[+] save in memory")
        
    elif msg.text == "run" or msg.text == "start bot":
        tok = "".join(user_token)
        chat = "".join(user_chat_id)
        mes = "".join(user_msg)
        url = (f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={chat}&text={mes}")
        payload = {
            "UrlBox" : url,
            "AgentList" : "Google Chrome",
            "VersionList" : "HTTP/1.1",
            "MethodList" : "GET"
        }
        try:
            start_run = time.time()
            req = requests.post("https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx", payload)
            end_run = time.time()
            bot.send_message(msg.chat.id, text=f"[+] Message Sended\n[+] Token = {tok}\n[+] Chat ID = {chat}\n[+] Message = {mes}\n[+] End Mission in {end_run-start_run:.2f}")
        
        except:
            bot.send_message(msg.chat.id, text="[!] cannot connect to the server ! Please Try Again")
    
    elif msg.text == "clear token":
        user_token.clear()
        bot.send_message(msg.chat.id, "token list is clear\nyou can set a new token with { set token [token] }")
    
    elif msg.text == "clear chat id":
        user_chat_id.clear()
        bot.send_message(msg.chat.id, "chat id list is clear\nyou can set a new chat id with { set chat id [chat id] }")
    
    elif msg.text == "clear message":
        user_msg.clear()
        bot.send_message(msg.chat.id, "message list is clear\nyou can set a new message with { set message [message] }")
        
    elif msg.text == "clear all":
        user_token.clear()
        user_chat_id.clear()
        user_msg.clear()
        bot.send_message(msg.chat.id, text="all lists was clear")
        
    elif msg.text == "show token":
        bot.send_message(msg.chat.id, text=f"[+] Tokens = {user_token}")
    
    elif msg.text == "show chat id":
        bot.send_message(msg.chat.id, text=f"[+] Chat IDS = {user_chat_id}")
        
    elif msg.text == "show message":
        bot.send_message(msg.chat.id, text=f"[+] Messages = {user_msg}")
        
    elif msg.text == "show all":
        bot.send_message(msg.chat.id, text=f"[+] Tokens = {user_token}")
        bot.send_message(msg.chat.id, text=f"[+] Chat IDS = {user_chat_id}")
        bot.send_message(msg.chat.id, text=f"[+] Messages = {user_msg}")
        
    elif msg.text == "my id" or msg.text == "my chat id":
        chat = msg.from_user.id
        bot.send_message(msg.chat.id, chat)
    
    elif msg.text == "my first name" or msg.text == "my name":
        name = msg.from_user.first_name
        bot.send_message(msg.chat.id, name)

    elif msg.text == "my username":
        user_name = msg.from_user.username
        bot.send_message(msg.chat.id, user_name)
        
    elif msg.text == "my last name":
        last_name = msg.from_user.last_name
        bot.send_message(msg.chat.id, last_name)
        
    elif msg.text == "my info":
        user_name = msg.from_user.username
        name = msg.from_user.first_name
        second_name = msg.from_user.last_name
        chat = msg.from_user.id
        bot.send_message(msg.chat.id, text=f"first name => {name}\nlast name => {second_name}\nuser name => @{user_name}\nchat id => {chat}")
    
bot.infinity_polling()
