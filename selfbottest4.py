# -*- coding: utf-8 -*-

from LineAPI.linepy import *
from LineAPI.akad.ttypes import Message
from LineAPI.akad.ttypes import ContentType as Type
from LineAPI.akad.ttypes import ChatRoomAnnouncementContents
from LineAPI.akad.ttypes import ChatRoomAnnouncement
from datetime import datetime, timedelta, date, timezone
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, multiprocessing, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib3, urllib.parse, html5lib, wikipedia, atexit, timeit, pafy, youtube_dl, traceback

dz = LINE("EMohmFMeyUB3a003kkC8.AlUwBuOESO9tzvoy4jATca.c0BAzNbPwxQwPwF0BEqhh5Viy+Waxgr9KinVrGsiIPY=")
dz.log("Auth Token : " + str(dz.authToken))
dz.log("Timeline Token : " + str(dz.tl.channelAccessToken))

#==============================================================================#
call = dz
oepoll = OEPoll(dz)
dzMID = dz.profile.mid
dzProfile = dz.getProfile()
lineSettings = dz.getSettings()
#==============================================================================#
botStart = time.time()
#==============================================================================#

myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}

helpMessage ="""╔═══════════ 
║ ✇✇  DLG BOT  ✇✇
╠═══════════
╠⍟➣  /Help
╠⍟➣  Tagall
╠⍟➣  /Member list
╠⍟➣  Spamtag @[User]
╠⍟➣  Info @[User]
╠⍟➣  /Ginfo 
╠⍟➣  /Calendar
╠⍟➣  /discord
╠⍟➣  /facebook
╠⍟➣  /website
╠⍟➣  /youtube
╠⍟➣  /twitter
╠⍟➣  /instagram
╠⍟➣  /teamspeak
╠⍟➣  /family
╠⍟➣  /tech
╠⍟➣  /games
╠⍟➣  /donate
╠⍟➣  /merch
╠═══════════
"""

family =""" ✇✇  DLG FAMILY  ✇✇
════════════
══  DL.    ═  K565 ══ 
══  D@L  ═  K480 ══
══  dl8    ═  K41 ══
══  dDL   ═  K458 ══
══  DL^    ═  K240 ══
══  DLD   ═  K565 ═
══  pdl     ═  K517 ══
══  wDL   ═  K517 ══
══  DlL     ═  K488 ══
════════════
"""

tech =""" DLG Tech Team
════════════
[DL#] Fekhole
➣ Teamspeak/Youtube
════════════
[dla] TJ/I Am Rocket
➣ Spreadsheets/Graphic Design/Youtube
════════════
[DL.] Dex
➣ Discord/Website/Graphic Design/Youtube
════════════
[DL.] xParzivalx
➣ Website/Bot/Youtube
════════════
[DL.] Lulou 
➣ Website/Youtube/Twitter/Instagram
════════════
[TUE] ShirleysTemple
➣ Graphic Design
════════════
"""

games =""" DLG Family Games
════════════
Lords Mobile
➣ [DL.] HBO
════════════
Clash of Clans
➣ [DL.] HBO
════════════
World of Warcraft
➣ Vyndroe
════════════
Rise of Civilizations
➣ [DLE] ToiletWater
════════════
Pirates of the Caribbean
➣ [DLE] JonSnow5025
════════════
Diablo
➣ [DxL/DML] Rahvin
════════════
"""

donate =""" paypal.me/darklegendsgaming
All donations go to DLG family, tech support, and Youtube staff.
Owned by HBO/Richard Owen
"""

sid = []
wait = {
    "spamr":True,
    "Invite":True,
    "ainvite":False,
    "atarget":False,
    "dtarget":False,
    "afriend":False,
    "dfriend":False,
    "asilent":False,
    "dsilent":False,
    "santet":True,
    "Autojoin":False,
    "Timeline":False,
    "LikeOn":True,
    "getmid":True,
    "mimic":True,
    }

org = {
    "tmimic":{},
    "Target":{},
    "Silent":{},
    "Friend":{},
    "invitan":{},
    "inviter":{}
    }

pro = {
    'prosider':{},
    'proPoint':{},
    'proTime':{},
    'Protectgr':{},
    'Protectcancl':{},
    'Protectjoin':{},
    'Protectinvite':{},
    'wellcome':False,
    'bymsg':False,
    'intaPoint':{},
    "Autokick":{}
    }

resp = {
    "csticker1":False,
    "csticker2":False,
    "csticker3":False,
    "detectsticker":False,
    "grupsticker":{},
    "Tag1":False,
    "Tag2":False,
    "Tag3":False,
	}

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

ciduk = {
    'ceadPoint':{},
    'ceadMember':{},
    'cetTime':{},
    'cOM':{}
    }

setTime = {}
setTime = wait2['setTime']
mulai = time.time() 

myProfile["displayName"] = dzProfile.displayName
myProfile["statusMessage"] = dzProfile.statusMessage
myProfile["pictureStatus"] = dzProfile.pictureStatus

contact = dz.getProfile()
backup = dz.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

#==============================================================================#
def restartBot():
    time.sleep(3)
    python = sys.executable
    os.execl(python, python, *sys.argv)
    
def restart_program(): 
    python = sys.executable
    os.execl(python, python, * sys.argv) 
    
def backupData():
    try:
        backup = settings
        f = codecs.open('temp.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False
    
def logError(text):
    dz.log("[ ERROR ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
        
def sendMessageWithMention(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@x '
        dz.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
        
def sendAudioWithURL(self, to_, url):
        path = self.downloadFileWithURL(url)
        try:
            self.sendAudio(to_, path)
        except Exception as e:
            raise Exception(e)

def sendAudioWithUrl(self, to_, url):
        path = '%s/pythonLine-%1.data' % (tempfile.gettempdir(), randint(0, 9))
        r = requests.get(url, stream=True, verify=False)
        if r.status_code == 200:
           with open(path, 'w') as f:
              shutil.copyfileobj(r.raw, f)
        else:
           raise Exception('Download audio failure.')
        try:
            self.sendAudio(to_, path)
        except Exception as e:
            raise e
            
def command(text):
    pesan = text.lower()
    if pesan.startswith(Setmain["keyCommand"]):
        cmd = pesan.replace(Setmain["keyCommand"],"")
    else:
        cmd = "command"
    return cmd
#==============================================================================#
def dhenzaBot(op):
    try:
        if op.type == 0:
            return
#=================[ NOTIFIED_INVITE_INTO_GROUP ]==============        
        if op.type == 13:
            if op.param2 == "u6fd63b2d8788d09692f671ef0bc3201d":
                dz.acceptGroupInvitation(op.param1)
#==============[ WELCOME] ===============
        if op.type == 17:
            ginfo = dz.getGroup(op.param1)
            if op.param1 == "c431a52f1131ba1d01ce91ada4bede4ba":
                dzx = dz.getContact(op.param2)
                dz.sendMessage(op.param1, "Hello " + str(dzx.displayName) + "!\n\nWelcome to " + str(ginfo.name) + ".")
                dz.sendImage(op.param1,"/home/pi/Downloads/welcome.png")

            if op.param1 == "c172a26b3b8f25ace97aa892c14832039":
                dzx = dz.getContact(op.param2)
                dz.sendMessage(op.param1, "Hello " + str(dzx.displayName) + "!\n\nWelcome to " + str(ginfo.name) + ".")
                dz.sendImage(op.param1,"/home/pi/Downloads/welcome.png")

#==================[ RECEIVE_MESSAGE ]===============
        if op.type == 25:
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                if msg.text in ["/Help"]:
                    dz.sendMessage(msg.to,helpMessage)          
					
        if op.type == 25:
            msg = op.message
            if msg.text is None:
                return
            if msg.text in ["My id"]:
                if msg.toType == 2:
                    dz.sendMessage(msg.to,dzMID)
                    
            elif msg.text in ["Me"]:
            	dz.sendMessage(receiver, None, contentMetadata={'mid': dzMID}, contentType=13)

            elif msg.text in ["Reject"]:
              if msg.toType == 2:
                gid = dz.getGroupIdsInvited()
                for i in gid:
                    dz.rejectGroupInvitation(i)
                dz.sendMessage(msg.to,"done reject")

            elif "bcgroup: " in msg.text:
                bc = msg.text.replace("bcgroup: ","")
                gid = dz.getGroupIdsJoined()
                for i in gid:
                    dz.sendMessage(i,bc+"\n\nDLG TEAM")

            elif "Gmid @" in msg.text:
                if 'MENTION' in msg.contentMetadata.keys() != None:
                    names = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                        try:
                            dz.sendMessage(msg.to,str(mention['M']))
                        except Exception as e:
                            pass
            elif "info @" in text.lower():
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]                
                mmid = dz.getContact(key1)
                vcx = mmid.mid
                dz.sendContact(msg.to,vcx)
#==================[ REBOOT ]===================
            elif msg.text in ["Reboot"]:
                    try:
                        dz.sendMessage(msg.to,"Restarting .....")
                        restartBot()
                    except:
                        dz.sendMessage(msg.to,"Please wait")
                        restartBot()
                        pass
            elif msg.text in ["Refresh"]:
                    dz.sendMessage(msg.to, "Bot has been restarted")
                    restart_program()
                
            elif msg.text in ["Runtime"]:
                timeNow = time.time()
                runtime = timeNow - botStart
                runtime = format_timespan(runtime)
                dz.sendMessage(msg.to, "ʙᴏᴛ ʀᴜɴ  {}".format(str(runtime)))
            
            elif "Spamtag @" in msg.text: 
                _name = msg.text.replace("Spamtag @","")
                _nametarget = _name.rstrip(' ')
                gs = dz.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        xname = g.displayName
                        xlen = str(len(xname)+1)
                        msg.contentType = 0
                        msg.text = "@"+xname+" "
                        msg.contentMetadata ={'MENTION':'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(g.mid)+'}]}','EMTVER':'4'}
                        dz.sendMessage(msg.to,msg.text,msg.contentMetadata)
                        dz.sendMessage(msg.to,msg.text,msg.contentMetadata)
                        dz.sendMessage(msg.to,msg.text,msg.contentMetadata)
                        dz.sendMessage(msg.to,msg.text,msg.contentMetadata)
                        dz.sendMessage(msg.to,msg.text,msg.contentMetadata)
                        dz.sendMessage(msg.to,msg.text,msg.contentMetadata)
                        dz.sendMessage(msg.to,msg.text,msg.contentMetadata)
                        dz.sendMessage(msg.to,msg.text,msg.contentMetadata)

            elif msg.text in ["/blank"]:
                blank = "'"
                dz.sendContact(msg.to, blank)	
#=============================================
            elif msg.text in ["My groups"]:
                    gid = dz.getGroupIdsJoined()
                    h = ""
                    for i in gid:
                        gn = dz.getGroup(i).name
                        h += "╠ ➽ %s\n" % (gn)
                    dz.sendMessage(msg.to,"╔══════════════\n╠⟦ My Groups ⟧\n╔══════════════\n"+ h +"╚══════════════")
#=============================================
            elif msg.text in ["Tag"]:
                group = dz.getGroup(msg.to)
                nama = [contact.mid for contact in group.members]
                k = len(nama)//20
                for a in range(k+1):
                    txt = u''
                    s=0
                    b=[]
                    for i in group.members[a*20 : (a+1)*20]:
                        b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                        s += 7
                        txt += u'@Zero \n'
                    dz.sendMessage(msg.to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
#=============================================
            elif msg.text in ["Cancel all"]:
                group = dz.getGroup(msg.to)
                if group.invitee is None:
                    dz.sendMessage(op.message.to, "No pending invites to cancel")
                else:
                    nama = [contact.mid for contact in group.invitee]
                    for x in nama:
                        time.sleep(0.2)
                        dz.cancelGroupInvitation(msg.to, [x])
                    dz.sendMessage(msg.to, "Deleted all pending invites")
#=============================================
            elif text.lower() in ["member list"]:   
                kontak = dz.getGroup(msg.to)
                group = kontak.members
                msgs="╔══════════════\n╠⟦ ᴍᴇᴍʙᴇʀ ʟɪsᴛ ⟧\n╔══════════════"
                for ids in group:
                    msgs+="\n╠ ➽ %s" % (ids.displayName)
                msgs+="\n╚══════════════\n╠⟦ᴛᴏᴛᴀʟ ᴍᴇᴍʙᴇʀs : %i ⟧\n" % len(group)+"╚══════════════"
                dz.sendMessage(msg.to, msgs)
#=============================================
        if op.type == 26:
            msg = op.message
            text = msg.text
            if msg.toType == 2:
                if wait["mimic"] == True:
                    if 'tagall' in text.lower():
                        dz.sendMessage(msg.to,"Tag")
                    elif 'Spamtag @' in msg.text: 
                        dz.sendMessage(msg.to,msg.text,msg.contentMetadata)
                    elif '/help' in text.lower():
                        dz.sendMessage(msg.to,helpMessage)
                    elif '/reboot' in text.lower():
                        dz.sendMessage(msg.to,"Reboot")
                    elif '/member list' in text.lower():
                        kontak = dz.getGroup(msg.to)
                        group = kontak.members
                        msgs="╔══════════════\n╠⟦ ᴍᴇᴍʙᴇʀ ʟɪsᴛ ⟧\n╔══════════════"
                        for ids in group:
                            msgs+="\n╠ ➽ %s" % (ids.displayName)
                        msgs+="\n╚══════════════\n╠⟦ᴛᴏᴛᴀʟ ᴍᴇᴍʙᴇʀs : %i ⟧\n" % len(group)+"╚══════════════"
                        dz.sendMessage(msg.to, msgs)
                    elif '/mygroups' in text.lower():
                        dz.sendMessage(msg.to,"My groups")
                    elif '/cancel all' in text.lower():
                        dz.sendMessage(msg.to,"Cancel all")
                    elif 'info @' in text.lower():
                        dz.sendMessage(msg.to,msg.text,msg.contentMetadata)
                    elif '/time' in text.lower():
                        dz.sendMessage(msg.to,"Time")
                    elif '/ginfo' in text.lower():
                        if msg.toType == 2:
                            ginfo = dz.getGroup(msg.to)
                            gCreator = ginfo.creator.displayName
                            if gCreator is None:
                                gCreator = "Error"
                            if ginfo.invitee is None:
                                sinvitee = "0"
                            else:
                                sinvitee = str(len(ginfo.invitee))
                            if ginfo.preventedJoinByTicket == True:
                                u = "close"
                            else:
                                u = "open"
                            try:
                                dz.sendMessage(msg.to,"╔══════════════\n╠═ GROUP NAME \n╠ ➽ " + str(ginfo.name) + "\n╠══════════════\n╠═ GROUP CREATOR \n╠ ➽ " + gCreator + "\n╠══════════════\n╠ ➽ ᴍᴇᴍʙᴇʀs: " + str(len(ginfo.members)) + " ᴍᴇᴍʙᴇʀs\n╠ ➽ ᴘᴇɴᴅɪɴɢ: " + sinvitee + " ᴘᴇᴏᴘʟᴇ\n╠ ➽ ᴜʀʟ : " + u + "\n╚══════════════")
                                dz.sendMessage(msg.to,"「ɢɪᴅ:」 \n➽ " + msg.to)
                                dz.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/"+ ginfo.pictureStatus)
                            except:
                                dz.sendMessage(msg.to,"╔══════════════\n╠═ GROUP NAME \n╠ ➽ " + str(ginfo.name) + "\n╠══════════════\n╠═ GROUP CREATOR \n╠ ➽ " + gCreator + "\n╚══════════════")
                                dz.sendMessage(msg.to,"「ɢɪᴅ:」 \n➽ " + msg.to)
                                dz.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/"+ ginfo.pictureStatus)
                    elif '/calendar' in text.lower():
                        dz.sendImage(msg.to,"/home/pi/Downloads/calendar.jpg")
                    elif '/runtime' in text.lower():
                        dz.sendMessage(msg.to,"Runtime")
                    elif '/website' in text.lower():
                        dz.sendMessage(msg.to,"https://darklegendsgaming.com")
                    elif '/youtube' in text.lower():
                        dz.sendMessage(msg.to,"https://www.youtube.com/channel/UCPW1tTAU9hLqKIl-yzhnqYw")
                    elif '/facebook' in text.lower():
                        dz.sendMessage(msg.to,"https://www.facebook.com/Dark-Legends-Gaming-347046466196913")
                    elif '/teamspeak' in text.lower():
                        dz.sendMessage(msg.to,"fekhole.teamspeak3.com:3171")
                    elif '/discord' in text.lower():
                        dz.sendMessage(msg.to,"https://discord.gg/3pe7qFx")
                    elif '/family' in text.lower():
                        dz.sendMessage(msg.to,family)
                    elif '/tech' in text.lower():
                        dz.sendMessage(msg.to,tech)
                    elif '/games' in text.lower():
                        dz.sendMessage(msg.to,games)
                    elif '/instagram' in text.lower():
                        dz.sendMessage(msg.to,"https://www.instagram.com/dark_legends_gaming")
                    elif '/twitter' in text.lower():
                        dz.sendMessage(msg.to,"https://www.twitter.com/DLG_Online")
                    elif '/donate' in text.lower():
                        dz.sendMessage(msg.to,donate)
                    elif '/merch' in text.lower():
                        dz.sendMessage(msg.to,"https://shop.spreadshirt.com/dark-legends-gaming")
                    elif "bcgroup: " in text.lower():
                        dz.sendMessage(msg.to,msg.text)
                    elif "testgroup: " in text.lower():
                        dz.sendMessage(msg.to,msg.text)
                    elif "/groupid" in text.lower():
                        dz.sendMessage(msg.to,msg.to)
                    else:
                        pass
                else:
                    pass
            else:
                pass
    except Exception as error:
        logError(error)
#==============================================================================#

while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                dhenzaBot(op)
                # jangan di hapus bagian  dhenza, byar tidak terjadi troblle!
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)

