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

dz = LINE("EKv4DxRG9K99SbmN0Ns8.AlUwBuOESO9tzvoy4jATca.DCWRyQT3qUX9tSQYHsc/sARyi+pVnnIGRf9F8XK67/c=")
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
╠⍟➣  /bus
╠⍟➣  /boarding
╠═══════════
"""

family =""" ✇✇  DLG FAMILY  ✇✇
════════════
══  DL.    ═  K518 ══ 
══  D@L  ═  K480 ══
══  dl8    ═  K41 ══
══  dDL   ═  K458 ══
══  DL^    ═  K583 ══
══  DLD   ═  K518 ══
══  DLP   ═  K277 ══
══  pdl     ═  K480 ══
══  wDL   ═  K518 ══
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

dlmadmins =""" DLm Bus Admins
════════════
[DLm/dla] Veruca Salt
➣ Saltyv
════════════
[dla] Phleth
➣ phleth
════════════
[dla] xAstraea
➣ xcalliope
════════════
[dla] Zambuki
➣ zambuki
════════════
[dla] Lady 
➣ bb2387 
════════════
[DL.] |6| SIX |6|
➣ 6sixxx6
════════════
[DWL] Morgool
➣ wargool
════════════
[dla] Sarge Pepper
➣ wtwhitloc
════════════
[dla/Dlx] Ms2Pac
➣ msjsoconfident 
════════════
[dla] Gold Factory
➣ jdhalf2727
════════════
[dla] I Am Rocket
➣ tjnocar
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

Dhenza = {
    "comment":"╔═════════════════════\nAuto like by:TBP\n╚══════════════════════",
    "cctvteks":"Masuk sayang\nUdah keciduk juga",
    "message":"╔═════════════════════\nThanks for adding me!\n╚══════════════════════",
    "welmsg":"╔═════════════════════\nSILENT TΣΔM βΩT\n╚══════════════════════",
    "leftmsg":"╔═════════════════════\nSILENT TΣΔM βΩT\n╚══════════════════════",
    "tagteks1":"Tag mau minta jajan ya",
    "tagteks2":"iya syang",
    "tagteks3":"kangen ya//-.."
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
            if op.param1 == "cd6ef278e18b895a1dbfc371c230201d4":
                dzx = dz.getContact(op.param2)
                dz.sendMessage(op.param1, "Hello " + str(dzx.displayName) + "\nWelcome to " + str(ginfo.name))
                dz.sendImageWithURL(op.param1,"http://dl.profile.line-cdn.net/" + dzx.pictureStatus)

        if op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 2:
                if msg.contentType == 7:
                    if resp["csticker1"] == True:
                        msg.contentType = 0
                        stk_id = msg.contentMetadata['STKID']
                        stk_ver = msg.contentMetadata['STKVER']
                        pkg_id = msg.contentMetadata['STKPKGID']
                        tikell = "STKID1: %s STKPKGID: %s STKVER: %s" % (stk_id,pkg_id,stk_ver)
                        dz.sendMessage(msg.to, tikell)

                    elif resp["csticker2"] == True:
                        msg.contentType = 0
                        stk_id = msg.contentMetadata['STKID']
                        stk_ver = msg.contentMetadata['STKVER']
                        pkg_id = msg.contentMetadata['STKPKGID']
                        tikell = "STKID2: %s STKPKGID: %s STKVER: %s" % (stk_id,pkg_id,stk_ver)
                        dz.sendMessage(msg.to, tikell)

                    elif resp["csticker3"] == True:
                        msg.contentType = 0
                        stk_id = msg.contentMetadata['STKID']
                        stk_ver = msg.contentMetadata['STKVER']
                        pkg_id = msg.contentMetadata['STKPKGID']
                        tikell = "STKID3: %s STKPKGID: %s STKVER: %s" % (stk_id,pkg_id,stk_ver)
                        dz.sendMessage(msg.to, tikell)
                    else:
                        pass
                        
                if msg.contentType == 13:
                    if wait["atarget"]==True:
                        if msg.contentMetadata["mid"] in org["Target"]:
                            dz.sendMessage(msg.to, "was save")
                            wait["atarget"]=False
                        else:
                            org["Target"][msg.contentMetadata["mid"]] = True
                            with open('org.json', 'w') as fp:
                                json.dump(org, fp, sort_keys=True, indent=4)
                            dz.sendMessage(msg.to, "save succes")
                            wait["atarget"]=False

                    elif wait["dtarget"]==True:
                        if msg.contentMetadata["mid"] in org["Target"]:
                            del org["Target"][msg.contentMetadata["mid"]]
                            with open('org.json', 'w') as fp:
                                json.dump(org, fp, sort_keys=True, indent=4)
                            wait["dtarget"]=False
                            dz.sendMessage(msg.to,"Target deleted")
                        else:
                            dz.sendMessage(msg.to,"Target not found")
#=====================[ MODE SILENT ]=================--======
                if msg.contentType == 13:
                    if wait["asilent"]==True:
                        if msg.contentMetadata["mid"] in org["Silent"]:
                            dz.sendMessage(msg.to, "siap on bos")
                            wait["asilent"]=False
                        else:
                            org["Silent"][msg.contentMetadata["mid"]] = True
                            with open('org.json', 'w') as fp:
                                json.dump(org, fp, sort_keys=True, indent=4)
                            dz.sendMessage(msg.to, "TBP succes")
                            wait["asilent"]=False

                    elif wait["dsilent"]==True:
                        if msg.contentMetadata["mid"] in org["Silent"]:
                            del org["Silent"][msg.contentMetadata["mid"]]
                            with open('org.json', 'w') as fp:
                                json.dump(org, fp, sort_keys=True, indent=4)
                            dz.sendMessage(msg.to,"Silent deleted")
                            wait["dsilent"]=False
                        else:
                            dz.sendMessage(msg.to,"Silent not found")
                            wait["dsilent"]=False
                    else:
                        pass
#=====================[ SEPAM ]========================
                if msg.contentType == 13:
                    if wait["getmid"]==True:
                        x = msg.contentMetadata["mid"]
                        dz.sendMessage(msg.to,x)
                        wait["getmid"]=False

                if msg.contentType == 13:
                    if wait["santet"]==True:
                        x = msg.contentMetadata["mid"]
                        dz.findAndAddContactsByMid(x)
                        try:
                            M = Message()
                            M.to = x
                            M.contentType = 13
                            M.contentMetadata = {'mid': "'"}
                            dz.sendMessage(M)
                            dz.sendMessage(M)
                            wait["santet"]=False
                        except:
                            pass
#========================[ INVITE ]===================
                if msg.contentType == 13:
                    if wait["afriend"]==True:
                        if msg.contentMetadata["mid"] in org["Friend"]:
                            dz.sendMessage(msg.to, "Team done")
                            wait["afriend"]=False
                        else:
                            org["Friend"][msg.contentMetadata["mid"]] = True
                            with open('org.json', 'w') as fp:
                                json.dump(org, fp, sort_keys=True, indent=4)
                            dz.sendMessage(msg.to, "Tem succes")
                            wait["afriend"]=False

                    elif wait["dfriend"]==True:
                        if msg.contentMetadata["mid"] in org["Friend"]:
                            del org["Friend"][msg.contentMetadata["mid"]]
                            with open('org.json', 'w') as fp:
                                json.dump(org, fp, sort_keys=True, indent=4)
                            dz.sendMessage(msg.to,"Hapus teman")
                            wait["dfriend"]=False
                        else:
                            dz.sendMessage(msg.to,"Teman tidak di temukan")
                            wait["dfriend"]=False

#=====================[ MODE INVITE ]==================
                if msg.contentType == 13:
                    if wait["Invite"] == True:
                        _name = msg.contentMetadata["displayName"]
                        invite = msg.contentMetadata["mid"]
                        groups = dz.getGroup(msg.to)
                        pending = groups.invitee
                        targets = []
                        for s in groups.members:
                            if _name in s.displayName:
                                dz.sendMessage(msg.to,"-> " + _name + " was here")
                                wait["Invite"] = False
                                break         
                            else:
                                targets.append(invite)
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                dz.findAndAddContactsByMid(target)
                                dz.inviteIntoGroup(msg.to,[target])
                                dz.sendMessage(msg.to,"sᴜᴄᴄᴇs ᴍᴇɴɢɪɴᴠɪᴛᴇ ᴊᴏᴍʙʟᴏ ɪɴɪ \n➡" + _name)
                                wait["Invite"] = False
                                break
                else:
                    pass
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

            elif "testgroup: " in msg.text:
                bc = msg.text.replace("testgroup: ","")
                dz.sendMessage("cd6ef278e18b895a1dbfc371c230201d4",bc+"\n\nDLG TEAM")

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
                        
            elif msg.text in ["Sp"]:
                start = time.time()
                dz.sendMessage(msg.to, "One sec Boss..")
                elapsed_time = time.time() - start
                dz.sendMessage(msg.to, "%ss" % (elapsed_time))
                
            elif msg.text in ["Refresh"]:
                    dz.sendMessage(msg.to, "Bot has been restarted")
                    restart_program()
                    
            elif msg.text in ["Time"]:
                timeNow = datetime.now()
                timeHours = datetime.strftime(timeNow,"(%H:%M)")
                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                bulan = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
                inihari = datetime.today()
                hr = inihari.strftime('%A')
                bln = inihari.strftime('%m')
                for i in range(len(day)):
                    if hr == day[i]: hasil = day[i]
                for k in range(0, len(bulan)):
                    if bln == str(k): bln = bulan[k-1]
                rst = hasil + ", " + inihari.strftime('%d') + " - " + bln + " - " + inihari.strftime('%Y') + "\nTime : [ " + inihari.strftime('%H:%M:%S') + " ]"
                dz.sendMessage(msg.to, rst)
                
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

#=================================================
            elif msg.text in ["Left on"]:
                pro["bymsg"]=True
                with open('pro.json', 'w') as fp:
                    json.dump(pro, fp, sort_keys=True, indent=4)
                dz.sendMessage(msg.to, "ᴏᴜᴛ ᴍᴇssᴀɢᴇ ᴀᴄᴛɪᴠᴇ")
            elif msg.text in ["Left off"]:
                pro["bymsg"]=False
                with open('pro.json', 'w') as fp:
                    json.dump(pro, fp, sort_keys=True, indent=4)
                dz.sendMessage(msg.to, "ᴏᴜᴛ ᴍᴇssᴀɢᴇ ɴᴏᴛ ᴀᴄᴛɪᴠᴇ")
#=================================================
            elif msg.text in ["Welcome on"]:
                pro["wellcome"]=True
                with open('pro.json', 'w') as fp:
                    json.dump(pro, fp, sort_keys=True, indent=4)
                dz.sendMessage(msg.to, "ᴡᴇʟʟᴄᴏᴍᴇ ᴍsɢ ᴀᴄᴛɪᴠᴇ")
            elif msg.text in ["Welcome off"]:
                pro["wellcome"]= False
                with open('pro.json', 'w') as fp:
                    json.dump(pro, fp, sort_keys=True, indent=4)
                dz.sendMessage(msg.to, "ᴡᴇʟʟᴄᴏᴍᴇ ᴍsɢ ɴᴏᴛ ᴀᴄᴛɪᴠᴇ")

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
            elif msg.text in ["Recover"]:
                thisgroup = dz.getGroups([msg.to])
                Mids = [contact.mid for contact in thisgroup[0].members]
                mi_d = Mids[:33]
                dz.createGroup("test", mi_d)
                dz.sendMessage(msg.to,"done")
#=============================================
            elif msg.text in ["Welcome"]:
                gs = dz.getGroup(msg.to)
                dz.sendMessage(msg.to,"ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ "+ gs.name)
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
                    elif 'addinviter @' in text.lower():
                        dz.sendMessage(msg.to,msg.text,msg.contentMetadata)
                    elif 'deleteinviter @' in text.lower():
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
                    elif '/dlcalendar' in text.lower():
                        dz.sendImage(msg.to,"/home/pi/Downloads/dlcalendar.jpg")
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
                    elif "/bus" in text.lower():
#                        dz.sendMessage(msg.to,"No bus scheduled due to guild fest")
                        dz.sendImageWithURL(msg.to,"https://darklegendsgaming.com/buspic")
                        timeBus = datetime(2019, 9 , 19, 0)
                        timediff = timeBus - datetime.now()
                        tdh = (timediff.seconds//3600) + (timediff.days*24)
                        tdm = ((timediff.seconds+60)//60)%60
                        timeBoard = datetime(2019, 9 , 18, 23, 30)
                        timediffboard = timeBoard - datetime.now()
                        tdbh = (timediffboard.seconds//3600) + (timediffboard.days*24)
                        tdbm = ((timediffboard.seconds+60)//60)%60
                        if tdbh < 0 and tdh == 0:
                            tdn = "Bus boarding is currently boarding! Hunt starts in " + str(tdm) + " minutes"
                            dz.sendMessage(msg.to, tdn)
                        if tdbh < 0 and tdh < 0:
                            tdn = "Next bus is currently being scheduled"
                            dz.sendMessage(msg.to, tdn)
                        if tdbh > 0 and tdh > 0:
                            tdn = "Bus boarding in " + str(tdbh) + " hours and " + str(tdbm) + " minutes. Hunt starts in " + str(tdh) + " hours and " + str(tdm) + " minutes"
                            dz.sendMessage(msg.to, tdn)
                    elif "/groupid" in text.lower():
                        dz.sendMessage(msg.to,msg.to)
                    elif "/boarding" in text.lower():
#                        dz.sendMessage(msg.to,"No bus scheduled due to guild fest")
                        timeBus = datetime(2019, 9 ,19, 0)
                        timediff = timeBus - datetime.now()
                        tdh = (timediff.seconds//3600) + (timediff.days*24)
                        tdm = ((timediff.seconds+60)//60)%60
                        timeBoard = datetime(2019, 9 , 18, 23, 30)
                        timediffboard = timeBoard - datetime.now()
                        tdbh = (timediffboard.seconds//3600) + (timediffboard.days*24)
                        tdbm = ((timediffboard.seconds+60)//60)%60
                        if tdbh < 0 and tdh == 0:
                            tdn = "Bus boarding is currently boarding! Hunt starts in " + str(tdm) + " minutes"
                            dz.sendMessage(msg.to, tdn)
                        if tdbh < 0 and tdh < 0:
                            tdn = "Next bus is currently being scheduled"
                            dz.sendMessage(msg.to, tdn)
                        if tdbh >= 0 and tdh > 0:
                            tdn = "Bus boarding in " + str(tdbh) + " hours and " + str(tdbm) + " minutes. Hunt starts in " + str(tdh) + " hours and " + str(tdm) + " minutes"
                            dz.sendMessage(msg.to, tdn)
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
