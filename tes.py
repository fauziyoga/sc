# -*- coding: utf-8 -*-

from LineAPI.linepy import *
from multiprocessing import Pool, Process
#from LineAPI.thrift.protocol import TCompactProtocol
#from LineAPI.thrift.transport import THttpClient
#from LineAPI.linepy import LoginRequest
#from urllib.parse import urlencode
#from random import randint
from shutil import copyfile
#import LineService
#import subprocess as cmd
from time import sleep
#from gtts import gTTS
from bs4 import BeautifulSoup
from datetime import datetime
#from googletrans import Translator
import ast, codecs, json, pafy, os, pytz, re, random, requests, sys, time, shutil, threading, glob, re, base64, string, os, requests, six, ast, pytz, wikipedia, urllib.parse, atexit, asyncio, traceback
import youtube_dl
_session = requests.session()
import threading
try:
	with open('token2.txt','r') as lg:
		tkn = lg.read()
		client = LINE(tkn)
except:
	client = LINE()
	with open('token2.txt','w') as lg:
		lg.write(client.authToken)
#client = LINE()
#channel = Channel(client, client.server.CHANNEL_ID['JUNGEL_PANG'])
#channelToken = channel.getChannelResult()
clientMid = client.profile.mid
clientStart = time.time()
clientPoll = OEPoll(client)
admin = ["uc6439bb55704ed7e865499ce68536704"]
myAdmin = ["uc6439bb55704ed7e865499ce68536704"]
creator = ["uc6439bb55704ed7e865499ce68536704"]
owner = ["uc6439bb55704ed7e865499ce68536704"]
tokenz = {}
simisimi = []

settings = {
    "simiSimi": {},
    "autoResponGC": " @! t",
    "autoResponGC2": " @! e",
    "autoResponGC3": " @! t",
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ]
}

wait =  {
    "leaveMessage": True,
    "autoLike": False,
    "messageLv": "Goodbye @! ",
    "sider": "Cie yang lagi ngintip",
    "ChangeVideoProfilevid":{},
    "ChangeVideoProfilePicture":{}
}

simi2 = {
    "simi-simi":{}
}

settings = {
    "simiSimi":{}
}

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

cctv2 = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

chatbot = {
    "admin": [],
    "botMute": [],
    "botOff": []
}



languageOpen = codecs.open("language.json","r","utf-8")
readOpen = codecs.open("read.json","r","utf-8")
settingsOpen = codecs.open("setting.json","r","utf-8")
unsendOpen = codecs.open("unsend.json","r","utf-8")
tokenOpen = codecs.open("toket.json","r","utf-8")
premiumOpen = codecs.open("user.json","r","utf-8")

language = json.load(languageOpen)
read = json.load(readOpen)
settings = json.load(settingsOpen)
unsend = json.load(unsendOpen)
token = json.load(tokenOpen)
premium = json.load(premiumOpen)


def restartBot():
	print ("[ INFO ] BOT RESETTED")
	python = sys.executable
	os.execl(python, python, *sys.argv)

def logError(text):
    client.log("[ ERROR ] {}".format(str(text)))
    tz = pytz.timezone("Asia/Makassar")
    timeNow = datetime.now(tz=tz)
    timeHours = datetime.strftime(timeNow,"(%H:%M)")
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    inihari = datetime.now(tz=tz)
    hr = inihari.strftime('%A')
    bln = inihari.strftime('%m')
    for i in range(len(day)):
        if hr == day[i]: hasil = hari[i]
    for k in range(0, len(bulan)):
        if bln == str(k): bln = bulan[k-1]
    time = "{}, {} - {} - {} | {}".format(str(hasil), str(inihari.strftime('%d')), str(bln), str(inihari.strftime('%Y')), str(inihari.strftime('%H:%M:%S')))
    with open("errorLog.txt","a") as error:
        error.write("\n[{}] {}".format(str(time), text))
        

def siderMembers(to, mid):
    try:
        arrData = ""
        textx = "Haii ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@pikachu\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+settings["mention"]
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(client.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"        
        client.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        client.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def timeChange(secs):
	mins, secs = divmod(secs,60)
	hours, mins = divmod(mins,60)
	days, hours = divmod(hours,24)
	weeks, days = divmod(days,7)
	months, weeks = divmod(weeks,4)
	text = ""
	if months != 0: text += "%02d Bulan" % (months)
	if weeks != 0: text += " %02d Minggu" % (weeks)
	if days != 0: text += " %02d Hari" % (days)
	if hours !=  0: text +=  " %02d Jam" % (hours)
	if mins != 0: text += " %02d Menit" % (mins)
	if secs != 0: text += " %02d Detik" % (secs)
	if text[0] == " ":
		text = text[1:]
	return text

def convertYoutubeMp4(url):
	video = pafy.new(url, basic=False)
	result = video.streams[-1]
	return result.url

def convertYoutubeMp3(url):
	video = pafy.new(url, basic=False)
	result = video.audiostreams[-1]
	return result.url

def command(text):
	pesan = text.lower()
	if settings["setKey"] == True:
		if pesan.startswith(settings["keyCommand"]):
			cmd = pesan.replace(settings["keyCommand"],"")
		else:
			cmd = "Undefined command"
	else:
		cmd = text.lower()
	return cmd
	
def removeCmd(cmd, text):
	key = settings["keyCommand"]
	if settings["setKey"] == False: key = ''
	rmv = len(key + cmd) + 1
	return text[rmv:]

def backupData():
	try:
		backup = read
		f = codecs.open('read.json','w','utf-8')
		json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
		backup = settings
		f = codecs.open('setting.json','w','utf-8')
		json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
		backup = unsend
		f = codecs.open('unsend.json','w','utf-8')
		json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
		backup = premium
		f = codecs.open('user.json','w','utf-8')
		json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
		return True
	except Exception as error:
		logError(error)
		return False

def menuHelp():
	if settings['setKey'] == True:
		key = settings['keyCommand']
	else:
		key = ''
	menuHelp =	"╭─「 Help Message 」" + "\n" + \
				"│ " + key + "Self" + "\n" + \
                "│ " + key + "Group" + "\n" + \
                "│ " + key + "Media" + "\n" + \
                "│ " + key + "Tagall" + "\n" + \
				"│ " + key + "Lurking 「On/Off」" + "\n" + \
				"│ " + key + "Lurking" + "\n" + \
				"│ " + key + "Sider 「On/Off」" + "\n" + \
				"│ " + key + "Reader 「On/Off」" + "\n" + \
                "│ " + key + "Bot bye" + "\n" + \
				"╰─────────────"
	return menuHelp

def menuHelp1():
	if settings['setKey'] == True:
		key = settings['keyCommand']
	else:
		key = ''
	menuHelp1 =	"╭─「 Self Command 」" + "\n" + \
                "│ " + key + "Me" + "\n" + \
				"│ " + key + "MyMid" + "\n" + \
				"│ " + key + "MyName" + "\n" + \
				"│ " + key + "MyBio" + "\n" + \
				"│ " + key + "MyPicture" + "\n" + \
				"│ " + key + "MyVideoProfile" + "\n" + \
				"│ " + key + "MyCover" + "\n" + \
				"│ " + key + "MyProfile" + "\n" + \
				"│ " + key + "GetMid @Mention" + "\n" + \
				"│ " + key + "GetName @Mention" + "\n" + \
				"│ " + key + "GetBio @Mention" + "\n" + \
				"│ " + key + "GetPicture @Mention" + "\n" + \
				"│ " + key + "GetVideoProfile @Mention" + "\n" + \
				"│ " + key + "GetCover @Mention" + "\n" + \
                "│ " + key + "StealCover「Mention」" + "\n" + \
                "│ " + key + "Cari「Mention」" + "\n" + \
                "╰─────────────"
	return menuHelp1

def menuHelp2():
	if settings['setKey'] == True:
		key = settings['keyCommand']
	else:
		key = ''
	menuHelp2 =	"╭─「 Group Command 」" + "\n" + \
                "│ " + key + "GroupCreator" + "\n" + \
				"│ " + key + "GroupID" + "\n" + \
				"│ " + key + "GroupName" + "\n" + \
				"│ " + key + "GroupPicture" + "\n" + \
				"│ " + key + "MemberList" + "\n" + \
				"│ " + key + "PendingList" + "\n" + \
				"│ " + key + "GroupInfo" + "\n" + \
                "╰─────────────"
	return menuHelp2

def helpmessage3():
	if settings['setKey'] == True:
		key = settings['keyCommand']
	else:
		key = ''
	helpmessage3 ="╭─「 Special Command 」" + "\n" + \
                "│ " + key + "Mimic 「On/Off」" + "\n" + \
				"│ " + key + "MimicList" + "\n" + \
				"│ " + key + "MimicAdd @Mention" + "\n" + \
				"│ " + key + "MimicDel @Mention" + "\n" + \
				"│ " + key + "Tagall" + "\n" + \
				"│ " + key + "Lurking 「On/Off」" + "\n" + \
				"│ " + key + "Lurking" + "\n" + \
				"│ " + key + "Sider 「On/Off」" + "\n" + \
				"│ " + key + "Bot bye" + "\n" + \
				"│ " + key + "Likepost @Mention" + "\n" + \
                "╰─────────────"
	return helpmessage3

def helpmessage4():
	if settings['setKey'] == True:
		key = settings['keyCommand']
	else:
		key = ''
	helpmessage4 ="╭─「 Media Command 」" + "\n" + \
                "│ " + key + "InstaInfo 「Username」" + "\n" + \
				"│ " + key + "Quote" + "\n" + \
				"│ " + key + "Img 「Search」" + "\n" + \
				"│ " + key + "SearchLyric 「Search」" + "\n" + \
				"│ " + key + "SearchYoutube 「Search」" + "\n" + \
				"│ " + key + "Musik 「Penyanyi」" + "\n" + \
				"│ " + key + "Scloud 「Search」" + "\n" + \
				"│ " + key + "Fwindow: 「Text」" + "\n" + \
				"│ " + key + "Lgraffiti: 「Text」" + "\n" + \
				"│ " + key + "Animeongoing" + "\n" + \
				"│ " + key + "Cuaca 「Kota」" + "\n" + \
				"│ " + key + "Instapict 「Link」" + "\n" + \
				"│ " + key + "Instavideo 「Link」" + "\n" + \
				"│ " + key + "Asking 「Text」" + "\n" + \
				"│ " + key + "Idline 「Userid」" + "\n" + \
				"│ " + key + "Tiktok" + "\n" + \
				"│ " + key + "Ytmp4 「Link」" + "\n" + \
				"│ " + key + "Ytmp3 「Link」" + "\n" + \
				"│ " + key + "Ytmp3: 「Search」" + "\n" + \
				"│ " + key + "Devianart 「Search」" + "\n" + \
				"│ " + key + "Chatowner: 「text」" + "\n" + \
                "╰─────────────"
	return helpmessage4

def helpmessage5():
	if settings['setKey'] == True:
		key = settings['keyCommand']
	else:
		key = ''
	helpmessage5 ="╭─「 Settings Command 」" + "\n" + \
                "│ " + key + "AutoAdd 「On/Off」" + "\n" + \
				"│ " + key + "AutoJoin 「On/Off」" + "\n" + \
				"│ " + key + "AutoJoinTicket 「On/Off」" + "\n" + \
				"│ " + key + "AutoRead 「On/Off」" + "\n" + \
				"│ " + key + "AutoRespon 「On/Off」" + "\n" + \
				"│ " + key + "CheckContact 「On/Off」" + "\n" + \
				"│ " + key + "CheckPost 「On/Off」" + "\n" + \
				"│ " + key + "CheckSticker 「On/Off」" + "\n" + \
				"│ " + key + "DetectUnsend 「On/Off」" + "\n" + \
				"│ " + key + "SetKey: 「text」" + "\n" + \
				"│ " + key + "SetAutoAddMessage: 「text」" + "\n" + \
				"│ " + key + "SetAutoResponMessage: 「text」" + "\n" + \
				"│ " + key + "SetAutoJoinMessage: 「Text」" + "\n" + \
                "╰─────────────"
	return helpmessage5

def clientBot(op):
	try:
		if op.type == 0:
			print ("[ 0 ] END OF OPERATION")
			return

		if op.type == 5:
			print ("[ 5 ] NOTIFIED ADD CONTACT")
			if settings["autoAdd"] == True:
				client.findAndAddContactsByMid(op.param1)
			client.sendMention(op.param1, settings["autoAddMessage"], [op.param1])

		if op.type == 13:
			print ("[ 13 ] NOTIFIED INVITE INTO GROUP")
			if clientMid in op.param3:	        
				if settings["AutoJoinCancel"] == True:
					G = client.getGroup(op.param1)
					if len(G.members) <= settings["memberscancel"]:
						client.acceptGroupInvitation(op.param1)
						client.sendMessage(op.param1,"Maaf " + client.getContact(op.param2).displayName + "\nMember Kurang Dari 15 Orang")        
						client.leaveGroup(op.param1)
						
			if clientMid in op.param3:
				if settings["autoJoin"] == True:
					G = client.getGroup(op.param1)
					if len(G.members) <= settings["Members"]:
						client.rejectGroupInvitation(op.param1)
					else:
						client.acceptGroupInvitation(op.param1)
					dan = client.getContact(op.param2)
					tgb = client.getGroup(op.param1)
					client.sendMessage(op.param1, "Halo, Thx For Invite Me")
					client.sendContact(op.param1, op.param2)
					client.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net{}".format(dan.picturePath))
					
		if op.type == 15:
			if wait["leaveMessage"] == True:
				client.sendMention(op.param1, wait["messageLv"], [op.param2])
		
		if op.type == 17:
			dan = client.getContact(op.param2)
			tgb = client.getGroup(op.param1)
			#client.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net{}".format(dan.picturePath))
			#client.sendContact(op.param1, op.param2)
			client.sendMention(op.param1, "Halo @!,\nSelamat Datang Di {} \nJangan Lupa Check Note Ya \nSemoga Betah Kak 😘 ".format(str(tgb.name)),[op.param2])
			
		if op.type == 26:
			msg = op.message
			if msg.to in simi2["simi-simi"]:
				if simi2["simi-simi"][msg.to] == True:
					try:
						if msg.text is not None:
							simi = msg.text
							r = requests.get("https://api.moe.team/chatbot?text={}".format(simi))
							data = r.text
							data = json.loads(data)
							if data["code"] == 200:
								client.sendReplyMessage(msg.id, to, str(data["response"]))
					except Exception as error:
						pass

		if op.type == 26 or op.type == 25:
			try:
				print("[ 26 ] SEND MESSAGE")
				msg = op.message
				text = str(msg.text)
				msg_id = msg.id
				receiver = msg.to
				sender = msg._from
				cmd = command(text)
				setKey = settings["keyCommand"].title()
				if settings["setKey"] == False:
					setKey = ''
				if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
					if msg.toType == 0:
						if sender != client.profile.mid:
							to = sender
						else:
							to = receiver
					elif msg.toType == 1:
						to = receiver
					elif msg.toType == 2:
						to = receiver
					if msg.contentType == 0:
						if cmd == "logout":
							if msg._from in admin:
							    client.sendMessage(to, "Berhasil mematikan selfbot")
							    sys.exit("[ INFO ] BOT SHUTDOWN")
							    return
						elif cmd == "restart":
							if msg._from in admin:
							    client.sendMessage(to, "Berhasil mereset bot")
							    restartBot()
						elif cmd == "speed":
							if msg._from in admin:
							    start = time.time()
							    client.sendMessage(to, "Menghitung kecepatan...")
							    elapsed_time = time.time() - start
							    client.sendMessage(to, "Kecepatan mengirim pesan {} detik".format(str(elapsed_time)))
						elif cmd == "runtime":
							if msg._from in admin:
							    timeNow = time.time()
							    runtime = timeNow - clientStart
							    runtime = timeChange(runtime)
							    client.sendMessage(to, "Selfbot telah aktif selama {}".format(str(runtime)))
						elif cmd.startswith("setkey: "):
							sep = text.split(" ")
							key = text.replace(sep[0] + " ","")
							if " " in key:
								client.sendMessage(to, "Key tidak bisa menggunakan spasi")
							else:
								settings["keyCommand"] = str(key).lower()
								client.sendMessage(to, "Berhasil mengubah set key command menjadi : 「{}」".format(str(key).lower()))
						elif cmd == "help":
							helpMessage = menuHelp()
							#contact = (admin)
							#iconlink = "http://dl.profile.line-cdn.net/"+client.getProfile().picturePath
							#title = "Pikachu"
							#link = "line://ti/p/~yogafauzzz"
							client.sendMessage(to, helpMessage)
						elif cmd == "self":
							helpMessage1 = menuHelp1()
							#contact = (admin)
							#icon = "http://dl.profile.line-cdn.net/"+client.getProfile().picturePath
							#name = "Pikachu"
							#link = "line://ti/p/~yogafauzzz"
							client.sendMessage(to, helpMessage1)
						elif cmd == "group":
							helpMessage2 = menuHelp2()
							#contact = (admin)
							icon = "http://dl.profile.line-cdn.net/"+client.getProfile().picturePath
							name = "Pikachu"
							link = "line://ti/p/~yogafauzzz"
							client.sendMessage(to, helpMessage2)
						elif cmd == "special":
							helpMessage3 = helpmessage3()
							#contact = (admin)
							icon = "http://dl.profile.line-cdn.net/"+client.getProfile().picturePath
							name = "Pikachu"
							link = "line://ti/p/~yogafauzzz"
							client,sendMessage(to, helpMessage3)
						elif cmd == "media":
							helpMessage4 = helpmessage4()
							#contact = (admin)
							icon = "http://dl.profile.line-cdn.net/"+client.getProfile().picturePath
							name = "Pikachu"
							link = "line://ti/p/~yogafauzzz"
							client.sendMessage(to, helpMessage4)
						elif cmd == "settings":
							if msg._from in admin:
							    helpMessage5 = helpmessage5()
							    #contact = (admin)
							    icon = "http://dl.profile.line-cdn.net/"+client.getProfile().picturePath
							    name = "Pikachu"
							    link = "line://ti/p/~yogafauzzz"
							    client.sendMessage(to, helpMessage5)
						elif cmd == "errorlog":
							if msg._from in admin:
								with open('errorLog.txt', 'r') as fp:
									isi = fp.read()
								client.sendMessage(to, str(isi))
						elif cmd == "resetlogerror":
							if msg._from in admin:
								with open("errorLog.txt","w") as fp:
									fp.write("")
								client.sendMessage(to,"Berhasil reset log error")
						#elif cmd == "texttospeech":
							#helpTextToSpeech = menuTextToSpeech()
							#contact = (admin)
							#icon = "http://dl.profile.line-cdn.net/"+client.getProfile().picturePath
							#name = "Pikachu"
							#link = "line://ti/p/~yogafauzzz"
							#client.sendFooter(to, helpTextToSpeech, icon, name, link)
						#elif cmd == "translate":
							#helpTranslate = menuTranslate()
							#contact = (admin)
							#icon = "http://dl.profile.line-cdn.net/"+client.getProfile().picturePath
							#name = "Pikachu"
							#link = "line://ti/p/~yogafauzzz"
							#client.sendFooter(to, helpTranslate, icon, name, link)


						elif cmd == "status":
							if msg._from in admin:
							    try:
								    ret_ = "╔══[ Status ]"
								    if settings["autoAdd"] == True: ret_ += "\n╠ Auto Add : ON"
								    else: ret_ += "\n╠ Auto Add : OFF"
								    if settings["autoJoin"] == True: ret_ += "\n╠ Auto Join : ON"
								    else: ret_ += "\n╠ Auto Join : OFF"
								    if settings["autoJoin"] == True: ret_ += "\n╠ Auto Join Ticket : ON"
								    else: ret_ += "\n╠ Auto Join Ticket : OFF"
								    if settings["autoRead"] == True: ret_ += "\n╠ Auto Read : ON"
								    else: ret_ += "\n╠ Auto Read : OFF"
								    if settings["autoRespon"] == True: ret_ += "\n╠ Auto Respon : ON"
								    else: ret_ += "\n╠ Auto Respon : OFF"
								    if settings["checkContact"] == True: ret_ += "\n╠ Check Contact : ON"
								    else: ret_ += "\n╠ Check Contact : OFF"
								    if settings["checkPost"] == True: ret_ += "\n╠ Check Post : ON"
								    else: ret_ += "\n╠ Check Post : OFF"
								    if settings["checkSticker"] == True: ret_ += "\n╠ Check Sticker : ON"
								    else: ret_ += "\n╠ Check Sticker : OFF"
								    if settings["detectUnsend"] == True: ret_ += "\n╠ Detect Unsend : ON"
								    else: ret_ += "\n╠ Detect Unsend : OFF"
								    if settings["setKey"] == True: ret_ += "\n╠ Set Key : ON"
								    else: ret_ += "\n╠ Set Key : OFF"
								    ret_ +="\n╠ Auto Add Message : {}".format(settings["autoAddMessage"])
								    ret_ +="\n╠ Auto Join Message : {}".format(settings["autoJoinMessage"])
								    ret_ +="\n╠ Auto Respon Message : {}".format(settings["autoResponMessage"])
								    ret_ += "\n╚══[ Status ]"
								    client.sendMessage(to, str(ret_))
							    except Exception as error:
								    logError(error)
						elif cmd == "autoadd on":
							if settings["autoAdd"] == True:
								client.sendMessage(to, "Auto add telah aktif")
							else:
								settings["autoAdd"] = True
								client.sendMessage(to, "Berhasil mengaktifkan auto add")
						elif cmd == "autoadd off":
							if settings["autoAdd"] == False:
								client.sendMessage(to, "Auto add telah nonaktif")
							else:
								settings["autoAdd"] = False
								client.sendMessage(to, "Berhasil menonaktifkan auto add")
						elif cmd == "autojoin on":
							if msg._from in admin:
							    if settings["autoJoin"] == True:
								    client.sendMessage(to, "Auto join telah aktif")
							    else:
								    settings["autoJoin"] = True
								    client.sendMessage(to, "Berhasil mengaktifkan auto join")
						elif cmd == "autojoin off":
							if msg._from in admin:
							    if settings["autoJoin"] == False:
								    client.sendMessage(to, "Auto join telah nonaktif")
							    else:
								    settings["autoJoin"] = False
								    client.sendMessage(to, "Berhasil menonaktifkan auto join")
						elif cmd == "autojointicket on":
							if msg._from in admin:
							    if settings["autoJoinTicket"] == True:
								    client.sendMessage(to, "Auto join ticket telah aktif")
							    else:
								    settings["autoJoinTicket"] = True
								    client.sendMessage(to, "Berhasil mengaktifkan auto join ticket")
						elif cmd == "autojointicket off":
							if msg._from in admin:
							    if settings["autoJoinTicket"] == False:
								    client.sendMessage(to, "Auto join ticket telah nonaktif")
							    else:
								    settings["autoJoinTicket"] = False
								    client.sendMessage(to, "Berhasil menonaktifkan auto join ticket")
						elif cmd == "autoread on":
							if msg._from in admin:
							    if settings["autoRead"] == True:
								    client.sendMessage(to, "Auto read telah aktif")
							    else:
								    settings["autoRead"] = True
								    client.sendMessage(to, "Berhasil mengaktifkan auto read")
						elif cmd == "autoread off":
							if msg._from in admin:
							    if settings["autoRead"] == False:
								    client.sendMessage(to, "Auto read telah nonaktif")
							    else:
								    settings["autoRead"] = False
								    client.sendMessage(to, "Berhasil menonaktifkan auto read")
						elif cmd == "autorespon on":
							if msg._from in admin:
							    if settings["autoRespon"] == True:
								    client.sendMessage(to, "Auto respon telah aktif")
							    else:
								    settings["autoRespon"] = True
								    client.sendMessage(to, "Berhasil mengaktifkan auto respon")
						elif cmd == "autorespon off":
							if msg._from in admin:
							    if settings["autoRespon"] == False:
							        client.sendMessage(to, "Auto respon telah nonaktif")
							    else:
								    settings["autoRespon"] = False
								    client.sendMessage(to, "Berhasil menonaktifkan auto respon")
						elif cmd == "leave on":
							if msg._from in admin:
							    if wait["leaveMessage"] == True:
								    client.sendMessage(to, "Leave telah aktif")
							    else:
								    wait["leaveMessage"] = True
								    client.sendMessage(to, "Berhasil mengaktifkan Leave")
						elif cmd == "leave off":
							if msg._from in admin:
							    if wait["leaveMessage"] == False:
							        client.sendMessage(to, "Leave telah nonaktif")
							    else:
								    wait["leaveMessage"] = False
								    client.sendMessage(to, "Berhasil menonaktifkan Leave")
						elif cmd == "simi on":
							simi2["simi-simi"][msg.to] = True
							client.sendReplyMessage(msg.id, to, "Simi-Simi Sudah Aktif")
						elif cmd == "simi off":
							simi2["simi-simi"][msg.to] = False
							client.sendReplyMessage(msg.id, to, "Simi-Simi Dinonaktifkan")
						elif cmd == "checkcontact on":
							if settings["checkContact"] == True:
								client.sendMessage(to, "Check details contact telah aktif")
							else:
								settings["checkContact"] = True
								client.sendMessage(to, "Berhasil mengaktifkan check details contact")
						elif cmd == "checkcontact off":
							if settings["checkContact"] == False:
								client.sendMessage(to, "Check details contact telah nonaktif")
							else:
								settings["checkContact"] = False
								client.sendMessage(to, "Berhasil menonaktifkan Check details contact")
						elif cmd == "checkpost on":
							if settings["checkPost"] == True:
								client.sendMessage(to, "Check details post telah aktif")
							else:
								settings["checkPost"] = True
								client.sendMessage(to, "Berhasil mengaktifkan check details post")
						elif cmd == "checkpost off":
							if settings["checkPost"] == False:
								client.sendMessage(to, "Check details post telah nonaktif")
							else:
								settings["checkPost"] = False
								client.sendMessage(to, "Berhasil menonaktifkan check details post")
						elif cmd == "checksticker on":
							if settings["checkSticker"] == True:
								client.sendMessage(to, "Check details sticker telah aktif")
							else:
								settings["checkSticker"] = True
								client.sendMessage(to, "Berhasil mengaktifkan check details sticker")
						elif cmd == "checksticker off":
							if settings["checkSticker"] == False:
								client.sendMessage(to, "Check details sticker telah nonaktif")
							else:
								settings["checkSticker"] = False
								client.sendMessage(to, "Berhasil menonaktifkan check details sticker")
						elif cmd == "detectunsend on":
							if msg._from in admin:
							    if settings["detectUnsend"] == True:
								    client.sendMessage(to, "Detect unsend telah aktif")
							    else:
								    settings["detectUnsend"] = True
								    client.sendMessage(to, "Berhasil mengaktifkan detect unsend")
						elif cmd == "detectunsend off":
							if msg._from in admin:
							    if settings["detectUnsend"] == False:
								    client.sendMessage(to, "Detect unsend telah nonaktif")
							    else:
								    settings["detectUnsend"] = False
								    client.sendMessage(to, "Berhasil menonaktifkan detect unsend")
						elif cmd == "autolike on":
							if msg._from in admin:
							    if wait["autoLike"] == True:
								    client.sendMessage(to, "Auto like telah aktif")
							    else:
								    wait["autoLike"] = True
								    client.sendMessage(to, "Berhasil mengaktifkan auto like")
						elif cmd == "autolike off":
							if msg._from in admin:
							    if wait["autoLike"] == False:
								    client.sendMessage(to, "Auto like telah nonaktif")
							    else:
								    wait["autoLike"] = False
								    client.sendMessage(to, "Berhasil menonaktifkan auto like")
						elif cmd.startswith("setautoaddmessage: "):
							sep = text.split(" ")
							txt = text.replace(sep[0] + " ","")
							try:
								settings["autoAddMessage"] = txt
								client.sendMessage(to, "Berhasil mengubah pesan auto add menjadi : 「{}」".format(txt))
							except:
								client.sendMessage(to, "Gagal mengubah pesan auto add")
						elif cmd.startswith("setautoresponmessage: "):
							if msg._from in admin:
							    sep = text.split(" ")
							    txt = text.replace(sep[0] + " ","")
							    try:
								    settings["autoResponMessage"] = txt
								    client.sendMessage(to, "Berhasil mengubah pesan auto respon menjadi : 「{}」".format(txt))
							    except:
								    client.sendMessage(to, "Gagal mengubah pesan auto respon")
						elif cmd.startswith("setautojoinmessage: "):
							sep = text.split(" ")
							txt = text.replace(sep[0] + " ","")
							try:
								settings["autoJoinMessage"] = txt
								client.sendMessage(to, "Berhasil mengubah pesan auto join menjadi : 「{}」".format(txt))
							except:
								client.sendMessage(to, "Gagal mengubah pesan auto join")
						elif cmd.startswith("setleave: "):
							sep = text.split(" ")
							txt = text.replace(sep[0] + " ","")
							try:
								wait["messageLv"] = txt
								client.sendMessage(to, "Berhasil mengubah pesan leave menjadi : 「{}」".format(txt))
							except:
								client.sendMessage(to, "Gagal mengubah pesan leave")


						elif cmd.startswith("updatenamebot: "):
							if msg._from in admin:
							    sep = text.split(" ")
							    name = text.replace(sep[0] + " ","")
							    if len(name) <= 20:
								    profile = client.getProfile()
								    profile.displayName = name
								    client.updateProfile(profile)
								    client.sendMessage(to, "Berhasil mengubah nama menjadi : {}".format(name))
						elif cmd.startswith("updatebiobot: "):
							if msg._from in admin:
							    sep = text.split(" ")
							    bio = text.replace(sep[0] + " ","")
							    if len(bio) <= 500:
								    profile = client.getProfile()
								    profile.displayName = bio
								    client.updateProfile(profile)
								    client.sendMessage(to, "Berhasil mengubah bio menjadi : {}".format(bio))
						elif cmd == "me":
							client.sendReplyMessage(msg_id,to, None, contentMetadata={'mid': sender}, contentType=13)
						elif cmd == "myprofile":
							contact = client.getContact(sender)
							cover = client.getProfileCoverURL(sender)
							result = "╔══[ Details Profile ]"
							result += "\n╠ Display Name : @!"
							result += "\n╠ Mid : {}".format(contact.mid)
							result += "\n╠ Status Message : {}".format(contact.statusMessage)
							result += "\n╠ Picture Profile : http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus)
							result += "\n╠ Cover : {}".format(str(cover))
							result += "\n╚══[ Finish ]"
							client.sendImageWithURL(to, "http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus))
							client.sendMention(to, result, [sender])
						elif cmd == "mymid":
							contact = client.getContact(sender)
							client.sendMention(to, "@!: {}".format(contact.mid), [sender])
						elif cmd == "myname":
							contact = client.getContact(sender)
							client.sendMention(to, "@!: {}".format(contact.displayName), [sender])
						elif cmd == "mybio":
							contact = client.getContact(sender)
							client.sendMention(to, "@!: {}".format(contact.statusMessage), [sender])
						elif cmd == "mypicture":
							contact = client.getContact(sender)
							client.sendMessage(to, "http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus))
						elif cmd == "myvideoprofile":
							contact = client.getContact(sender)
							if contact.videoProfile == None:
								return client.sendMessage(to, "Anda tidak memiliki video profile")
							client.sendVideoWithURL(to, "http://dl.profile.line-cdn.net/{}/vp".format(contact.pictureStatus))
						elif cmd == "mycover":
							cover = client.getProfileCoverURL(sender)
							client.sendImageWithURL(to, str(cover))
						elif cmd.startswith("getmid "):
							if 'MENTION' in msg.contentMetadata.keys()!= None:
								names = re.findall(r'@(\w+)', text)
								mention = ast.literal_eval(msg.contentMetadata['MENTION'])
								mentionees = mention['MENTIONEES']
								lists = []
								for mention in mentionees:
									if mention["M"] not in lists:
										lists.append(mention["M"])
								for ls in lists:
									client.sendMention(to, "@!: {}".format(ls), [ls])
						elif cmd.startswith("getname "):
							if 'MENTION' in msg.contentMetadata.keys()!= None:
								names = re.findall(r'@(\w+)', text)
								mention = ast.literal_eval(msg.contentMetadata['MENTION'])
								mentionees = mention['MENTIONEES']
								lists = []
								for mention in mentionees:
									if mention["M"] not in lists:
										lists.append(mention["M"])
								for ls in lists:
									contact = client.getContact(ls)
									client.sendMention(to, "@!: {}".format(contact.displayName), [ls])
						elif cmd.startswith("getbio "):
							if 'MENTION' in msg.contentMetadata.keys()!= None:
								names = re.findall(r'@(\w+)', text)
								mention = ast.literal_eval(msg.contentMetadata['MENTION'])
								mentionees = mention['MENTIONEES']
								lists = []
								for mention in mentionees:
									if mention["M"] not in lists:
										lists.append(mention["M"])
								for ls in lists:
									contact = client.getContact(ls)
									client.sendMention(to, "@!: {}".format(contact.statusMessage), [ls])
						elif cmd.startswith("getpicture "):
							if 'MENTION' in msg.contentMetadata.keys()!= None:
								names = re.findall(r'@(\w+)', text)
								mention = ast.literal_eval(msg.contentMetadata['MENTION'])
								mentionees = mention['MENTIONEES']
								lists = []
								for mention in mentionees:
									if mention["M"] not in lists:
										lists.append(mention["M"])
								for ls in lists:
									contact = client.getContact(ls)
									client.sendImageWithURL(to, "http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus))
						elif cmd.startswith("getvideoprofile "):
							if 'MENTION' in msg.contentMetadata.keys()!= None:
								names = re.findall(r'@(\w+)', text)
								mention = ast.literal_eval(msg.contentMetadata['MENTION'])
								mentionees = mention['MENTIONEES']
								lists = []
								for mention in mentionees:
									if mention["M"] not in lists:
										lists.append(mention["M"])
								for ls in lists:
									contact = client.getContact(ls)
									if contact.videoProfile == None:
										return client.sendMention(to, "@!tidak memiliki video profile", [ls])
									client.sendVideoWithURL(to, "http://dl.profile.line-cdn.net/{}/vp".format(contact.pictureStatus))
						elif cmd.startswith("getcover "):
							if 'MENTION' in msg.contentMetadata.keys()!= None:
								names = re.findall(r'@(\w+)', text)
								mention = ast.literal_eval(msg.contentMetadata['MENTION'])
								mentionees = mention['MENTIONEES']
								lists = []
								for mention in mentionees:
									if mention["M"] not in lists:
										lists.append(mention["M"])
								for ls in lists:
									cover = client.getProfileCoverURL(ls)
									client.sendImageWithURL(to, str(cover))
						elif cmd == "friendlist":
							contacts = client.getAllContactIds()
							num = 0
							result = "╔══[ Friend List ]"
							for listContact in contacts:
								contact = client.getContact(listContact)
								num += 1
								result += "\n╠ {}. {}".format(num, contact.displayName)
							result += "\n╚══[ Total {} Friend ]".format(len(contacts))
							client.sendMessage(to, result)
						elif cmd.startswith("friendinfo "):
							sep = text.split(" ")
							query = text.replace(sep[0] + " ","")
							contacts = client.getAllContactIds()
							try:
								listContact = contacts[int(query)-1]
								contact = client.getContact(listContact)
								cover = client.getProfileCoverURL(listContact)
								result = "╔══[ Details Profile ]"
								result += "\n╠ Display Name : @!"
								result += "\n╠ Mid : {}".format(contact.mid)
								result += "\n╠ Status Message : {}".format(contact.statusMessage)
								result += "\n╠ Picture Profile : http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus)
								result += "\n╠ Cover : {}".format(str(cover))
								result += "\n╚══[ Finish ]"
								client.sendImageWithURL(to, "http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus))
								client.sendMention(to, result, [contact.mid])
							except Exception as error:
								logError(error)
						elif cmd == "blocklist":
							blockeds = client.getBlockedContactIds()
							num = 0
							result = "╔══[ List Blocked ]"
							for listBlocked in blockeds:
								contact = client.getContact(listBlocked)
								num += 1
								result += "\n╠ {}. {}".format(num, contact.displayName)
							result += "\n╚══[ Total {} Blocked ]".format(len(blockeds))
							client.sendMessage(to, result)
						elif cmd.startswith("friendbroadcast: "):
							sep = text.split(" ")
							txt = text.replace(sep[0] + " ","")
							contacts = client.getAllContactIds()
							for contact in contacts:
								client.sendMessage(contact, "[ Broadcast ]\n{}".format(str(txt)))
							client.sendMessage(to, "Berhasil broadcast ke {} teman".format(str(len(contacts))))
						elif cmd.startswith("cari "):
							if 'MENTION' in msg.contentMetadata.keys() != None:
								names = re.findall(r'@(\w+)', text)
								mention = ast.literal_eval(msg.contentMetadata['MENTION'])
								mentionees = mention['MENTIONEES']
								G = client.getGroupIdsJoined()
								cgroup = client.getGroups(G)
								groups = client.groups
								ngroup = ""
								ngroup += "╭──「 Found In Group 」"
								no = 0 + 1
								num = 0
								for mention in mentionees:
									for x in range(len(cgroup)):
										gMembMids = [contact.mid for contact in cgroup[x].members]
										if mention['M'] in gMembMids:
											ngroup += "\n│ {}. {} | {}".format(str(no), str(cgroup[x].name), str(len(cgroup[x].members)))
											no += 1
											num += 1
									ngroup += "\n╰── 「 Total {} Groups 」".format(str(num))
									client.sendMessage(to, str(ngroup))
								if ngroup == "":
									client.sendMessage(to, "NOT FOUND")
						
						elif cmd == 'groupcreator':
							group = client.getGroup(to)
							GS = group.creator.mid
							client.sendContact(to, GS)
						elif cmd == "changedual":
							if msg._from in admin:
								wait["ChangeVideoProfilevid"][msg._from] = True
								client.sendMessage(to,"Send Videonya...")
						elif cmd.startswith("changedualurl: "):
							if msg._from in admin:
								sep = msg.text.split(" ")
								url = msg.text.replace(sep[0] + " ","")
								client.downloadFileURL(url,'path','video.mp4')
								wait["ChangeVideoProfilePicture"][msg._from] = True
								client.sendMessage(to, "Send Gambarnya.....")
						elif cmd.startswith("changegroupname: "):
							if msg.toType == 2:
								sep = text.split(" ")
								groupname = text.replace(sep[0] + " ","")
								if len(groupname) <= 20:
									group = client.getGroup(to)
									group.name = groupname
									client.updateGroup(group)
									client.sendMessage(to, "Berhasil mengubah nama group menjadi : {}".format(groupname))
						elif cmd == "openqr":
							if msg.toType == 2:
								group = client.getGroup(to)
								group.preventedJoinByTicket = False
								client.updateGroup(group)
								groupUrl = client.reissueGroupTicket(to)
								client.sendMessage(to, "Berhasil membuka QR Group\n\nGroupURL : line://ti/g/{}".format(groupUrl))
						elif cmd == "closeqr":
							if msg.toType == 2:
								group = client.getGroup(to)
								group.preventedJoinByTicket = True
								client.updateGroup(group)
								client.sendMessage(to, "Berhasil menutup QR Group")
						elif cmd == "grouppicture":
							if msg.toType == 2:
								group = client.getGroup(to)
								groupPicture = "http://dl.profile.line-cdn.net/{}".format(group.pictureStatus)
								client.sendImageWithURL(to, groupPicture)
						elif cmd == "groupname":
							if msg.toType == 2:
								group = client.getGroup(to)
								client.sendMessage(to, "Nama Group : {}".format(group.name))
						elif cmd == "groupid":
							if msg.toType == 2:
								group = client.getGroup(to)
								client.sendMessage(to, "Group ID : {}".format(group.id))
						elif cmd == "grouplist":
							if msg._from in admin:
							     groups = client.getGroupIdsJoined()
							     ret_ = "╔══[ Group List ]"
							     no = 0
							     for gid in groups:
								     group = client.getGroup(gid)
								     no += 1
								     ret_ += "\n╠ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
							     ret_ += "\n╚══[ Total {} Groups ]".format(str(len(groups)))
							     client.sendMessage(to, str(ret_))
						elif cmd == "memberlist":
							if msg.toType == 2:
								group = client.getGroup(to)
								num = 0
								ret_ = "╔══[ List Member ]"
								for contact in group.members:
									num += 1
									ret_ += "\n╠ {}. {}".format(num, contact.displayName)
								ret_ += "\n╚══[ Total {} Members]".format(len(group.members))
								client.sendMessage(to, ret_)
						elif cmd == "pendinglist":
							if msg.toType == 2:
								group = client.getGroup(to)
								ret_ = "╔══[ Pending List ]"
								no = 0
								if group.invitee is None or group.invitee == []:
									return client.sendMessage(to, "Tidak ada pendingan")
								else:
									for pending in group.invitee:
										no += 1
										ret_ += "\n╠ {}. {}".format(str(no), str(pending.displayName))
									ret_ += "\n╚══[ Total {} Pending]".format(str(len(group.invitee)))
									client.sendMessage(to, str(ret_))
						elif cmd == "groupinfo":
							group = client.getGroup(to)
							try:
								try:
									groupCreator = group.creator.mid
								except:
									groupCreator = "Tidak ditemukan"
								if group.invitee is None:
									groupPending = "0"
								else:
									groupPending = str(len(group.invitee))
								if group.preventedJoinByTicket == True:
									groupQr = "Tertutup"
									groupTicket = "Tidak ada"
								else:
									groupQr = "Terbuka"
									groupTicket = "https://line.me/R/ti/g/{}".format(str(client.reissueGroupTicket(group.id)))
								ret_ = "╔══[ Group Information ]"
								ret_ += "\n╠ Nama Group : {}".format(group.name)
								ret_ += "\n╠ ID Group : {}".format(group.id)
								ret_ += "\n╠ Pembuat : @!"
								ret_ += "\n╠ Jumlah Member : {}".format(str(len(group.members)))
								ret_ += "\n╠ Jumlah Pending : {}".format(groupPending)
								ret_ += "\n╠ Group Qr : {}".format(groupQr)
								ret_ += "\n╠ Group Ticket : {}".format(groupTicket)
								ret_ += "\n╚══[ Success ]"
								client.sendImageWithURL(to, "http://dl.profile.line-cdn.net/{}".format(group.pictureStatus))
								client.sendMention(to, str(ret_), [groupCreator])
							except:
								ret_ = "╔══[ Group Information ]"
								ret_ += "\n╠ Nama Group : {}".format(group.name)
								ret_ += "\n╠ ID Group : {}".format(group.id)
								ret_ += "\n╠ Pembuat : {}".format(groupCreator)
								ret_ += "\n╠ Jumlah Member : {}".format(str(len(group.members)))
								ret_ += "\n╠ Jumlah Pending : {}".format(groupPending)
								ret_ += "\n╠ Group Qr : {}".format(groupQr)
								ret_ += "\n╠ Group Ticket : {}".format(groupTicket)
								ret_ += "\n╚══[ Success ]"
								client.sendImageWithURL(to, "http://dl.profile.line-cdn.net/{}".format(group.pictureStatus))
								client.sendMessage(to, str(ret_))
						elif cmd.startswith("broadcast: "):
							if msg._from in admin:
								sep = text.split(" ")
								pesan = text.replace(sep[0] + " ","")
								saya = client.getGroupIdsJoined()
								for group in saya:
									client.sendMessage(group,"[ Broadcast ]\n{}".format(str(pesan)))
								client.sendMessage(to, "Berhasil broadcast ke {} group".format(str(len(group))))
							
						
						elif cmd == 'tagall':
							group = client.getGroup(to)
							midMembers = [contact.mid for contact in group.members]
							midSelect = len(midMembers)//20
							for mentionMembers in range(midSelect+1):
								no = 0
								ret_ = "╭──[ Mentionall ]"
								dataMid = []
								for dataMention in group.members[mentionMembers*20 : (mentionMembers+1)*20]:
									dataMid.append(dataMention.mid)
									no += 1
									ret_ += "\n│ {}. @!".format(str(no))
								ret_ += "\n╰─[ Total {} Members ]".format(str(len(dataMid)))
								client.sendMention(to, ret_, dataMid)
						elif cmd == "tagall" or text.lower() == '😆':
							group = client.getGroup(to)
							nama = [contact.mid for contact in group.members]
							nm1, nm2, nm3, nm4, jml = [], [], [], [], len(nama)
							if jml <= 100:
								mentionMembers(msg.to, nama)
							if jml > 100 and jml < 200:
								for i in range (0, 99):
									nm1 += [nama[i]]
								mentionMembers(msg.to, nm1)
								for j in range (100, len(nama)-1):
									nm2 += [nama[j]]
								mentionMembers(msg.to, nm2)
							if jml > 200 and jml < 300:
								for i in range (0, 99):
									nm1 += [nama[i]]
								mentionMembers(msg.to, nm1)
								for j in range (100, 199):
									nm2 += [nama[j]]
								mentionMembers(msg.to, nm2)
								for k in range (200, len(nama)-1):
									nm3 += [nama[k]]
								mentionMembers(msg.to, nm3)
							if jml > 300 and jml < 400:
								for i in range (0, 99):
								    nm1 += [nama[i]]
								mentionMembers(msg.to, nm1)
								for j in range (100, 199):
									nm2 += [nama[j]]
								mentionMembers(msg.to, nm2)
								for k in range (200, 299):
									nm3 += [nama[k]]
									mentionMembers(msg.to, nm3)
								for l in range (300, len(nama)-1):
									nm4 += [nama[l]]
								mentionMembers(msg.to, nm4)
							if jml > 400 and jml < 500:
								for i in range (0, 99):
									nm1 += [nama[i]]
								mentionMembers(msg.to, nm1)
								for j in range (100, 199):
									nm2 += [nama[j]]
								mentionMembers(msg.to, nm2)
								for k in range (200, 299):
									nm3 += [nama[k]]
								mentionMembers(msg.to, nm3)
								for l in range (300, 399):
									nm4 += [nama[l]]
								mentionMembers(msg.to, nm4)
								for m in range (400, len(nama)-1):
									nm5 += [nama[m]]
								mentionMembers(msg.to, nm5)		
								
						
						elif cmd == "lurking on":
							tz = pytz.timezone("Asia/Jakarta")
							timeNow = datetime.now(tz=tz)
							day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
							hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
							bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
							hr = timeNow.strftime("%A")
							bln = timeNow.strftime("%m")
							for i in range(len(day)):
								if hr == day[i]: hasil = hari[i]
							for k in range(0, len(bulan)):
								if bln == str(k): bln = bulan[k-1]
							readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
							if to in read['readPoint']:
								try:
									del read['readPoint'][to]
									del read['readMember'][to]
								except:
									pass
								read['readPoint'][to] = msg_id
								read['readMember'][to] = []
								client.sendMessage(to, "Lurking telah diaktifkan")
							else:
								try:
									del read['readPoint'][to]
									del read['readMember'][to]
								except:
									pass
								read['readPoint'][to] = msg_id
								read['readMember'][to] = []
								client.sendMessage(to, "Set reading point : \n{}".format(readTime))
						elif cmd == "lurking off":
							tz = pytz.timezone("Asia/Jakarta")
							timeNow = datetime.now(tz=tz)
							day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
							hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
							bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
							hr = timeNow.strftime("%A")
							bln = timeNow.strftime("%m")
							for i in range(len(day)):
								if hr == day[i]: hasil = hari[i]
							for k in range(0, len(bulan)):
								if bln == str(k): bln = bulan[k-1]
							readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
							if to not in read['readPoint']:
								client.sendMessage(to,"Lurking telah dinonaktifkan")
							else:
								try:
									del read['readPoint'][to]
									del read['readMember'][to]
								except:
									pass
								client.sendMessage(to, "Delete reading point : \n{}".format(readTime))
						elif cmd == "lurking":
							if to in read['readPoint']:
								if read["readMember"][to] == []:
									return client.sendMessage(to, "Tidak Ada Sider")
								else:
									no = 0
									result = "╭──[  Reader ]"
									for dataRead in read["readMember"][to]:
										no += 1
										result += "\n│ {}. @!".format(str(no))
									result += "\n╰─[ Total {} Sider ]".format(str(len(read["readMember"][to])))
									client.sendMention(to, result, read["readMember"][to])
									read['readMember'][to] = []
						elif cmd == "reader on":
							try:
								tz = pytz.timezone("Asia/Jakarta")
								timeNow = datetime.now(tz=tz)
								nyamar = contentMetadata={"MSG_SENDER_NAME":"{}".format(client.getContact(msg._from).displayName),"MSG_SENDER_ICON": "http://dl.profile.line-cdn.net/{}".format(client.getContact(msg._from).pictureStatus)}
								client.sendMessage(to, "「 Status Reader 」\nBerhasil diaktifkan\n\n• Jam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]"+"\n• Tanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d'),nyamar)
								del cctv2['point'][msg.to]
								del cctv2['sidermem'][msg.to]
								del cctv2['cyduk'][msg.to]
							except:
								pass
							cctv2['point'][msg.to] = msg.id
							cctv2['sidermem'][msg.to] = ""
							cctv2['cyduk'][msg.to]=True
							
						elif cmd == "reader off":
							if msg.to in cctv2['point']:
								tz = pytz.timezone("Asia/Jakarta")
								timeNow = datetime.now(tz=tz)
								cctv2['cyduk'][msg.to]=False
								nyamar = contentMetadata={"MSG_SENDER_NAME":"{}".format(client.getContact(msg._from).displayName),"MSG_SENDER_ICON": "http://dl.profile.line-cdn.net/{}".format(client.getContact(msg._from).pictureStatus)}
								client.sendMessage(to, "「 Status reader 」\nBerhasil dimatikan\n\n• Jam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]"+"\n• Tanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d'),nyamar)
							else:
								client.sendMessage(to, "Sudak tidak aktif")
						elif cmd == "sider on":
							try:
								tz = pytz.timezone("Asia/Jakarta")
								timeNow = datetime.now(tz=tz)
								nyamar = contentMetadata={"MSG_SENDER_NAME":"{}".format(client.getContact(msg._from).displayName),"MSG_SENDER_ICON": "http://dl.profile.line-cdn.net/{}".format(client.getContact(msg._from).pictureStatus)}
								client.sendMessage(to, "「 Status Sider 」\nBerhasil diaktifkan\n\n• Jam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]"+"\n• Tanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d'),nyamar)
								del cctv['point'][msg.to]
								del cctv['sidermem'][msg.to]
								del cctv['cyduk'][msg.to]
							except:
							    pass
							cctv['point'][msg.to] = msg.id
							cctv['sidermem'][msg.to] = ""
							cctv['cyduk'][msg.to]=True
							
						elif cmd == "sider off":
							if msg.to in cctv['point']:
								tz = pytz.timezone("Asia/Jakarta")
								timeNow = datetime.now(tz=tz)
								cctv['cyduk'][msg.to]=False
								nyamar = contentMetadata={"MSG_SENDER_NAME":"{}".format(client.getContact(msg._from).displayName),"MSG_SENDER_ICON": "http://dl.profile.line-cdn.net/{}".format(client.getContact(msg._from).pictureStatus)}
								client.sendMessage(to, "「 Status Sider 」\nBerhasil dimatikan\n\n• Jam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]"+"\n• Tanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d'),nyamar)
							else:
								client.sendMessage(to, "Sudak tidak aktif")
						elif cmd == "updatebot":
							if msg._from in admin:
							    settings["changePictureProfile"] = True
							    client.sendMessage(to, "Silahkan kirim gambarnya")
						elif cmd == "changegrouppicture":
							if msg.toType == 2:
								if to not in settings["changeGroupPicture"]:
									settings["changeGroupPicture"].append(to)
								client.sendMessage(to, "Silahkan kirim gambarnya")
						elif cmd == "mimic on":
							if settings["mimic"]["status"] == True:
								client.sendMessage(to, "Reply message telah aktif")
							else:
								settings["mimic"]["status"] = True
								client.sendMessage(to, "Berhasil mengaktifkan reply message")
						elif cmd == "mimic off":
							if settings["mimic"]["status"] == False:
								client.sendMessage(to, "Reply message telah nonaktif")
							else:
								settings["mimic"]["status"] = False
								client.sendMessage(to, "Berhasil menonaktifkan reply message")
						elif cmd == "mimiclist":
							if settings["mimic"]["target"] == {}:
								client.sendMessage(to, "Tidak Ada Target")
							else:
								no = 0
								result = "╔══[ Mimic List ]"
								target = []
								for mid in settings["mimic"]["target"]:
									target.append(mid)
									no += 1
									result += "\n╠ {}. @!".format(no)
								result += "\n╚══[ Total {} Mimic ]".format(str(len(target)))
								client.sendMention(to, result, target)
						elif 'likepost ' in text.lower():
							try:
								typel = [1001,1002,1003,1004,1005,1006]
								key = eval(msg.contentMetadata["MENTION"])
								u = key["MENTIONEES"][0]["M"]
								a = client.getContact(u).mid
								s = client.getContact(u).displayName
								hasil = client.getHomeProfile(mid=a)
								st = hasil['result']['feeds']
								for i in range(len(st)):
									test = st[i]
									result = test['post']['postInfo']['postId']
									client.like(str(msg.to), str(result), likeType=random.choice(typel))
									client.comment(str(msg.to), str(result), 'Auto like by Fauzi \n\nline.me/ti/p/~yogafauzzz')
								client.sendMessage(to, 'Done Like '+str(len(st))+' Post From ' + str(s))
							except Exception as e:
								client.sendMessage(to, str(e))
								
						elif cmd == "creator" or text.lower() == 'creator':
							ma = "" 
							for i in creator:
								ma = client.getContact(i)
								client.sendReplyMessage(msg_id,to, None, contentMetadata={'mid': i}, contentType=13)
						elif cmd.startswith("mimicadd "):
							if 'MENTION' in msg.contentMetadata.keys()!= None:
								names = re.findall(r'@(\w+)', text)
								mention = ast.literal_eval(msg.contentMetadata['MENTION'])
								mentionees = mention['MENTIONEES']
								lists = []
								for mention in mentionees:
									if mention["M"] not in lists:
										lists.append(mention["M"])
								for ls in lists:
									try:
										if ls in settings["mimic"]["target"]:
											client.sendMessage(to, "Target sudah ada dalam list")
										else:
											settings["mimic"]["target"][ls] = True
											client.sendMessage(to, "Berhasil menambahkan target")
									except:
										client.sendMessage(to, "Gagal menambahkan target")
						elif cmd.startswith("mimicdel "):
							if 'MENTION' in msg.contentMetadata.keys()!= None:
								names = re.findall(r'@(\w+)', text)
								mention = ast.literal_eval(msg.contentMetadata['MENTION'])
								mentionees = mention['MENTIONEES']
								lists = []
								for mention in mentionees:
									if mention["M"] not in lists:
										lists.append(mention["M"])
								for ls in lists:
									try:
										if ls not in settings["mimic"]["target"]:
											client.sendMessage(to, "Target sudah tida didalam list")
										else:
											del settings["mimic"]["target"][ls]
											client.sendMessage(to, "Berhasil menghapus target")
									except:
										client.sendMessage(to, "Gagal menghapus target")
						elif cmd.startswith("spamtag"):
							if msg._from in admin:
								dan = text.split(" ")
								num = int(dan[1])
								text = "Berhasil {} spam mention".format(str(dan[1]))
								if 'MENTION' in msg.contentMetadata.keys()!= None:
									names = re.findall(r'@(\w+)', text)
									mention = ast.literal_eval(msg.contentMetadata['MENTION'])
									mentionees = mention['MENTIONEES']
									lists = []
									for mention in mentionees:
										if mention["M"] not in lists:
											lists.append(mention["M"])
									for ls in lists:
										for var in range(0,num):
											client.sendMention(to, "@!", [ls])
									client.sendMessage(to, text)
						elif cmd.startswith("ytmp3: "):
							try:
								sep = msg.text.split(" ")
								textToSearch = msg.text.replace(sep[0] + " ","")
								query = urllib.parse.quote(textToSearch)
								search_url="https://www.youtube.com/results?search_query="
								mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
								sb_url = search_url + query
								sb_get = requests.get(sb_url, headers = mozhdr)
								soupeddata = BeautifulSoup(sb_get.content, "html.parser")
								yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
								x = (yt_links[1])
								yt_href =  x.get("href")
								yt_href = yt_href.replace("watch?v=", "")
								qx = "https://youtu.be" + str(yt_href)
								vid = pafy.new(qx)
								stream = vid.streams
								best = vid.getbest()
								best.resolution, best.extension
								for s in stream:
									shi = best.url
									me = best.url
									vin = s.url
									hasil = ""
									title = '\n• Title :  ' + str(vid.title)
									author = '\n• Author : ' + str(vid.author)
									durasi = '\n• Duration : ' + str(vid.duration)
									suka = '\n• Likes : ' + str(vid.likes)
									rating = '\n• Rating : ' + str(vid.rating)
								#client.sendImageWithURL(to, me)
								client.sendMessage(to,title+ author+ durasi+ suka+ rating)
								client.sendAudioWithURL(to, shi)
							except Exception as e:
								client.sendMessage(to,str(e))
							
						elif cmd.startswith("instainfo"):
							sep = text.split(" ")
							txt = text.replace(sep[0] + " ","")
							url = requests.get("https://rest.farzain.com/api/ig_profile.php?id={}&apikey=SgPT6l42ujrcb2hf06tnGHyNR".format(txt))
							data = url.json()
							link = "https://www.instagram.com/{}".format(data["info"]["username"])
							result = "╭──「 Instagram Info "
							result += "\n│ Name : {}".format(data["info"]["full_name"])
							result += "\n│ Username: {}".format(data["info"]["username"])
							result += "\n│ Bio : {}".format(data["info"]["bio"])
							result += "\n│ Follower : {}".format(data["count"]["followers"])
							result += "\n│ Following : {}".format(data["count"]["following"])
							result += "\n│ Post : {}".format(data["count"]["post"])
							result += "\n╰─────"
							client.sendImageWithURL(to, data["info"]["profile_pict"])
							client.sendReplyMessage(msg_id,to, result)
						elif cmd.startswith("instastory "):
							sep = text.split(" ")
							query = text.replace(sep[0] + " ","")
							cond = query.split("|")
							search = str(cond[0])
							if len(cond) == 2:
								url = requests.get("http://rahandiapi.herokuapp.com/instastory/{}?key=betakey".format(search))
								data = url.json()
								num = int(cond[1])
								if num <= len(data["url"]):
									search = data["url"][num - 1]
									if search["tipe"] == 1:
										client.sendImageWithURL(to, str(search["link"]))
									elif search["tipe"] == 2:
										client.sendVideoWithURL(to, str(search["link"]))
						elif cmd == "quote" or cmd == " quote":
							r=requests.get("https://awkm.herokuapp.com/api/quotes")
							data=r.text
							data=json.loads(data)
							hasil = "「 Random Quote 」\n"
							hasil += "Author : {} \n".format(data["author"])
							hasil += str(data["quotes"])
							client.sendMessage(msg.to, str(hasil))
						elif cmd.startswith("say-"):
							sep = text.split("-")
							sep = sep[1].split(" ")
							lang = sep[0]
							if settings["setKey"] == False:
								txt = text.lower().replace("say-" + lang + " ","")
							else:
								txt = text.lower().replace(settings["keyCommand"] + "say-" + lang + " ","")
							if lang not in language["gtts"]:
								return client.sendMessage(to, "Bahasa {} tidak ditemukan".format(lang))
							tts = gTTS(text=txt, lang=lang)
							tts.save("line/tmp/tts-{}.mp3".format(lang))
							client.sendAudio(to, "line/tmp/tts-{}.mp3".format(lang))
							client.deleteFile("line/tmp/tts-{}.mp3".format(lang))
						elif cmd.startswith("searchyoutube "):
							sep = text.split(" ")
							txt = msg.text.replace(sep[0] + " ","")
							cond = txt.split("|")
							search = cond[0]
							url = requests.get("http://api.w3hills.com/youtube/search?keyword={}&api_key=86A7FCF3-6CAF-DEB9-E214-B74BDB835B5B".format(search))
							data = url.json()
							if len(cond) == 1:
								no = 0
								result = "╔══[ Youtube Search ]"
								for anu in data["videos"]:
									no += 1
									result += "\n╠ {}. {}".format(str(no),str(anu["title"]))
								result += "\n╚══[ Total {} Result ]".format(str(len(data["videos"])))
								result += "\n\nUntuk mengirim hasil, silahkan gunakan command {}Searchyoutube {}|「number」".format(str(setKey), str(search))
								client.sendMessage(to, result)
							elif len(cond) == 2:
								num = int(str(cond[1]))
								if num <= len(data):
									search = data["videos"][num - 1]
									ret_ = "╔══[ Youtube Info ]"
									ret_ += "\n╠ Channel : {}".format(str(search["publish"]["owner"]))
									ret_ += "\n╠ Title : {}".format(str(search["title"]))
									ret_ += "\n╠ Release : {}".format(str(search["publish"]["date"]))
									ret_ += "\n╠ Viewers : {}".format(str(search["stats"]["views"]))
									ret_ += "\n╠ Likes : {}".format(str(search["stats"]["likes"]))
									ret_ += "\n╠ Dislikes : {}".format(str(search["stats"]["dislikes"]))
									ret_ += "\n╠ Rating : {}".format(str(search["stats"]["rating"]))
									ret_ += "\n╠ Description : {}".format(str(search["description"]))
									ret_ += "\n╚══[ {} ]".format(str(search["webpage"]))
									client.sendImageWithURL(to, str(search["thumbnail"]))
									client.sendMessage(to, str(ret_))
						elif cmd.startswith("img "):
							sep = text.split(" ")
							txt = text.replace(sep[0] + " ","")
							url = requests.get("https://xeonwz.herokuapp.com/images/google.api?q={}".format(txt))
							data = url.json()
							client.sendImageWithURL(to, random.choice(data["content"]))
						elif cmd.startswith("searchmusic "):
							sep = text.split(" ")
							query = text.replace(sep[0] + " ","")
							cond = query.split("|")
							search = str(cond[0])
							url = requests.get("http://api.ntcorp.us/joox/search?q={}".format(str(search)))
							data = url.json()
							if len(cond) == 1:
								num = 0
								ret_ = "╭──「 Result Music 」"
								for music in data["result"]:
									num += 1
									ret_ += "\n│ {}. {}".format(str(num), str(music["single"]))
								ret_ += "\n╰─────「 Total {} Music 」".format(str(len(data["result"])))
								ret_ += "\n\nUntuk mengirim music, silahkan gunakan command {}SearchMusic {}|「number」".format(str(setKey), str(search))
								client.sendMessage(to, str(ret_))
							elif len(cond) == 2:
								num = int(cond[1])
								if num <= len(data["result"]):
									music = data["result"][num - 1]
									url = requests.get("http://api.ntcorp.us/joox/song_info?sid={}".format(str(music["sid"])))
									data = url.json()
									ret_ = "╭─「 Music 」"
									ret_ += "\n│ Title : {}".format(str(data["result"]["song"]))
									ret_ += "\n│ Album : {}".format(str(data["result"]["album"]))
									ret_ += "\n│ Size : {}".format(str(data["result"]["size"]))
									ret_ += "\n│ Link : {}".format(str(data["result"]["mp3"][0]))
									ret_ += "\n╰─────"
									client.sendImageWithURL(to, str(data["result"]["img"]))
									client.sendMessage(to, str(ret_))
									client.sendAudioWithURL(to, str(data["result"]["mp3"][0]))
						elif cmd.startswith("searchlyric "):
							sep = text.split(" ")
							txt = text.replace(sep[0] + " ","")
							cond = txt.split("|")
							query = cond[0]
							with requests.session() as web:
								web.headers["user-agent"] = "Mozilla/5.0"
								url = web.get("https://www.musixmatch.com/search/{}".format(urllib.parse.quote(query)))
								data = BeautifulSoup(url.content, "html.parser")
								result = []
								for trackList in data.findAll("ul", {"class":"tracks list"}):
									for urlList in trackList.findAll("a"):
										title = urlList.text
										url = urlList["href"]
										result.append({"title": title, "url": url})
								if len(cond) == 1:
									ret_ = "╔══[ Musixmatch Result ]"
									num = 0
									for title in result:
										num += 1
										ret_ += "\n╠ {}. {}".format(str(num), str(title["title"]))
									ret_ += "\n╚══[ Total {} Lyric ]".format(str(len(result)))
									ret_ += "\n\nUntuk melihat lyric, silahkan gunakan command {}SearchLyric {}|「number」".format(str(setKey), str(query))
									client.sendMessage(to, ret_)
								elif len(cond) == 2:
									num = int(cond[1])
									if num <= len(result):
										data = result[num - 1]
										with requests.session() as web:
											web.headers["user-agent"] = "Mozilla/5.0"
											url = web.get("https://www.musixmatch.com{}".format(urllib.parse.quote(data["url"])))
											data = BeautifulSoup(url.content, "html5lib")
											for lyricContent in data.findAll("p", {"class":"mxm-lyrics__content "}):
												lyric = lyricContent.text
												client.sendMessage(to, lyric)
						elif cmd.startswith("scloud "):
							sep = msg.text.split(" ")
							query = msg.text.replace(sep[0] + " ","")
							cond = query.split("|")
							search = str(cond[0])
							result = requests.get("http://rest.farzain.com/api/soundcloud.php?id={}&apikey=SgPT6l42ujrcb2hf06tnGHyNR".format(str(search)))
							data = result.text
							data = json.loads(data)
							if len(cond) == 1:
								num = 0
								ret_ = "╭─「 Result 」"
								for music in data["result"]:
									num += 1
									ret_ += "\n│  {}. {}".format(str(num), str(music["title"]))
								ret_ += "\n╰─────「 Total {} Soundcloud 」".format(str(len(data["result"])))
								ret_ += "\n\nUntuk Melihat Details Soundcloud, silahkan gunakan command {}Scloud {} | 「 number 」".format(str(setKey), str(search))
								client.sendMessage(to, str(ret_))
							elif len(cond) == 2:
								num = int(cond[1])
								if num <= len(data["result"]):
									music = data["result"][num - 1]
									ret_ = "╭─「 Soundcloud 」"
									ret_ += "\n│  Title : {}".format(str(music["title"]))
									ret_ += "\n│  Link : {}".format(str(music["url"]))
									ret_ += "\n╰─────────────"
									client.sendImageWithURL(to, music["img"])
									client.sendMessage(to, str(ret_))
									client.sendAudioWithURL(to, music["url_download"])
						elif cmd.startswith("1247w7 "):
							sep = msg.text.split(" ")
							query = msg.text.replace(sep[0] + " ","")
							cond = query.split("|")
							search = str(cond[0])
							result = requests.get("https://api.boteater.co/joox?search={}".format(str(search)))
							data = result.text
							data = json.loads(data)
							if len(cond) == 1:
								num = 0
								ret_ = "╭─「 Result 」"
								for music in data["result"]:
									num += 1
									ret_ += "\n│  {}. {}. - {}".format(str(num), str(music["artis"]), str(music["judul"]))
								ret_ += "\n╰─────「 Total {} Musik 」".format(str(len(data["result"])))
								ret_ += "\n\nUntuk Melihat Details Musik, silahkan gunakan command {}Musik {} | 「 number 」".format(str(setKey), str(search))
								client.sendMessage(to, str(ret_))
							elif len(cond) == 2:
								num = int(cond[1])
								if num <= len(data["result"]):
									spec = data["result"][num - 1]["link"]
									req= requests.get(spec)
									specs = req.text
									spek = json.loads(specs)
									client.sendMessage(to, spek["result"][0]["lyric"])
									client.sendAudioWithURL(to, spek["result"][0]["320url"])             
						
						elif cmd.startswith("musik "):
							sep = msg.text.split(" ")
							query = msg.text.replace(sep[0] + " ","")
							cond = query.split("|")
							search = str(cond[0])
							result = requests.get("http://api.fckveza.com/jooxmusic={}".format(str(search)))
							data = result.text
							data = json.loads(data)
							if len(cond) == 1:
								num = 0
								ret_ = "╭─「 Result 」"
								for music in data["result"]:
									num += 1
									ret_ += "\n│  {}. {}".format(str(num), str(music["judul"]))
								ret_ += "\n╰─────「 Total {} Music 」".format(str(len(data["result"])))
								ret_ += "\n\nUntuk Melihat Details Musik, silahkan gunakan command {}Musik {} | 「 number 」".format(str(setKey), str(search))
								client.sendMessage(to, str(ret_))
							elif len(cond) == 2:
								num = int(cond[1])
								if num <= len(data["result"]):
									music = data["result"][num - 1]
									url = requests.get("http://api.fckveza.com/musicid={}".format(str(music["songid"])))
									data = url.json()
									ret_ = "╭─「 Music 」"
									ret_ += "\n│ Singer : {}".format(str(data["result"][0]["artis"]))
									ret_ += "\n│ Title : {}".format(str(data["result"][0]["judul"]))
									ret_ += "\n│ Album : {}".format(str(data["result"][0]["single"]))
									ret_ += "\n╰─────"
									client.sendImageWithURL(to, data["result"][0]["imgUrl"])
									client.sendMessage(to, str(ret_))
									client.sendAudioWithURL(to, data["result"][0]["mp3Url"])
						
						elif cmd.startswith("vvh65 "):
							anunya = text.replace("musik ","")
							r = requests.get("https://arsybai.herokuapp.com/rest/joox?apikey=pikachu&query={}".format(str(anunya)))
							data = r.text
							data = json.loads(data)
							if data != []:
								fine = "╭─「 Music 」"
								fine += "\n│ Penyanyi : {}".format(str(data["result"][0]["singer"]))
								fine += "\n│ Judul : {}".format(str(data["result"][0]["title"]))
								fine += "\n│ Album : {}".format(str(data["result"][0]["album"]))
								fine += "\n╰─────"
								client.sendImageWithURL(to, data["result"][0]["img"])
								client.sendMessage(to, "Mohon bersabar. . .")
								client.sendAudioWithURL(to, data["result"][0]["mp3"])
						elif cmd.startswith("yffg: "):
							anunya = text.replace("musik: ","")
							r = requests.get("https://rest.farzain.com/api/joox/search.php?apikey=SgPT6l42ujrcb2hf06tnGHyNR&id={}".format(str(anunya)))
							data = r.text
							data = json.loads(data)
							fine = "[ Music ]\n\n"
							fine += "Penyanyi : {}".format(str(data["info"]["penyanyi"]))
							fine += "\nJudul : {}".format(str(data["info"]["judul"]))
							fine += "\nAlbum : {}".format(str(data["info"]["album"]))
							fine += "\nLink : {}".format(str(data["audio"]["mp3"]))
							client.sendImageWithURL(to, data["gambar"])
							client.sendMessage(to, str(fine))
							client.sendMessage(to, "Mohon bersabar. . .")
							client.sendAudioWithURL(to, data["audio"]["mp3"])
						elif cmd.startswith("fwindow: "):
							sep = text.split(" ")
							anu = text.replace(sep[0] + " ","")
							r = requests.get("http://api.zicor.ooo/fwindow.php?text={}&btype=3".format(urllib.parse.quote(anu)))
							data = r.text
							data = json.loads(data)
							ret_ = data["image"]
							client.sendImageWithURL(to, ret_)
						elif cmd.startswith("lgraffiti: "):
							sep = text.split(" ")
							anu = text.replace(sep[0] + " ","")
							r = requests.get("http://api.zicor.ooo/graffiti.php?text={}".format(urllib.parse.quote(anu)))
							data = r.text
							data = json.loads(data)
							ret_ = data["image"]
							client.sendImageWithURL(to, ret_)
						elif cmd.startswith("animeongoing"):
							r = requests.get("https://rest.farzain.com/api/animestream.php?apikey=SgPT6l42ujrcb2hf06tnGHyNR&type=new")
							data = r.text
							data = json.loads(data)
							ret_ = "╭─「 Result 」"
							num = 0
							for music in data["result"]:
								num += 1
								ret_ += "\n│  {}. {}".format(str(num), music["title"])
								ret_ += "\n│  {} {}".format(str(), music["eps_url"])
							ret_ += "\n╰──「 Total {} Anime Ongoing 」".format(str(len(data["result"])))
							client.sendMessage(to, str(ret_))
						elif cmd.startswith("animusik"):
							r = requests.get("http://api.moe.team/animusic")
							data = r.text
							data = json.loads(data)
							hasil = "「 Anime musik 」\n"
							hasil += "Title : {}".format(data["data"]["title"])
							#hasil += str(data["data"]["quots"])
							client.sendImageWithURL(to, data["data"]["image"])
							client.sendMessage(msg.to, str(hasil))
							client.sendAudioWithURL(to, data["data"]["audio"])
							#client.sendImageWithURL(to, music["image"])
							#client.sendMessage(to, ret_)
						elif cmd.startswith("cuaca "):
							sep = text.split(" ")
							anu = text.replace(sep[0] + " ","")
							r = requests.get("https://rest.farzain.com/api/cuaca.php?id={}&apikey=SgPT6l42ujrcb2hf06tnGHyNR".format(urllib.parse.quote(anu)))
							data = r.text
							data = json.loads(data)
							ret_ = "╭─「 Result 」"
							ret_ += "\n│  Tempat : {}".format(str(data["respon"]["tempat"]))
							ret_ += "\n│  Cuaca : {}".format(str(data["respon"]["cuaca"]))
							ret_ += "\n│  Deskripsi : {}".format(str(data["respon"]["deskripsi"]))
							ret_ += "\n│  Suhu : {}".format(str(data["respon"]["suhu"]))
							ret_ += "\n│  Kelembapan : {}".format(str(data["respon"]["kelembapan"]))
							ret_ += "\n│  Udara : {}".format(str(data["respon"]["udara"]))
							ret_ += "\n│  Angin : {}".format(str(data["respon"]["angin"]))
							ret_ += "╰──────────"
							client.sendMessage(to, ret_)
						elif cmd.startswith("instapict "):
							sep = text.split(" ")
							anu = text.replace(sep[0] + " ","")
							r = requests.get("https://rest.farzain.com/api/ig_post.php?id={}?_a=1&apikey=SgPT6l42ujrcb2hf06tnGHyNR".format(urllib.parse.quote(anu)))
							data = r.text
							data = json.loads(data)
							ret_ = data["first_pict"]
							client.sendImageWithURL(to, ret_)
						
							
						elif cmd.startswith("instavideo "):
							sep = text.split(" ")
							anu = text.replace(sep[0] + " ","")
							r = requests.get("https://rest.farzain.com/api/ig_post.php?id={}?_a=1&apikey=SgPT6l42ujrcb2hf06tnGHyNR".format(urllib.parse.quote(anu)))
							data = r.text
							data = json.loads(data)
							ret_ = data["first_video"]
							client.sendVideoWithURL(to, ret_)
						elif cmd.startswith("asking "):
							kata = removeCmd("asking", text)
							sch = kata.replace(" ","+")
							with _session as web:
								urlz = "http://lmgtfy.com/?q={}".format(str(sch))
								r = _session.get("http://tiny-url.info/api/v1/create?apikey=A942F93B8B88C698786A&provider=cut_by&format=json&url={}".format(str(urlz)))
								data = r.text
								data = json.loads(data)
								url = data["shorturl"]
								ret_ = "「Ask」"
								ret_ += "\n\nLink : {}".format(str(url))
								client.sendMessage(to, str(ret_))
						elif cmd.startswith("idline "):
							a = removeCmd("idline", text)
							b = client.findContactsByUserid(a)
							line = b.mid
							client.sendMessage(msg.to,"http://line.me/ti/p/~" + a)
							client.sendContact(to, line)
						elif cmd.startswith("dlscloud "):
							kata = removeCmd("dlscloud", text)
							sch = kata.replace(" ","+")
							result = requests.get("https://api.tanyz.xyz/download/soundCold/?link={}".format(str(sch)))
							data = result.text
							data = json.loads(data)
							url = data["Hasil"]
							ret_ = "╭─「 Result 」"
							ret_ += "\n│  Link : {}".format(str(url["download"]))
							ret_ += "╰──────────"
							client.sendMessage(to, ret_)
						elif cmd.startswith("tiktok"):
							r = requests.get("https://rest.farzain.com/api/tiktok.php?country=id, jp, kr&apikey=SgPT6l42ujrcb2hf06tnGHyNR&type=json")
							data = r.text
							data = json.loads(data)
							if data["status"] == 200:
								client.sendVideoWithURL(to, str(data["first_video"]))
						elif cmd.startswith("ytmp4 "):
							try:
								sep = msg.text.split(" ")
								text = msg.text.replace(sep[0] + " ","")
								qx = text
								vid = pafy.new(qx)
								stream = vid.streams
								best = vid.getbest()
								best.resolution, best.extension
								me = best.url
								client.sendReplyMessage(msg.id, to, "Mohon bersabar. ... ..")
								client.sendVideoWithURL(to, me)
							except Exception as e:
								client.sendMessage(to,str(e))
						elif cmd.startswith("ytmp4dl "):
							try:
								sep = msg.text.split(" ")
								text = msg.text.replace(sep[0] + " ","")
								qx = text
								vid = pafy.new(qx)
								best = vid.getbest()
								best.resolution, best.extension
								me = best.url
								#client.sendReplyMessage(msg.id, to, "Mohon bersabar. ... ..")
								client.sendFileMp4WithURL(to, me)
							except Exception as e:
								client.sendMessage(to,str(e))
						elif cmd.startswith("ytmp3 "):
							try:
								sep = msg.text.split(" ")
								text = msg.text.replace(sep[0] + " ","")
								qx = text
								vid = pafy.new(qx)
								best = vid.getbest()
								best.resolution, best.extension
								me = best.url
								client.sendReplyMessage(msg.id, to, "Mohon bersabar. ... ..")
								client.sendAudioWithURL(to, me)
							except Exception as e:
								client.sendMessage(to,str(e))
						elif cmd.startswith("ytmp3dl "):
							try:
								sep = msg.text.split(" ")
								text = msg.text.replace(sep[0] + " ","")
								qx = text
								vid = pafy.new(qx)
								best = vid.getbest()
								best.resolution, best.extension
								me = best.url
								#client.sendReplyMessage(msg.id, to, "Mohon bersabar. ... ..")
								client.sendFileMp3WithURL(to, me)
							except Exception as e:
								client.sendMessage(to,str(e))
						elif cmd.startswith("chatowner: "):
							contact = client.getContact(sender)
							text = cmd.replace("chatowner: ","")
							for own in owner:
								result = "@!"
								result += "\nSender : {}".format(contact.displayName)
								result += "\nPesan : {}".format(text)
								result += "\nMid : {}".format(contact.mid)
								client.sendReplyMessage(msg.id, to, "Pesan terkirim to Owner")
								client.sendMention(own, result, [sender])
						elif cmd.startswith("chat: "):
							if msg._from in admin:
								a = cmd.replace("chat: ","")[0]
								b = a.split()
								c = client.findContactsByUserid(a)[1]
								line = c.mid
								contact = client.getContact(sender)
								for cht in line:
									result = "@!"
									result += "\nSender : {}".format(contact.displayName)
									result += "\nPesan : {}".format(b)
									client.sendReplyMessage(msg.id, to, "Pesan terkirim ")
									client.sendMention(cht, result, [sender])
						elif cmd.startswith("ytdl "):
							search = cmd.replace("ytdl ","")
							r = requests.get("https://rest.farzain.com/api/yt_download.php?id={}&apikey=SgPT6l42ujrcb2hf06tnGHyNR".format(search))
							data = r.text
							data = json.loads(data)
							ret_ = "╭─「 Result 」"
							num = 0
							if data["urls"] != []:
								num += 1
								ret_ += "\n│  {}. {}".format(str(num), data["id"])
								ret_ += "\n│  {} {}".format(str(), data["label"])
								ret_ += "\n│  {} {}".format(str(), data["size"])
							ret_ += "\n╰──「 Total {}  」".format(str(len(data["urls"])))
							client.sendMessage(to, str(ret_))
							
						elif cmd.startswith("deviantart "):
							try:
								search = cmd.replace("devianart ","")
								r = requests.get("https://xeonwz.herokuapp.com/images/deviantart.api?q={}".format(search))
								data = r.text
								data = json.loads(data)
								if data["content"] != []:
									items = data["content"]
									path = random.choice(items)
									a = items.index(path)
									b = len(items)
									client.sendImageWithURL(to, str(path))
							except Exception as error:
								logError(error)
								var= traceback.print_tb(error.__traceback__)
								client.sendReplyMessage(msg.id, to,str(var))
							
						
						elif cmd.startswith("convert audio to file"):
							client.sendReplyMessage(msg.id, to,"Kirim audionya....")
							a = client.downloadObjectMsg(msg_id, "path","audio.mp3")
							client.sendFile(to, a)
						elif cmd.startswith("convert video to file"):
							client.sendReplyMessage(msg.id, to,"Kirim videonya....")
							a = client.downloadObjectMsg(msg_id, "path","video.mp4")
							client.sendFile(to, a)
						elif cmd.startswith("tr-"):
							sep = text.split("-")
							sep = sep[1].split(" ")
							lang = sep[0]
							if settings["setKey"] == False:
								txt = text.lower().replace("tr-" + lang + " ","")
							else:
								txt = text.lower().replace(settings["keyCommand"] + "tr-" + lang + " ","")
							if lang not in language["googletrans"]:
								return client.sendMessage(to, "Bahasa {} tidak ditemukan".format(lang))
							translator = Translator()
							result = translator.translate(txt, dest=lang)
							client.sendMessage(to, result.text)
						if text.lower() == "mykey":
							client.sendMessage(to, "Keycommand yang diset saat ini : 「{}」".format(str(settings["keyCommand"])))
						elif text.lower() == "setkey on":
							if settings["setKey"] == True:
								client.sendMessage(to, "Setkey telah aktif")
							else:
								settings["setKey"] = True
								client.sendMessage(to, "Berhasil mengaktifkan setkey")
						elif text.lower() == "setkey off":
							if settings["setKey"] == False:
								client.sendMessage(to, "Setkey telah nonaktif")
							else:
								settings["setKey"] = False
								client.sendMessage(to, "Berhasil menonaktifkan setkey")
						elif 'Set reader: ' in msg.text:
							if msg._from in admin:
								spl = msg.text.replace('Set reader: ','')
								if spl in [""," ","\n",None]:
									client.sendMessage(to, "Gagal mengganti Reader Msg")
								else:
									wait["sider"] = spl
									client.sendMessage(to, "「Reader Msg」\Reader Msg diganti jadi :\n\n「{}」".format(str(spl)))
						elif text.lower() == "cek reader":
							if msg._from in admin:
								client.sendMessage(to, "「Reader Msg」\Reader Msg mu :\n\n「 " + str(wait["sider"]) + " 」")
						elif 'Set sider: ' in msg.text:
							if msg._from in admin:
								spl = msg.text.replace('Set sider: ','')
								if spl in [""," ","\n",None]:
									client.sendMessage(to, "Gagal mengganti Sider Msg")
								else:
									settings["mention"] = spl
									client.sendMessage(to, "「Sider Msg」\nSider Msg diganti jadi :\n\n「{}」".format(str(spl)))
						elif text.lower() == "cek sider":
							if msg._from in admin:
								client.sendMessage(to, "「Sider Msg」\nSider Msg mu :\n\n「 " + str(settings["mention"]) + " 」")
								
						elif text.lower() == 'remove chat':
							if msg._from in admin:
							     client.removeAllMessages(op.param2)
							     client.sendMessage(to, "Chat dibersihkan....")
								
						elif text.lower() == 'pika2 bye':
							client.leaveGroup(msg.to)
							
						elif text.lower() in ["pika2 out"]:
							if msg._from in admin: 
								gid = client.getGroupIdsJoined()
								for i in gid:
									client.leaveGroup(i)
						elif text.lower() == 'login sb':
							if msg._from in premium["myService"]:
								user = premium["myService"][sender]
								try:
									linkqr = requests.get(url = 'https://api.eater.pw/token?header=CHROMEOS')
									qr = linkqr.text
									qrz = json.loads(qr)
									link = qrz['result'][0]['linktkn']
									qrp = qrz['result'][0]['linkqr']
									tokenz['{}'.format(sender)]= link
									#client.sendReplyMessage(msg_id,to, 'Check your PM')
									client.sendReplyMessage(msg_id,to, "Open this link on your LINE for\nsmartphone in 2 minutes \n{}".format(qrp))
									if sender not in premium['listLogin']:
										premium['listLogin'][sender] =  '%s' % user
										a = tokenz['{}'.format(msg._from)]
										req = requests.get(url = '{}'.format(a))
										b = req.text
										os.system('cp -r sbtes sb{}'.format(user))
										os.system('cd sb{} && echo -n "{}" > token.json'.format(user, b))
										os.system('screen -dmS sb{}'.format(user))
										os.system('screen -r sb{} -X stuff "cd sb{} && python3 sbtes.py \n"'.format(user, user))
										client.sendReplyMessage(msg_id,to, "「 Login Succes 」")
									else:
										client.sendMessage(to, "「 Request Login 」\n\nLink QR Expired -_-")
								except:
									client.sendMessage(to, "「  ERROR 」\n\nPlease Nonactive Filter Chat Or Letter Sealing -_-")
                        
						elif ("Adduser " in msg.text):
							if msg._from in admin:
								key = eval(msg.contentMetadata["MENTION"])
								key1 = key["MENTIONEES"][0]["M"]
								if key1 not in premium['myService']:
									nama = str(text.split(' ')[1])
									premium['myService'][key1] =  '%s' % nama
									client.sendMessage(to, 'Added to service')
								else:
									client.sendMessage(to, 'User already in service')
										
						elif ("Delluser " in msg.text):
							if msg._from in admin:
								if 'MENTION' in msg.contentMetadata.keys()!= None:
									key = eval(msg.contentMetadata["MENTION"])
									key1 = key["MENTIONEES"][0]["M"]
									if key1 in premium['myService']:
										del premium['myService'][key1]
										client.sendMessage(to, 'Deleted to service')
									else:
										client.sendMessage(to, 'User not in service')
										
						elif text.lower() == 'logout sb':
							if msg._from in premium["myService"]:
								del premium['listLogin'][msg._from]
								user = premium["myService"][msg._from]
								os.system('screen -S sb{} -X quit'.format(str(user)))
								os.system('rm -rf sb{}'.format(str(user)))
								time.sleep(2)
								client.sendMessage(to, "Sukses")
						elif text.lower() == 'remove':
							if msg._from in admin:
								sep = text.split(" ")
								anu = text.replace(sep[0] + " ","")
								os.system("screen -S sb{} -X quit".format(str(anu)))
								os.system('rm -rf sb{}'.format(str(anu)))
								time.sleep(2)
								client.sendMention(to, ' @!\nSucces remove file : {}'.format(str(anu)),' ', [msg._from])
						elif text.lower() == 'sb screen':
							if msg._from in admin:
								process = os.popen('screen -list')
								a = process.read()
								client.sendMessage(to, "{}".format(a))
								process.close()
						elif text.lower() == 'sb dirz':
							if msg._from in admin:
								process = os.popen('cd clone && ls')
								a = process.read()
								client.sendMessage(to, "{}".format(a))
								process.close()
						
						elif text.lower() == "help login" and to not in chatbot["botMute"]:
							if msg._from in premium["myService"]:
								client.sendMention(msg.to, 'Hai @!\n\n1. Type : Login Sb\n2. Check Personal Chat\n3. Press the Link Qr\n4. Type "Help" To see your command',' ', [msg._from])
						elif text.lower().startswith("adduser ") and msg._from not in myAdmin:
							client.sendMention(msg.to, 'Type : Add user\n\nHai @! Sorry you are not Owner',' ', [msg._from])
						elif text.lower().startswith("deluser ") and msg._from not in myAdmin:
							client.sendMention(msg.to, 'Type : Delete user\n\nHai @! Sorry you are not Owner',' ', [msg._from])
						elif text.lower().startswith("remove ") and msg._from not in myAdmin:
							client.sendMention(msg.to, 'Type : Remove\n\nHai @! Sorry you are not Owner',' ', [msg._from])
						elif text.lower() == "list user" and msg._from not in myAdmin:
							client.sendMention(msg.to, 'Type : List user selfbot\n\nHai @! Sorry you are not Owner',' ', [msg._from])
						elif text.lower() == "restart sb" and msg._from not in premium["myService"] and msg._from not in premium["myOwner"]:
							client.sendMention(msg.to, 'Type : Restart selfbot\n\nHai @! Sorry You are not listed In List User',' ', [msg._from])
						elif text.lower() == "login sb" and msg._from not in premium["myService"] and msg._from not in premium["myOwner"]:
							client.sendMention(msg.to, 'Type : Login selfbot\n\nHai @! Sorry You are not listed In List User',' ', [msg._from])
						elif text.lower() == "help login" and msg._from not in premium["myService"] and msg._from not in premium["myOwner"]:
							client.sendMention(msg.to, 'Type : Help login selfbot\n\nHai @! Sorry You are not listed In List User',' ', [msg._from])
						elif text.lower() == "logout sb" and msg._from not in premium["myService"] and msg._from not in premium["myOwner"]:
							client.sendMention(msg.to, 'Type : LogOut selfbot\n\nHai @! Sorry You are not listed In List User',' ', [msg._from])
						elif text.lower() == "logout sb" and msg._from in premium['listLogin'] and to not in chatbot["botMute"]:
							if msg._from in premium["myService"]:
								del premium['listLogin'][msg._from]
								user = premium["myService"][msg._from]
								os.system("screen -S {} -X quit".format(str(user)))
								os.system('rm -rf {}'.format(str(user)))
								time.sleep(2)
								client.sendMention(msg.to, '「  Logout Sb  」\n> @! LogOut From Selfbot',' ', [msg._from])
						elif text.lower() == "logout sb" and msg._from not in premium['listLogin']:
							if msg._from in premium["myService"]:
								client.sendMention(msg.to, '「  Logout Sb  」\nHai @!Sorry Please You Login First By Type < Login Sb > Or Type < Help Login >',' ', [msg._from])
						elif text.lower() == "restart sb" and to not in chatbot["botMute"]:
							if msg._from in premium["myService"]:
								user = premium["myService"][msg._from]
								os.system("screen -S {} -X quit".format(str(user)))
								os.system('screen -dmS {}'.format(user))
								os.system('screen -r {} -X stuff "cd {} && python3 sb.py \n"'.format(user, user))
								time.sleep(3)
								client.sendMention(msg.to, '「  Restart Sb  」\n> @! Succes Restart selfbot',' ', [msg._from])
						elif text.lower().startswith("remove") and msg._from in myAdmin:
							sep = text.split(" ")
							anu = text.replace(sep[0] + " ","")
							os.system("screen -S -X {} quit".format(str(anu)))
							os.system('rm -rf {}'.format(str(anu)))
							time.sleep(2)
							client.sendMention(msg.to, '「 Remove 」\n> @!\nSucces remove file : {}'.format(str(anu)),' ', [msg._from])
									
						elif ("Adminadd " in msg.text):
							if msg._from in creator:
								key = eval(msg.contentMetadata["MENTION"])
								key["MENTIONEES"][0]["M"]
								targets = []
								for x in key["MENTIONEES"]:
									targets.append(x["M"])
								for target in targets:
									try:
										admin.append(target)
										client.sendMessage(to,"Berhasil menambahkan admin")
									except:
										pass
						
						elif ("Admindell " in msg.text):
							if msg._from in creator:
								key = eval(msg.contentMetadata["MENTION"])
								key["MENTIONEES"][0]["M"]
								targets = []
								for x in key["MENTIONEES"]:
									targets.append(x["M"])
								for target in targets:
									try:
										admin.remove(target)
										client.sendMessage(to,"Berhasil menghapus admin")
									except:
										pass
						if text is None: return
						if "/ti/g/" in msg.text.lower():
							if settings["autoJoinTicket"] == True:
								link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
								links = link_re.findall(text)
								n_links = []
								for l in links:
									if l not in n_links:
										n_links.append(l)
								for ticket_id in n_links:
									group = client.findGroupByTicket(ticket_id)
									client.acceptGroupInvitationByTicket(group.id,ticket_id)
									client.sendMessage(to, "Berhasil masuk ke group %s" % str(group.name))
					elif msg.contentType == 1:
						if settings["changePictureProfile"] == True:
							path = client.downloadObjectMsg(msg_id, saveAs="LineAPI/tmp/{}-cpp.bin".format(time.time()))
							settings["changePictureProfile"] = False
							client.updateProfilePicture(path)
							client.sendMessage(to, "Berhasil mengubah foto profile")
							client.deleteFile(path)
						if msg.toType == 2:
							if to in settings["changeGroupPicture"]:
								path = client.downloadObjectMsg(msg_id, saveAs="LineAPI/tmp/{}-cgp.bin".format(time.time()))
								settings["changeGroupPicture"].remove(to)
								client.updateGroupPicture(to, path)
								client.sendMessage(to, "Berhasil mengubah foto group")
								client.deleteFile(path)
					elif msg.contentType == 7:
						if settings["checkSticker"] == True:
							stk_id = msg.contentMetadata['STKID']
							stk_ver = msg.contentMetadata['STKVER']
							pkg_id = msg.contentMetadata['STKPKGID']
							ret_ = "╔══[ Sticker Info p]"
							ret_ += "\n╠ STICKER ID : {}".format(stk_id)
							ret_ += "\n╠ STICKER PACKAGES ID : {}".format(pkg_id)
							ret_ += "\n╠ STICKER VERSION : {}".format(stk_ver)
							ret_ += "\n╠ STICKER URL : line://shop/detail/{}".format(pkg_id)
							ret_ += "\n╚══[ Finish ]"
							client.sendMessage(to, str(ret_))
					elif msg.contentType == 13:
						if settings["checkContact"] == True:
							try:
								contact = client.getContact(msg.contentMetadata["mid"])
								cover = client.getProfileCoverURL(msg.contentMetadata["mid"])
								ret_ = "╔══[ Details Contact ]"
								ret_ += "\n╠ Nama : {}".format(str(contact.displayName))
								ret_ += "\n╠ MID : {}".format(str(msg.contentMetadata["mid"]))
								ret_ += "\n╠ Bio : {}".format(str(contact.statusMessage))
								ret_ += "\n╠ Gambar Profile : http://dl.profile.line-cdn.net/{}".format(str(contact.pictureStatus))
								ret_ += "\n╠ Gambar Cover : {}".format(str(cover))
								ret_ += "\n╚══[ Finish ]"
								client.sendImageWithURL(to, "http://dl.profile.line-cdn.net/{}".format(str(contact.pictureStatus)))
								client.sendMessage(to, str(ret_))
							except:
								client.sendMessage(to, "Kontak tidak valid")
					elif msg.contentType == 16:
						if wait["autoLike"] == True:
							url = msg.contentMetadata["postEndUrl"]
							client.like(url[25:58], url[66:], likeType=1003)
							client.comment(url[25:58], url[66:], 'Auto like by Fauzi \n\nline.me/ti/p/~yogafauzzz')
						if settings["checkPost"] == True:
							try:
								ret_ = "╔══[ Details Post ]"
								if msg.contentMetadata["serviceType"] == "GB":
									contact = client.getContact(sender)
									auth = "\n╠ Penulis : {}".format(str(contact.displayName))
								else:
									auth = "\n╠ Penulis : {}".format(str(msg.contentMetadata["serviceName"]))
								purl = "\n╠ URL : {}".format(str(msg.contentMetadata["postEndUrl"]).replace("line://","https://line.me/R/"))
								ret_ += auth
								ret_ += purl
								if "mediaOid" in msg.contentMetadata:
									object_ = msg.contentMetadata["mediaOid"].replace("svc=myhome|sid=h|","")
									if msg.contentMetadata["mediaType"] == "V":
										if msg.contentMetadata["serviceType"] == "GB":
											ourl = "\n╠ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
											murl = "\n╠ Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(msg.contentMetadata["mediaOid"]))
										else:
											ourl = "\n╠ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
											murl = "\n╠ Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(object_))
										ret_ += murl
									else:
										if msg.contentMetadata["serviceType"] == "GB":
											ourl = "\n╠ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
										else:
											ourl = "\n╠ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
									ret_ += ourl
								if "stickerId" in msg.contentMetadata:
									stck = "\n╠ Stiker : https://line.me/R/shop/detail/{}".format(str(msg.contentMetadata["packageId"]))
									ret_ += stck
								if "text" in msg.contentMetadata:
									text = "\n╠ Tulisan : {}".format(str(msg.contentMetadata["text"]))
									ret_ += text
								ret_ += "\n╚══[ Finish ]"
								client.sendMessage(to, str(ret_))
							except:
								client.sendMessage(to, "Post tidak valid")
			except Exception as error:
				logError(error)


		if op.type == 26 or op.type == 25:
			try:
				print("[ 26 ] RECEIVE MESSAGE")
				msg = op.message
				text = str(msg.text)
				msg_id = msg.id
				receiver = msg.to
				sender = msg._from
				if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
					if msg.toType == 0:
						if sender != client.profile.mid:
							to = sender
						else:
							to = receiver
					elif msg.toType == 1:
						to = receiver
					elif msg.toType == 2:
						to = receiver
					#if sender in settings["mimic"]["target"] and settings["mimic"]["status"] == True and settings["mimic"]["target"][sender] == True:
						#if msg.contentType == 0:
							#client.sendMessage(to, text)
						#elif msg.contentType == 1:
							#path = client.downloadObjectMsg(msg_id, saveAs="LineAPI/tmp/{}-mimic.bin".format(time.time()))
							#client.sendImage(to, path)
							#client.deleteFile(path)
					if msg.contentType == 2:
						if msg._from in admin:
							if msg._from in wait["ChangeVideoProfilevid"]:
								wait["ChangeVideoProfilePicture"][msg._from] = True
								del wait["ChangeVideoProfilevid"][msg._from]
								client.downloadObjectMsg(msg_id,'path','video.mp4')
								client.sendMessage(to,"Send gambarnya...")
					if msg.contentType == 1:
						if msg._from in admin:
							if msg._from in wait["ChangeVideoProfilePicture"]:
								del wait["ChangeVideoProfilePicture"][msg._from]
								client.downloadObjectMsg(msg_id,'path','image.jpg')
								client.nadyacantikimut('video.mp4','image.jpg')
								client.sendMessage(to,"Change Video Profile Success!!!")
					if msg.contentType == 0:
						if settings["autoRead"] == True:
							client.sendChatChecked(to, msg_id)
						if sender not in clientMid:
							if msg.toType != 0 and msg.toType == 2:
								if 'MENTION' in msg.contentMetadata.keys()!= None:
									names = re.findall(r'@(\w+)', text)
									mention = ast.literal_eval(msg.contentMetadata['MENTION'])
									mentionees = mention['MENTIONEES']
									for mention in mentionees:
										if clientMid in mention["M"]:
											if settings["autoRespon"] == True:
												client.sendMention(sender, settings["autoResponMessage"], [sender])
											break
						if text is None: return
						if "/ti/g/" in msg.text.lower():
							if settings["autoJoinTicket"] == True:
								link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
								links = link_re.findall(text)
								n_links = []
								for l in links:
									if l not in n_links:
										n_links.append(l)
								for ticket_id in n_links:
									group = client.findGroupByTicket(ticket_id)
									client.acceptGroupInvitationByTicket(group.id,ticket_id)
									client.sendMessage(to, "Berhasil masuk ke group %s" % str(group.name))
						if settings["detectUnsend"] == True:
							try:
								unsendTime = time.time()
								unsend[msg_id] = {"text": text, "from": sender, "time": unsendTime}
							except Exception as error:
								logError(error)
					if msg.contentType == 6:
						if settings["responGc"] == True:
							contact = client.getContact(sender)
							if msg.toType == 0:
								if msg.contentMetadata["GC_EVT_TYPE"] == "I":
									client.sendMention(sender, settings["autoResponGC"], [sender])
									arg = "   Info : Invited Group Call"
									arg += "\n   Executor : {}".format(str(contact.displayName))
									print (arg)
							elif msg.toType == 2:
								group = client.getGroup(to)
								if msg.contentMetadata["GC_EVT_TYPE"] == "S":
									arg = "   Info : Started Group Call"
									arg += "\n   Group Name : {}".format(str(group.name))
									arg += "\n   Executor : {}".format(str(contact.displayName))
									print (arg)
									client.sendMention(sender, settings["autoResponGC2"], [sender])
								elif msg.contentMetadata["GC_EVT_TYPE"] == "E":
									client.sendMention(sender, settings["autoResponGC3"], [sender])
									arg = "   Info : Ended Group Call"
									arg += "\n   Group Name : {}".format(str(group.name))
									arg += "\n   Executor : {}".format(str(contact.displayName))
									print (arg) 
					elif msg.contentType == 13:
						try:
							client.getContact(msg.contentMetadata["mid"])
						except:
							client.removeMessage(msg_id)
							client.sendMessage(to, "Crash ra guno :v")
							print ("Crash contact detected...")
							return
					if msg.contentType == 1:
						if settings["detectUnsend"] == True:
							try:
								unsendTime = time.time()
								image = client.downloadObjectMsg(msg_id, saveAs="LineAPI/tmp/{}-image.bin".format(time.time()))
								unsend[msg_id] = {"from": sender, "image": image, "time": unsendTime}
							except Exception as error:
								logError(error)
			except Exception as error:
				logError(error)


		if op.type == 55:
			print ("[ 55 ] NOTIFIED READ MESSAGE")
			if op.param1 in read["readPoint"]:
				if op.param2 not in read["readMember"][op.param1]:
					read["readMember"][op.param1].append(op.param2)
						
		if op.type == 55:
			 try:
				 if cctv['cyduk'][op.param1]==True:
					 if op.param1 in cctv['point']:
						 Name = client.getContact(op.param2).displayName
						 if Name in cctv['sidermem'][op.param1]:
							 pass
						 else:
							 cctv['sidermem'][op.param1] += "\n~ " + Name
							 siderMembers(op.param1, [op.param2])
					 else:
						 pass
				 else:
					 pass
			 except:
				  pass
						
						
		if op.type == 55:
			if cctv2['cyduk'][op.param1]==True:
				if op.param1 in cctv2['point']:
					Name = client.getContact(op.param2).displayName
					if Name in cctv2['sidermem'][op.param1]:
					    pass
					else:
						cctv2['sidermem'][op.param1] += "\n~ " + Name
						#zxn=["Jangan sider terus ","Jangan sider ","Halo ayo kita ngobrol ","Turun kak ikut chat ","Sider mulu ","sider tak doakan jones ","Ciyyee yang lagi ngintip ","Hai Kang ngintip ","Jangan sider mulu dong kk "]
						nyamar = contentMetadata={"MSG_SENDER_NAME":"{}".format(client.getContact(op.param2).displayName),"MSG_SENDER_ICON": "http://dl.profile.line-cdn.net/{}".format(client.getContact(op.param2).pictureStatus)}
						pref=["Cie yang lagi ngintip ","Eh ada","Nah lagi scroll ya ","Halo ","Sini kak ","Turun kak ikut chat","Tercyduk kau ","Hey ","Diem diem bae ","Lagi ngapain "]
						client.sendMessage(op.param1, random.choice(pref)+' '+ Name)
						#siderMembers(op.param1, [op.param2])
					
		
		if op.type == 65:
			try:
				if settings["detectUnsend"] == True:
					to = op.param1
					sender = op.param2
					if sender in unsend:
						unsendTime = time.time()
						contact = client.getContact(unsend[sender]["from"])
						if "text" in unsend[sender]:
							try:
								sendTime = unsendTime - unsend[sender]["time"]
								sendTime = timeChange(sendTime)
								ret_ = "╭─「 Pesan dihapus 」"
								ret_ += "\n│ Pengirim : @!"
								ret_ += "\n│ Waktu : {} yang lalu".format(sendTime)
								ret_ += "\n│ Type : Text"
								ret_ += "\n│ Text : {}".format(unsend[sender]["text"])
								ret_ += "\n╰─────────────"
								client.sendMention(to, ret_, [contact.mid])
								del unsend[sender]
							except:
								del unsend[sender]
						elif "image" in unsend[sender]:
							try:
								sendTime = unsendTime - unsend[sender]["time"]
								sendTime = timeChange(sendTime)
								ret_ = "╭─「 Pesan dihapus 」"
								ret_ += "\n│ Pengirim : @!"
								ret_ += "\n│ Waktu : {} yang lalu".format(sendTime)
								ret_ += "\n│ Type : Image"
								ret_ += "\n│ Text : None"
								ret_ += "\n╰─────────────"
								client.sendMention(to, ret_, [contact.mid])
								client.sendImage(to, unsend[sender]["image"])
								client.deleteFile(unsend[sender]["image"])
								del unsend[sender]
							except:
								client.deleteFile(unsend[sender]["image"])
								del unsend[sender]
					else:
						client.sendMessage(to, "Data unsend tidak ditemukan")
			except Exception as error:
				logError(error)
		backupData()
	except Exception as error:
		logError(error)

def run():
	while True:
		ops = clientPoll.singleTrace(count=50)
		if ops != None:
			for op in ops:
				try:
					clientBot(op)
				except Exception as error:
					logError(error)
				clientPoll.setRevision(op.revision)

if __name__ == "__main__":
	run()
