# -*- coding: utf-8 -*-

from LineAPI.linepy import *
from LineAPI.akad.ttypes import Message
from LineAPI.akad.ttypes import ContentType as Type
from LineAPI.akad.ttypes import ChatRoomAnnouncementContents
from LineAPI.akad.ttypes import ChatRoomAnnouncement
from datetime import datetime, timedelta
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, multiprocessing, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib3, urllib.parse, html5lib, wikipedia, atexit, timeit, pafy, youtube_dl, traceback

dz = LINE("EHwlv7Dxz6xMfiPai2J8.AlUwBuOESO9tzvoy4jATca.zX6+ff/u7SvtBCybjKHvbVSDgtst5X1wie4tdg9GZw0=")
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
══  MAIN GUILDS  ══
══  DL.    ═  K480 ══ 
══  DL#  ═  K480 ══
══  dla    ═  K480 ══
══  D@L  ═  K480 ══
══  DlW   ═  K480 ══
══  dl8    ═  K262 ══
══  dDL   ═  K458 ══
══  DL^    ═  K262 ══
════════════
══  SUB  GUILDS  ══
══  Dlx     ═  K480 ══
══  DLD   ═  K480 ══
══  pdl     ═  K480 ══
══  wDL   ═  K480 ══
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
            if wait["Autojoin"] == True:
                dz.acceptGroupInvitation(op.param1)
        if op.type == 13:
            if op.param2 in org["inviter"]:
                dz.acceptGroupInvitation(op.param1)
#=====================[ PROTECT INVITE ]======================
        if op.type == 12:
            if op.param1 in pro["Protectinvite"]:
                X = dz.getGroup(op.param1)
                orang = [contact.mid for contact in X.invitee]
                for m in orang:
                    org["invitan"][m]=True
                    with open('setting.json', 'w') as fp:
                        json.dump(org, fp, sort_keys=True, indent=4)
        if op.type == 13:
            if op.param1 in pro["Protectinvite"]:
                if op.param2 in org["Friend"]:
                    if op.param3 in org["Friend"]:
                        pass
                    else:
                        X = dz.getGroup(op.param1)
                        orang = [contact.mid for contact in X.invitee]
                        for m in orang:
                            org["invitan"][m]=True
                            with open('org.json', 'w') as fp:
                                json.dump(org, fp, sort_keys=True, indent=4)
                else:
                    if op.param3 in org["Friend"]:
                        pass
                    else:
                        try:
                            dz.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            dz.sendMessage(op.param1,"limit")
#==============[ WELCOME] ===============
        if op.type == 17:
            if pro["wellcome"] == True:
                if op.param1 in pro["Protectjoin"]:
                    if op.param2 not in org["invitan"]:
                        pass
                    else:
                        ginfo = dz.getGroup(op.param1)
                        dzx = dz.getContact(op.param2)
                        dz.sendMessage(op.param1, "Ehhh  " + str(dzx.displayName) + "\nWellcome to " + str(ginfo.name) +"\n"+ Dhenza["welmsg"])
                        dz.sendImageWithURL(op.param1,"http://dl.profile.line-cdn.net/" + ydx.pictureStatus)
                else:
                    ginfo = dz.getGroup(op.param1)
                    dzx = dz.getContact(op.param2)
                    dz.sendMessage(op.param1, "Ehhh  " + str(dzx.displayName) + "\nWellcome to " + str(ginfo.name) +"\n"+ Dhenza["welmsg"])
                    dz.sendImageWithURL(op.param1,"http://dl.profile.line-cdn.net/" + dzx.pictureStatus)                    

#=============== [ NOTIFIED_KICKOUT_FROM_GROUP ]===========
        if op.type == 19:
            if op.param1 in pro["Autokick"]:
                if op.param2 in org["Friend"]:
                    pass
                else:
                    try:
                        dz.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        dz.sendMessage(op.param1,"limit")
                   
						
            if op.param3 in org["Friend"]:
                if op.param2 in org["Friend"]:
                    pass
                else:                   
                    try:
                        dz.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        dz.sendMessage(op.param1,"limit")
                    try:
                    	dz.inviteIntoGroup(op.param1,[op.param3])
                    except:
                        try:
                            G = dz.getGroup(op.param1)
                            G.preventJoinByTicket = False
                            dz.updateGroup(G)
                            invsend = 0
                            Ticket = dz.reissueGroupTicket(op.param1)
                            dz.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G = dz.getGroup(op.param1)
                            G.preventJoinByTicket = True
                            dz.updateGroup(G)
                        except Exception as e:
                            print(e)

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
            
            elif msg.text in ["Ginfo"]:
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

                    
            elif msg.text in ["Mimic list"]:
                if org["tmimic"] == {}:
                    dz.sendMessage(msg.to,"Not have list")
                else:
                    mc = []
                    for mi_d in org["tmimic"]:
                        mc.append(mi_d)
                    pass
                    cban = dz.getContacts(mc)
                    nban = []
                    for x in range(len(cban)):
                        nban.append(cban[x].displayName)
                    pass
                    jo = "\n╠ ➽ ".join(str(i) for i in nban)
                    dz.sendMessage(msg.to,"╔══════════════\n╠⟦ ᴍɪᴍɪᴄ ʟɪsᴛ ⟧\n╔══════════════\n╠ ➽ %s\n╚══════════════\n╠⟦ Total: %s ⟧\n"%(jo,str(len(cban)))+"╚══════════════")
            elif "Addmimic @" in msg.text:
                if 'MENTION' in msg.contentMetadata.keys() != None:
                    names = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    G = dz.getGroupIdsJoined()
                    cgroup = dz.getGroups(G)
                    ngroup = ""
                    for mention in mentionees:
                        org['tmimic'][mention['M']] = True
                        dz.sendMessage(msg.to,"ᴍɪᴍɪᴄ ᴀᴅᴅᴇᴅ")
                        with open('org.json', 'w') as fp:
                            json.dump(org, fp, sort_keys=True, indent=4)

            elif "addinviter @" in msg.text:
                if 'MENTION' in msg.contentMetadata.keys() != None:
                    names = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    G = dz.getGroupIdsJoined()
                    cgroup = dz.getGroups(G)
                    ngroup = ""
                    for mention in mentionees:
                        org['inviter'][mention['M']] = True
                        dz.sendMessage(msg.to,"Inviter Added")
                        with open('org.json', 'w') as fp:
                            json.dump(org, fp, sort_keys=True, indent=4)

            elif "Unmimic @" in msg.text:
                if 'MENTION' in msg.contentMetadata.keys() != None:
                    names = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    G = dz.getGroupIdsJoined()
                    cgroup = dz.getGroups(G)
                    ngroup = ""
                    for mention in mentionees:
                        del org['tmimic'][mention['M']]
                        dz.sendMessage(msg.to,"ᴍɪᴍɪᴄ ᴅᴇʟᴇᴛᴇᴅ")
                        with open('org.json', 'w') as fp:
                            json.dump(org, fp, sort_keys=True, indent=4)
            elif "deleteinviter @" in msg.text:
                if 'MENTION' in msg.contentMetadata.keys() != None:
                    names = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    G = dz.getGroupIdsJoined()
                    cgroup = dz.getGroups(G)
                    ngroup = ""
                    for mention in mentionees:
                        del org['inviter'][mention['M']]
                        dz.sendMessage(msg.to,"Inviter Deleted")
                        with open('org.json', 'w') as fp:
                            json.dump(org, fp, sort_keys=True, indent=4)
            elif "Mimic " in msg.text:
                xpesan = msg.text
                xres = xpesan.replace("Mimic ","")
                if xres == "off":
                    wait['mimic'] = False
                    dz.sendMessage(msg.to,"ᴍɪᴍɪᴄ sᴇᴛ ᴛᴏ ᴏғғ")
                elif xres == "on":
                    wait['mimic'] = True
                    dz.sendMessage(msg.to,"ᴍɪᴍɪᴄ sᴇᴛ ᴛᴏ ᴏɴ")

            elif msg.text in ["Reject"]:
              if msg.toType == 2:
                gid = dz.getGroupIdsInvited()
                for i in gid:
                    dz.rejectGroupInvitation(i)
                dz.sendMessage(msg.to,"done reject")

            elif "Bcgroup: " in msg.text:
                bc = msg.text.replace("Bcgrup: ","")
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
            elif "Kick @" in msg.text:
                if 'MENTION' in msg.contentMetadata.keys() != None:
                    names = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                        try:
                            dz.kickoutFromGroup(msg.to, [mention['M']])							
                        except:
                            dz.sendMessage(msg.to, "ʟɪᴍɪᴛ ʙᴏss..")
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

            elif msg.text in ["Status"]:
                md = "╔════════════════════\n╠SILENT TΣΔM βΩT\n╠════════════════════\n"
                if wait["Autojoin"] == True: md+="╠➣ᴀᴜᴛᴏᴊᴏɪɴ : ✔\n"
                else:md+="╠➣ᴀᴜᴛᴏᴊᴏɪɴ : ❌\n"
                if resp["Tag1"] == True: md+="╠➣ ᴍᴇɴᴛɪᴏɴ1 : ✔\n"
                else:md+="╠➣ᴍᴇɴᴛɪᴏɴ1 : ❌\n"
                if resp["Tag2"] == True: md+="╠➣ᴍᴇɴᴛɪᴏɴ2 : ✔\n"
                else:md+="╠➣ᴍᴇɴᴛɪᴏɴ2 : ❌\n"
                if resp["Tag3"] == True: md+="╠➣ᴍᴇɴᴛɪᴏɴ3 : ✔\n"
                else:md+="╠➣ᴍᴇɴᴛɪᴏɴ3 : ❌\n"
                if wait["Invite"] == True: md+="╠➣ɪɴᴠɪᴛᴇ : ✔\n"
                else:md+="╠➣ɪɴᴠɪᴛᴇ : ❌\n"
                if wait["LikeOn"] == True: md+="╠➣ᴀᴜᴛᴏʟɪᴋᴇ : ✔\n"
                else:md+="╠➣ᴀᴜᴛᴏʟɪᴋᴇ : ❌\n"
                if wait["getmid"] == True: md+="╠➣ɢᴇᴛ ᴍɪᴅ : ✔\n"
                else:md+="╠➣ɢᴇᴛ ᴍɪᴅ : ❌\n"
                if wait["Timeline"] == True: md+="╠➣ɢᴇᴛ ᴘᴏsᴛ : ✔\n"
                else:md+="╠➣ɢᴇᴛ ᴘᴏsᴛ : ❌\n"
                if pro["wellcome"] == True: md+="╠➣ᴡeʟʟᴄᴏᴍᴇ ᴛᴇᴋs : ✔\n"
                else:md+="╠➣ᴡᴇʟʟᴄᴏᴍᴇ ᴛᴇᴋs : ❌\n"
                if pro["bymsg"] == True: md+="╠➣ʙʏᴇ ᴍsɢ ᴛᴇᴋs : ✔\n╠════════════════════\n╠➣line://ti/p/~tambotprotect\n╠➣line://ti/p/~dhenz415\n╚════════════════════"
                else:md+="╠➣ʙʏᴇ ᴍsɢ ᴛᴇᴋs : ❌\n╠════════════════════\n╠➣line://ti/p/~tambotprotect\n╠➣line://ti/p/~tambotprotect\n╚════════════════════"
                dz.sendMessage(msg.to,md)

#=============================================
            elif msg.text in ["My groups"]:
                    gid = dz.getGroupIdsJoined()
                    h = ""
                    for i in gid:
                        gn = dz.getGroup(i).name
                        h += "╠ ➽ %s\n" % (gn)
                    dz.sendMessage(msg.to,"╔══════════════\n╠⟦ My Groups ⟧\n╔══════════════\n"+ h +"╚══════════════")
#=============================================
            elif msg.text in ["Gift"]:
                    giftnya={'MSGTPL': '5',
                            'PRDTYPE': 'THEME',
                            'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58'}           
                    dz.sendMessage(msg.to,None, contentMetadata=giftnya, contentType=9)
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
                        dz.sendMessage(msg.to,"Member list")
                    elif '/mygroups' in text.lower():
                        dz.sendMessage(msg.to,"My groups")
                    elif '/cancel all' in text.lower():
                        dz.sendMessage(msg.to,"Cancel all")
#                    elif 'kick @' in text.lower():
#                        dz.sendMessage(msg.to,msg.text,msg.contentMetadata)
                    elif 'info @' in text.lower():
                        dz.sendMessage(msg.to,msg.text,msg.contentMetadata)
                    elif 'addinviter @' in text.lower():
                        dz.sendMessage(msg.to,msg.text,msg.contentMetadata)
                    elif 'deleteinviter @' in text.lower():
                        dz.sendMessage(msg.to,msg.text,msg.contentMetadata)
                    elif '/time' in text.lower():
                        dz.sendMessage(msg.to,"Time")
                    elif '/ginfo' in text.lower():
                        dz.sendMessage(msg.to,"Ginfo")
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
