#!/usr/bin/env python

import sys
import json
import random
import datetime

import io
import requests
import socket
from adapt.intent import IntentBuilder


def speech(text):
    global o
    o["speech"] = {"text": text}


# get json from stdin and load into python dict
o = json.loads(sys.stdin.read())

intent = o["intent"]["name"]
msg = o["text"]

if intent == "GetTime":
    now = datetime.datetime.now()
    speech("It's %s %d %s." % (now.strftime('%H'), now.minute, now.strftime('%p')))

elif intent == "Hello":
    replies = ['Hi!', 'Hello!', 'Hey there!', 'Greetings.']
    speech(random.choice(replies))

elif intent == "PercentageControl":
    percentage_control(self,msg)
    replies = ['Okey', 'Done!', 'Adjusted as your like']
    speech(random.choice(replies))

elif intent == "ChangeState":
    things_onoff(self,msg)
    replies = ['Okey', 'Done!', 'Adjusted as your like']
    speech(random.choice(replies))

# convert dict to json and print to stdout
print(json.dumps(o))



    def send_post_openhab(self,item, signal): 
        URL= 'http://10.5.55.3:8080/rest/items/'+item
        headers = {
            'Content-Type': 'text/plain',
            'Accept': 'application/json',
        }

        data = signal
        url_archivo_salida = 'response.xml'

        try:
            resp = requests.post( URL, headers = headers, data = data )

        except Exception as e:
            print( 'The exception >> ' + type(e).__name__ )
            raise e

        else:
            #requests.codes.ok = 200 => OK
            if( resp.status_code == requests.codes.ok ):
                with open( url_archivo_salida, 'w' ) as f:
                    f.write( resp.text )
                    f.close()
            else:
                out = 'resp.status_code >> ' + str(resp.status_code) + ' != ' + str(requests.codes.ok) 

    def percentage_control(self,msg):

        utterance = msg.data["utterance"]
        number = str(extract_number(utterance))

        if "lights" in msg.data.get('utterance') or "light" in msg.data.get('utterance'):
            if "kitchen" in msg.data.get('utterance'):           
                if "to" in msg.data.get('utterance'):
                    self.send_post_openhab("Kueche_LichtDimmer", number)          
            if "living room" in msg.data.get('utterance'):           
                if "to" in msg.data.get('utterance'):
                    self.send_post_openhab("WZ_LichtDimmer", number) 

        if "blinds" in msg.data.get('utterance'):
            if "kitchen" in msg.data.get('utterance'):
                if "up" in msg.data.get('utterance') or "raise" in msg.data.get('utterance') :
                    self.send_post_openhab("Kuche_Jalousie1", "0")
                    self.send_post_openhab("Kuche_Jalousie2", "0")
                if "down" in msg.data.get('utterance') or "lower" in msg.data.get('utterance'):
                    self.send_post_openhab("Kuche_Jalousie1", "100")
                    self.send_post_openhab("Kuche_Jalousie2", "100")            
                elif "to" in msg.data.get('utterance'):
                    self.send_post_openhab("Kuche_Jalousie1", number)
                    self.send_post_openhab("Kuche_Jalousie2", number)                                  

            if "living room" in msg.data.get('utterance'):
                if "up" in msg.data.get('utterance') or "raise" in msg.data.get('utterance'):
                    self.send_post_openhab("WZ_Jalousien", "0")
                if "down" in msg.data.get('utterance') or "lower" in msg.data.get('utterance'):
                    self.send_post_openhab("WZ_Jalousien", "100")          
                elif "to" in msg.data.get('utterance'):
                    self.send_post_openhab("WZ_Jalousien", number)                

            if "all" in msg.data.get('utterance'):
                if "up" in msg.data.get('utterance') or "raise" in msg.data.get('utterance'):
                    self.send_post_openhab("Wohnung_Jalousien", "0")
                if "down" in msg.data.get('utterance') or "lower" in msg.data.get('utterance'):
                    self.send_post_openhab("Wohnung_Jalousien", "100")            
                elif "to" in msg.data.get('utterance'):
                    self.send_post_openhab("Wohnung_Jalousien", number)                               


    def things_onoff(self,msg):
        print (msg.data.get('utterance'))

        if "lights" in msg.data.get('utterance') or "light" in msg.data.get('utterance'):
            if "kitchen" in msg.data.get('utterance'):
                if "table" in msg.data.get('utterance'):
                    if "on" in msg.data.get('utterance'):          
                        self.send_post_openhab("Kueche1_KNX_Licht_Schalten", "ON")
                    if "off" in msg.data.get('utterance'):
                        self.send_post_openhab("Kueche1_KNX_Licht_Schalten", "OFF")          
                elif "work" in msg.data.get('utterance'):
                    if "on" in msg.data.get('utterance'):          
                        self.send_post_openhab("Kueche2_KNX_Licht_Schalten", "ON")
                    if "off" in msg.data.get('utterance'):
                        self.send_post_openhab("Kueche2_KNX_Licht_Schalten", "OFF")          
                else:
                    if "on" in msg.data.get('utterance'):          
                        self.send_post_openhab("Kueche_LichtDimmer", "100")
                    if "off" in msg.data.get('utterance'):
                        self.send_post_openhab("Kueche_LichtDimmer", "0")                                     
            if "living room" in msg.data.get('utterance'):       
                if "center" in msg.data.get('utterance'):
                    if "on" in msg.data.get('utterance'):          
                        self.send_post_openhab("WZ_KNX_Licht_Schalten", "ON")
                    if "off" in msg.data.get('utterance'):
                        self.send_post_openhab("WZ_KNX_Licht_Schalten", "OFF")          
                else:
                    if "on" in msg.data.get('utterance'):          
                        self.send_post_openhab("WZ_LichtDimmer", "100")
                    if "off" in msg.data.get('utterance'):
                        self.send_post_openhab("WZ_LichtDimmer", "0")          

        if "hob" in msg.data.get('utterance'):        
            if "on" in msg.data.get('utterance'):          
                self.send_post_openhab("Kueche_Platte", "ON")
            if "off" in msg.data.get('utterance'):
                self.send_post_openhab("Kueche_Platte", "OFF")          

    """def relax_mode(self,msg):
        self.send_post_openhab("WZ_LichtDimmer", "40")
        self.send_post_openhab("WZ_KNX_Licht_Schalten", "ON")
        self.send_post_openhab("Kueche_LichtDimmer", "10")
        self.send_post_openhab("WZ_Jalousien", "100")
        self.send_post_openhab("Kuche_Jalousie1", "80")
        self.send_post_openhab("Kuche_Jalousie2", "80")
        self.speak_dialog("Relax") """
                

    def stop(self):
        pass


