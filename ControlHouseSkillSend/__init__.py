# Importing IntentBuilder
from adapt.intent import IntentBuilder
# Importing MycroftSkill class
from mycroft.skills.core import MycroftSkill
from mycroft.util import extract_number

import io
import requests
import socket


class ControlHouseSkill(MycroftSkill):

    def __init__(self):
        super(ControlHouseSkill, self).__init__("ControlHousekill")

    def initialize(self):

        self.log.info(self.lang)                                                
        if self.lang == 'en-us':                                                
            self.speak('I am an english gentleman') 
            switch = IntentBuilder("ControlIntent").require("OnOff").build()
            self.register_intent(switch, self.things_onoff)

            percentage = IntentBuilder("ControlIntent1").require("Percentage").build()
            self.register_intent(percentage, self.things_control)

            music = IntentBuilder("ControlIntent2").require("MusicCommands").build()
            self.register_intent(music, self.music_control)
                                        
        elif self.lang == 'de-de':                                              
            self.speak('Ich bin Deutscher')   

            switchG = IntentBuilder("ControlIntentG").require("OnOffG").build()
            self.register_intent(switchG, self.things_onoffG)

            percentageG = IntentBuilder("ControlIntentG").require("PercentageG").build()
            self.register_intent(percentageG, self.things_controlG)

            musicG = IntentBuilder("ControlIntentG").require("MusicCommandsG").build()
            self.register_intent(musicG, self.music_controlG)


    def send_post_openhab(self,item, signal):
        URL= 'http://192.168.1.36:8080/rest/items/'+item
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

    def things_control(self,msg):

        utterance = msg.data["utterance"]
        number = str(extract_number(utterance))

        if "lights" in msg.data.get('utterance') or "light" in msg.data.get('utterance'):
            if "green" in msg.data.get('utterance'):           
                if "kitchen" in msg.data.get('utterance'):
                        self.send_post_openhab("HueColorLamp1_Color_Color", "120,100,100")
                        self.speak_dialog("BlindsAdjust")
                if "living room" in msg.data.get('utterance'):
                        self.send_post_openhab("HueBulb_Color_Color", "120,100,100")
                        self.speak_dialog("BlindsAdjust")
                elif "room" in msg.data.get('utterance') or "bedroom" in msg.data.get('utterance'):                
                        self.send_post_openhab("HueColorLamp2_Color_Color", "120,100,100")
                        self.speak_dialog("BlindsAdjust")                
            if "red" in msg.data.get('utterance'):           
                if "kitchen" in msg.data.get('utterance'):
                        self.send_post_openhab("HueColorLamp1_Color_Color", "0,100,100")
                        self.speak_dialog("BlindsAdjust")
                if "living room" in msg.data.get('utterance'):
                        self.send_post_openhab("HueBulb_Color_Color", "0,100,100")
                        self.speak_dialog("BlindsAdjust")
                elif "room" in msg.data.get('utterance') or "bedroom" in msg.data.get('utterance'):                
                        self.send_post_openhab("HueColorLamp2_Color_Color", "0,100,100")
                        self.speak_dialog("BlindsAdjust") 
            if "blue" in msg.data.get('utterance'):           
                if "kitchen" in msg.data.get('utterance'):
                        self.send_post_openhab("HueColorLamp1_Color_Color", "202,100,100")
                        self.speak_dialog("BlindsAdjust")
                if "living room" in msg.data.get('utterance'):
                        self.send_post_openhab("HueBulb_Color_Color", "202,100,100")
                        self.speak_dialog("BlindsAdjust")
                elif "room" in msg.data.get('utterance') or "bedroom" in msg.data.get('utterance'):                
                        self.send_post_openhab("HueColorLamp2_Color_Color", "202,100,100")
                        self.speak_dialog("BlindsAdjust") 
            if "yellow" in msg.data.get('utterance'):           
                if "kitchen" in msg.data.get('utterance'):
                        self.send_post_openhab("HueColorLamp1_Color_Color", "46,99,100")
                        self.speak_dialog("BlindsAdjust")
                if "living room" in msg.data.get('utterance'):
                        self.send_post_openhab("HueBulb_Color_Color", "46,99,100")
                        self.speak_dialog("BlindsAdjust")
                elif "room" in msg.data.get('utterance') or "bedroom" in msg.data.get('utterance'):                
                        self.send_post_openhab("HueColorLamp2_Color_Color", "46,99,100")
                        self.speak_dialog("BlindsAdjust")  
            if "orange" in msg.data.get('utterance'):           
                if "kitchen" in msg.data.get('utterance'):
                        self.send_post_openhab("HueColorLamp1_Color_Color", "27,100,100")
                        self.speak_dialog("BlindsAdjust")
                if "living room" in msg.data.get('utterance'):
                        self.send_post_openhab("HueBulb_Color_Color", "27,100,100")
                        self.speak_dialog("BlindsAdjust")
                elif "room" in msg.data.get('utterance') or "bedroom" in msg.data.get('utterance'):                
                        self.send_post_openhab("HueColorLamp2_Color_Color", "27,100,100")
                        self.speak_dialog("BlindsAdjust") 
            if "pink" in msg.data.get('utterance'):           
                if "kitchen" in msg.data.get('utterance'):
                        self.send_post_openhab("HueColorLamp1_Color_Color", "326,100,100")
                        self.speak_dialog("BlindsAdjust")
                if "living room" in msg.data.get('utterance'):
                        self.send_post_openhab("HueBulb_Color_Color", "326,100,100")
                        self.speak_dialog("BlindsAdjust")
                elif "room" in msg.data.get('utterance') or "bedroom" in msg.data.get('utterance'):                
                        self.send_post_openhab("HueColorLamp2_Color_Color", "326,100,100")
                        self.speak_dialog("BlindsAdjust")                             
            if "purple" in msg.data.get('utterance'):           
                if "kitchen" in msg.data.get('utterance'):
                        self.send_post_openhab("HueColorLamp1_Color_Color", "263,78,100")
                        self.speak_dialog("BlindsAdjust")
                if "living room" in msg.data.get('utterance'):
                        self.send_post_openhab("HueBulb_Color_Color", "263,78,100")
                        self.speak_dialog("BlindsAdjust")
                elif "room" in msg.data.get('utterance') or "bedroom" in msg.data.get('utterance'):                
                        self.send_post_openhab("HueColorLamp2_Color_Color", "263,78,100")
                        self.speak_dialog("BlindsAdjust")      
            if "white" in msg.data.get('utterance'):           
                if "kitchen" in msg.data.get('utterance'):
                        self.send_post_openhab("HueColorLamp1_Color_Color", "191,1,100")
                        self.speak_dialog("BlindsAdjust")
                if "living room" in msg.data.get('utterance'):
                        self.send_post_openhab("HueBulb_Color_Color", "191,1,100")
                        self.speak_dialog("BlindsAdjust")
                elif "room" in msg.data.get('utterance') or "bedroom" in msg.data.get('utterance'):                
                        self.send_post_openhab("HueColorLamp2_Color_Color", "191,1,100")
                        self.speak_dialog("BlindsAdjust")                                          
            else: #si el número es distinto de null
                if "kitchen" in msg.data.get('utterance'):
                        self.send_post_openhab("HueColorLamp1_Color_Dimmer", number)
                        self.speak_dialog("BlindsAdjust")
                if "living room" in msg.data.get('utterance'):
                        self.send_post_openhab("HueBulb_Color_Dimmer", number)
                        self.speak_dialog("BlindsAdjust")
                elif "room" in msg.data.get('utterance') or "bedroom" in msg.data.get('utterance'):                
                        self.send_post_openhab("HueColorLamp2_Color_Dimmer", number)
                        self.speak_dialog("BlindsAdjust")

        if "blinds" in msg.data.get('utterance') or "shutters" in msg.data.get('utterance') or "blind" in msg.data.get('utterance'):
            if "kitchen" in msg.data.get('utterance'):
                if "up" in msg.data.get('utterance') or "raise" in msg.data.get('utterance') :
                    self.send_post_openhab("Kuche_Jalousie1", "0")
                    self.send_post_openhab("Kuche_Jalousie2", "0")
                    self.speak_dialog("BlindsUp")
                if "down" in msg.data.get('utterance') or "lower" in msg.data.get('utterance'):
                    self.send_post_openhab("Kuche_Jalousie1", "100")
                    self.send_post_openhab("Kuche_Jalousie2", "100")
                    self.speak_dialog("BlindsDown")              
                elif "to" in msg.data.get('utterance') or "as" in msg.data.get('utterance'):
                    self.send_post_openhab("Kuche_Jalousie1", number)
                    self.send_post_openhab("Kuche_Jalousie2", number)                    
                    self.speak_dialog("BlindsAdjust")                

            if "living room" in msg.data.get('utterance'):
                if "up" in msg.data.get('utterance') or "raise" in msg.data.get('utterance'):
                    self.send_post_openhab("WZ_Jalousien", "0")
                    self.speak_dialog("BlindsUp")
                if "down" in msg.data.get('utterance') or "lower" in msg.data.get('utterance'):
                    self.send_post_openhab("WZ_Jalousien", "100")
                    self.speak_dialog("BlindsDown")              
                elif "to" in msg.data.get('utterance'):
                    self.send_post_openhab("WZ_Jalousien", number)                
                    self.speak_dialog("BlindsAdjust")

            if "all" in msg.data.get('utterance') or "house" in msg.data.get('utterance') or "home" in msg.data.get('utterance'):
                if "up" in msg.data.get('utterance') or "raise" in msg.data.get('utterance'):
                    self.send_post_openhab("Wohnung_Jalousien", "0")
                    self.speak_dialog("BlindsUp")
                if "down" in msg.data.get('utterance') or "lower" in msg.data.get('utterance'):
                    self.send_post_openhab("Wohnung_Jalousien", "100")
                    self.speak_dialog("BlindsDown")              
                elif "to" in msg.data.get('utterance'):
                    self.send_post_openhab("Wohnung_Jalousien", number)                
                    self.speak_dialog("BlindsAdjust")     

        if "music" in msg.data.get('utterance') or "stereo" in msg.data.get('utterance') or "yamaha" in msg.data.get('utterance') or "sound system" in msg.data.get('utterance') or "radio" in msg.data.get('utterance'):                          
            if "source" in msg.data.get('utterance') or "function" in msg.data.get('utterance') or "mode" in msg.data.get('utterance'): 
                if "bluetooth" in msg.data.get('utterance'): 
                    self.send_post_openhab("RXV685Main_Zone_Zone_channels_", "Bluetooth")
                    self.speak_dialog("BlindsAdjust") 
                if "tuner" in msg.data.get('utterance') or "radio" in msg.data.get('utterance'): 
                    self.send_post_openhab("RXV685Main_Zone_Zone_channels_", "Tuner")
                    self.speak_dialog("BlindsAdjust") 
                if "auxiliar" in msg.data.get('utterance') or "aux" in msg.data.get('utterance'):   
                    self.send_post_openhab("RXV685Main_Zone_Zone_channels_", "aux")
                    self.speak_dialog("BlindsAdjust") 
                if "net radio" in msg.data.get('utterance'):   
                    self.send_post_openhab("RXV685Main_Zone_Zone_channels_", "NET RADIO")
                    self.speak_dialog("BlindsAdjust") 
                if "cd" in msg.data.get('utterance'):   
                    self.send_post_openhab("RXV685Main_Zone_Zone_channels_", "CD")
                    self.speak_dialog("BlindsAdjust") 
                if "usb" in msg.data.get('utterance'):   
                    self.send_post_openhab("RXV685Main_Zone_Zone_channels_", "USB")
                    self.speak_dialog("BlindsAdjust") 
            if "volume" in msg.data.get('utterance'): 
                    self.send_post_openhab("RXV685Main_Zone_Zone_channels_Volume", number)
                    self.speak_dialog("BlindsAdjust") 
            if "scene" in msg.data.get('utterance'): 
                    self.send_post_openhab("RXV685Main_Zone_Zone_channels_Scene", "Scene "+number)
                    self.speak_dialog("BlindsAdjust") 

    def things_onoff(self,msg):
        print (msg.data.get('utterance'))

        if "lights" in msg.data.get('utterance') or "light" in msg.data.get('utterance'):
            if "home" in msg.data.get('utterance') or "house" in msg.data.get('utterance') or "all" in msg.data.get('utterance'):     
                if "on" in msg.data.get('utterance'):          
                    self.send_post_openhab("HueBulb_Color_OnOff", "ON")
                    self.send_post_openhab("HueColorLamp1_Color_OnOff", "ON")
                    self.send_post_openhab("HueColorLamp2_Color_OnOff", "ON")
                    self.speak_dialog("LightsOn")  
                if "off" in msg.data.get('utterance'):
                    self.send_post_openhab("HueBulb_Color_OnOff", "OFF")
                    self.send_post_openhab("HueColorLamp1_Color_OnOff", "OFF")
                    self.send_post_openhab("HueColorLamp2_Color_OnOff", "OFF")          
                    self.speak_dialog("LightsOff") 
            if "kitchen" in msg.data.get('utterance'):
                if "table" in msg.data.get('utterance'):
                    if "on" in msg.data.get('utterance'):          
                        self.send_post_openhab("Kueche1_KNX_Licht_Schalten", "ON")
                        self.speak_dialog("LightsOn")  
                    if "off" in msg.data.get('utterance'):
                        self.send_post_openhab("Kueche1_KNX_Licht_Schalten", "OFF")          
                        self.speak_dialog("LightsOff")
                elif "work" in msg.data.get('utterance'):
                    if "on" in msg.data.get('utterance'):          
                        self.send_post_openhab("Kueche2_KNX_Licht_Schalten", "ON")
                        self.speak_dialog("LightsOn")  
                    if "off" in msg.data.get('utterance'):
                        self.send_post_openhab("Kueche2_KNX_Licht_Schalten", "OFF")          
                        self.speak_dialog("LightsOff")
                elif "ceiling" in msg.data.get('utterance'):
                    if "on" in msg.data.get('utterance'):          
                        self.send_post_openhab("Kueche_LichtDimmer", "100")
                        self.speak_dialog("LightsOn")  
                    if "off" in msg.data.get('utterance'):
                        self.send_post_openhab("Kueche_LichtDimmer", "0")          
                        self.speak_dialog("LightsOff")
                else:               
                    if "on" in msg.data.get('utterance'):          
                        self.send_post_openhab("HueColorLamp1_Color_OnOff", "ON")
                        self.speak_dialog("LightsOn")  
                    if "off" in msg.data.get('utterance'):
                        self.send_post_openhab("HueColorLamp1_Color_OnOff", "OFF")          
                        self.speak_dialog("LightsOff")                                 
            if "living room" in msg.data.get('utterance'):        
                if "center" in msg.data.get('utterance'):
                    if "on" in msg.data.get('utterance'):          
                        self.send_post_openhab("WZ_KNX_Licht_Schalten", "ON")
                        self.speak_dialog("LightsOn")  
                    if "off" in msg.data.get('utterance'):
                        self.send_post_openhab("WZ_KNX_Licht_Schalten", "OFF")          
                        self.speak_dialog("LightsOff")
                elif "ceiling" in msg.data.get('utterance'):   
                    if "on" in msg.data.get('utterance'):          
                        self.send_post_openhab("WZ_LichtDimmer", "100")
                        self.speak_dialog("LightsOn")  
                    if "off" in msg.data.get('utterance'):
                        self.send_post_openhab("WZ_LichtDimmer", "0")          
                        self.speak_dialog("LightsOff")  
                else:
                    if "on" in msg.data.get('utterance'):          
                        self.send_post_openhab("HueBulb_Color_OnOff", "ON")
                        self.speak_dialog("LightsOn")  
                    if "off" in msg.data.get('utterance'):
                        self.send_post_openhab("HueBulb_Color_OnOff", "OFF")          
                        self.speak_dialog("LightsOff")          
            elif "room" in msg.data.get('utterance') or "bedroom" in msg.data.get('utterance'):       
                if "on" in msg.data.get('utterance'):          
                    self.send_post_openhab("HueColorLamp2_Color_OnOff", "ON")  
                    self.speak_dialog("LightsOn")  
                if "off" in msg.data.get('utterance'):
                    self.send_post_openhab("HueColorLamp2_Color_OnOff", "OFF")         
                    self.speak_dialog("LightsOff")
                

        if "hob" in msg.data.get('utterance'):        
            if "on" in msg.data.get('utterance'):          
                self.send_post_openhab("Kueche_Platte", "ON")
                self.speak_dialog("GeneralOn")  
            if "off" in msg.data.get('utterance'):
                self.send_post_openhab("Kueche_Platte", "OFF")          
                self.speak_dialog("GeneralOff")

        if "oven" in msg.data.get('utterance'):        
            if "on" in msg.data.get('utterance'):          
                self.send_post_openhab("Kueche_Platte", "ON")
                self.speak_dialog("GeneralOn")  
            if "off" in msg.data.get('utterance'):
                self.send_post_openhab("Kueche_Platte", "OFF")          
                self.speak_dialog("GeneralOff")

        if "music" in msg.data.get('utterance') or "stereo" in msg.data.get('utterance') or "yamaha" in msg.data.get('utterance') or "sound system" in msg.data.get('utterance') or "radio" in msg.data.get('utterance'): 

            if "on" in msg.data.get('utterance'):                
                self.send_post_openhab("RXV685Main_Zone_Zone_channels_Power", "ON")
                self.speak_dialog("GeneralOn")  
            if "off" in msg.data.get('utterance'): 
                self.send_post_openhab("RXV685Main_Zone_Zone_channels_Power", "OFF")
                self.speak_dialog("GeneralOff")

    def music_control(self,msg):

        if "play" in msg.data.get('utterance'):
            self.send_post_openhab("RXV685Main_Zone_Playback_channels_PlaybackControl", "Play")
            self.speak_dialog("BlindsAdjust") 
        if "pause" in msg.data.get('utterance'): 
            self.send_post_openhab("RXV685Main_Zone_Playback_channels_PlaybackControl", "Pause")
            self.speak_dialog("BlindsAdjust") 
        if "next" in msg.data.get('utterance'):
            self.send_post_openhab("RXV685Main_Zone_Playback_channels_PlaybackControl", "Next")
            self.speak_dialog("BlindsAdjust")                               
        if "previous" in msg.data.get('utterance'):
            self.send_post_openhab("RXV685Main_Zone_Playback_channels_PlaybackControl", "Previous")
            self.speak_dialog("BlindsAdjust") 
        if "mute" in msg.data.get('utterance') or "silence" in msg.data.get('utterance'):
            if "off" in msg.data.get('utterance') or "activate" in msg.data.get('utterance'):  
                self.send_post_openhab("RXV685Main_Zone_Zone_channels_Mute", "OFF")            
                self.speak_dialog("BlindsAdjust") 
            else:  
                self.send_post_openhab("RXV685Main_Zone_Zone_channels_Mute", "OFF")            
                self.speak_dialog("BlindsAdjust")                 

    def things_controlG(self,msg):

        utterance = msg.data["utterance"]
        number = str(extract_number(utterance))

        if "licht" in msg.data.get('utterance') or "lichter" in msg.data.get('utterance') or "beleuchtung" in msg.data.get('utterance'):
            if "grün" in msg.data.get('utterance'):           
                if "küche" in msg.data.get('utterance'):
                        self.send_post_openhab("HueColorLamp1_Color_Color", "120,100,100")
                        self.speak_dialog("BlindsAdjustG")
                if "wohnzimmer" in msg.data.get('utterance'):
                        self.send_post_openhab("HueBulb_Color_Color", "120,100,100")
                        self.speak_dialog("BlindsAdjustG")
                elif "raum" in msg.data.get('utterance') or "bedroom" in msg.data.get('utterance'):                
                        self.send_post_openhab("HueColorLamp2_Color_Color", "120,100,100")
                        self.speak_dialog("BlindsAdjustG")                
            if "rot" in msg.data.get('utterance'):           
                if "küche" in msg.data.get('utterance'):
                        self.send_post_openhab("HueColorLamp1_Color_Color", "0,100,100")
                        self.speak_dialog("BlindsAdjustG")
                if "wohnzimmer" in msg.data.get('utterance'):
                        self.send_post_openhab("HueBulb_Color_Color", "0,100,100")
                        self.speak_dialog("BlindsAdjustG")
                elif "raum" in msg.data.get('utterance') or "bedroom" in msg.data.get('utterance'):                
                        self.send_post_openhab("HueColorLamp2_Color_Color", "0,100,100")
                        self.speak_dialog("BlindsAdjustG") 
            if "blau" in msg.data.get('utterance'):           
                if "küche" in msg.data.get('utterance'):
                        self.send_post_openhab("HueColorLamp1_Color_Color", "202,100,100")
                        self.speak_dialog("BlindsAdjustG")
                if "wohnzimmer" in msg.data.get('utterance'):
                        self.send_post_openhab("HueBulb_Color_Color", "202,100,100")
                        self.speak_dialog("BlindsAdjustG")
                elif "raum" in msg.data.get('utterance') or "bedroom" in msg.data.get('utterance'):                
                        self.send_post_openhab("HueColorLamp2_Color_Color", "202,100,100")
                        self.speak_dialog("BlindsAdjustG") 
            if "gelb" in msg.data.get('utterance'):           
                if "küche" in msg.data.get('utterance'):
                        self.send_post_openhab("HueColorLamp1_Color_Color", "46,99,100")
                        self.speak_dialog("BlindsAdjustG")
                if "wohnzimmer" in msg.data.get('utterance'):
                        self.send_post_openhab("HueBulb_Color_Color", "46,99,100")
                        self.speak_dialog("BlindsAdjustG")
                elif "raum" in msg.data.get('utterance') or "bedroom" in msg.data.get('utterance'):                
                        self.send_post_openhab("HueColorLamp2_Color_Color", "46,99,100")
                        self.speak_dialog("BlindsAdjustG")  
            if "orange" in msg.data.get('utterance'):           
                if "küche" in msg.data.get('utterance'):
                        self.send_post_openhab("HueColorLamp1_Color_Color", "27,100,100")
                        self.speak_dialog("BlindsAdjustG")
                if "wohnzimmer" in msg.data.get('utterance'):
                        self.send_post_openhab("HueBulb_Color_Color", "27,100,100")
                        self.speak_dialog("BlindsAdjustG")
                elif "raum" in msg.data.get('utterance') or "bedroom" in msg.data.get('utterance'):                
                        self.send_post_openhab("HueColorLamp2_Color_Color", "27,100,100")
                        self.speak_dialog("BlindsAdjustG") 
            if "pink" in msg.data.get('utterance') or "rosa" in msg.data.get('utterance'):           
                if "küche" in msg.data.get('utterance'):
                        self.send_post_openhab("HueColorLamp1_Color_Color", "326,100,100")
                        self.speak_dialog("BlindsAdjustG")
                if "wohnzimmer" in msg.data.get('utterance'):
                        self.send_post_openhab("HueBulb_Color_Color", "326,100,100")
                        self.speak_dialog("BlindsAdjustG")
                elif "raum" in msg.data.get('utterance') or "bedroom" in msg.data.get('utterance'):                
                        self.send_post_openhab("HueColorLamp2_Color_Color", "326,100,100")
                        self.speak_dialog("BlindsAdjustG")                             
            if "violett" in msg.data.get('utterance') or "lila" in msg.data.get('utterance'):           
                if "küche" in msg.data.get('utterance'):
                        self.send_post_openhab("HueColorLamp1_Color_Color", "263,78,100")
                        self.speak_dialog("BlindsAdjustG")
                if "wohnzimmer" in msg.data.get('utterance'):
                        self.send_post_openhab("HueBulb_Color_Color", "263,78,100")
                        self.speak_dialog("BlindsAdjustG")
                elif "raum" in msg.data.get('utterance') or "bedroom" in msg.data.get('utterance'):                
                        self.send_post_openhab("HueColorLamp2_Color_Color", "263,78,100")
                        self.speak_dialog("BlindsAdjustG")      
            if "weiß" in msg.data.get('utterance'):           
                if "küche" in msg.data.get('utterance'):
                        self.send_post_openhab("HueColorLamp1_Color_Color", "191,1,100")
                        self.speak_dialog("BlindsAdjustG")
                if "wohnzimmer" in msg.data.get('utterance'):
                        self.send_post_openhab("HueBulb_Color_Color", "191,1,100")
                        self.speak_dialog("BlindsAdjustG")
                elif "raum" in msg.data.get('utterance') or "bedroom" in msg.data.get('utterance'):                
                        self.send_post_openhab("HueColorLamp2_Color_Color", "191,1,100")
                        self.speak_dialog("BlindsAdjustG")                                          
            else: #si el número es distinto de null
                if "küche" in msg.data.get('utterance'):
                        self.send_post_openhab("HueColorLamp1_Color_Dimmer", number)
                        self.speak_dialog("BlindsAdjustG")
                if "wohnzimmer" in msg.data.get('utterance'):
                        self.send_post_openhab("HueBulb_Color_Dimmer", number)
                        self.speak_dialog("BlindsAdjustG")
                elif "raum" in msg.data.get('utterance') or "bedroom" in msg.data.get('utterance'):                
                        self.send_post_openhab("HueColorLamp2_Color_Dimmer", number)
                        self.speak_dialog("BlindsAdjustG")

        if "jalousie" in msg.data.get('utterance') or "rollo" in msg.data.get('utterance') or "blende" in msg.data.get('utterance') or "vorhang" in msg.data.get('utterance'):
            if "küche" in msg.data.get('utterance'):
                if "hochziehen" in msg.data.get('utterance') or "hochfahren" in msg.data.get('utterance') :
                    self.send_post_openhab("Kuche_Jalousie1", "0")
                    self.send_post_openhab("Kuche_Jalousie2", "0")
                    self.speak_dialog("BlindsUpG")
                if "herunterziehen" in msg.data.get('utterance'):
                    self.send_post_openhab("Kuche_Jalousie1", "100")
                    self.send_post_openhab("Kuche_Jalousie2", "100")
                    self.speak_dialog("BlindsDownG")              
                elif "auf" in msg.data.get('utterance'):
                    self.send_post_openhab("Kuche_Jalousie1", number)
                    self.send_post_openhab("Kuche_Jalousie2", number)                    
                    self.speak_dialog("BlindsAdjustG")                

            if "wohnzimmer" in msg.data.get('utterance'):
                if "hochziehen" in msg.data.get('utterance') or "hochfahren" in msg.data.get('utterance') :
                    self.send_post_openhab("WZ_Jalousien", "0")
                    self.speak_dialog("BlindsUpG")
                if "herunterziehen" in msg.data.get('utterance'):
                    self.send_post_openhab("WZ_Jalousien", "100")
                    self.speak_dialog("BlindsDownG")              
                elif "auf" in msg.data.get('utterance'):
                    self.send_post_openhab("WZ_Jalousien", number)                
                    self.speak_dialog("BlindsAdjustG")

            if "alle" in msg.data.get('utterance'):
                if "hochziehen" in msg.data.get('utterance') or "hochfahren" in msg.data.get('utterance') :
                    self.send_post_openhab("Wohnung_Jalousien", "0")
                    self.speak_dialog("BlindsUpG")
                if "herunterziehen" in msg.data.get('utterance'):
                    self.send_post_openhab("Wohnung_Jalousien", "100")
                    self.speak_dialog("BlindsDownG")              
                elif "auf" in msg.data.get('utterance'):
                    self.send_post_openhab("Wohnung_Jalousien", number)                
                    self.speak_dialog("BlindsAdjustG")     

        if "musik" in msg.data.get('utterance') or "Stereoanlage" in msg.data.get('utterance') or "yamaha" in msg.data.get('utterance')or "soundsystem" in msg.data.get('utterance'):                          
            if "quelle" in msg.data.get('utterance') or "funktion" in msg.data.get('utterance'): 
                if "bluetooth" in msg.data.get('utterance'): 
                    self.send_post_openhab("RXV685Main_Zone_Zone_channels_", "Bluetooth")
                    self.speak_dialog("BlindsAdjustG") 
                if "tuner" in msg.data.get('utterance') or "radio" in msg.data.get('utterance'): 
                    self.send_post_openhab("RXV685Main_Zone_Zone_channels_", "Tuner")
                    self.speak_dialog("BlindsAdjustG") 
                if "auxiliar" in msg.data.get('utterance') or "aux" in msg.data.get('utterance')  or "hilfsfunktion" in msg.data.get('utterance'):   
                    self.send_post_openhab("RXV685Main_Zone_Zone_channels_", "aux")
                    self.speak_dialog("BlindsAdjustG") 
                if "net radio" in msg.data.get('utterance'):   
                    self.send_post_openhab("RXV685Main_Zone_Zone_channels_", "NET RADIO")
                    self.speak_dialog("BlindsAdjustG") 
            if "volume" in msg.data.get('utterance') or "lautstärke " in msg.data.get('utterance') or "umfang " in msg.data.get('utterance'): 
                    self.send_post_openhab("RXV685Main_Zone_Zone_channels_Volume", number)
                    self.speak_dialog("BlindsAdjustG") 
            if "szene" in msg.data.get('utterance'):
                    self.send_post_openhab("RXV685Main_Zone_Zone_channels_Scene", "Scene "+number)
                    self.speak_dialog("BlindsAdjustG") 

    def things_onoffG(self,msg):

        if "licht" in msg.data.get('utterance') or "lichter" in msg.data.get('utterance') or "beleuchtung" in msg.data.get('utterance'):
            if "haus" in msg.data.get('utterance') or "alle" in msg.data.get('utterance'):     
                if "einschalten" in msg.data.get('utterance') or "anschalten" in msg.data.get('utterance') or "ein" in msg.data.get('utterance'):          
                    self.send_post_openhab("HueBulb_Color_OnOff", "ON")
                    self.send_post_openhab("HueColorLamp1_Color_OnOff", "ON")
                    self.send_post_openhab("HueColorLamp2_Color_OnOff", "ON")
                    self.speak_dialog("LightsOnG")  
                if "machen" in msg.data.get('utterance') or "ausschalten" in msg.data.get('utterance') or "aus" in msg.data.get('utterance'):
                    self.send_post_openhab("HueBulb_Color_OnOff", "OFF")
                    self.send_post_openhab("HueColorLamp1_Color_OnOff", "OFF")
                    self.send_post_openhab("HueColorLamp2_Color_OnOff", "OFF")          
                    self.speak_dialog("LightsOffG") 
            if "küche" in msg.data.get('utterance'):
                if "tisch" in msg.data.get('utterance'):
                    if "einschalten" in msg.data.get('utterance') or "anschalten" in msg.data.get('utterance') or "ein" in msg.data.get('utterance'):          
                        self.send_post_openhab("Kueche1_KNX_Licht_Schalten", "ON")
                        self.speak_dialog("LightsOnG")  
                    if "machen" in msg.data.get('utterance') or "ausschalten" in msg.data.get('utterance') or "aus" in msg.data.get('utterance'):
                        self.send_post_openhab("Kueche1_KNX_Licht_Schalten", "OFF")          
                        self.speak_dialog("LightsOffG")
                elif "arbeit" in msg.data.get('utterance'):
                    if "einschalten" in msg.data.get('utterance') or "anschalten" in msg.data.get('utterance') or "ein" in msg.data.get('utterance'):          
                        self.send_post_openhab("Kueche2_KNX_Licht_Schalten", "ON")
                        self.speak_dialog("LightsOnG")  
                    if "machen" in msg.data.get('utterance') or "ausschalten" in msg.data.get('utterance') or "aus" in msg.data.get('utterance'):
                        self.send_post_openhab("Kueche2_KNX_Licht_Schalten", "OFF")          
                        self.speak_dialog("LightsOffG")
                elif "decken" in msg.data.get('utterance'):
                    if "einschalten" in msg.data.get('utterance') or "anschalten" in msg.data.get('utterance') or "ein" in msg.data.get('utterance'):          
                        self.send_post_openhab("Kueche_LichtDimmer", "100")
                        self.speak_dialog("LightsOnG")  
                    if "machen" in msg.data.get('utterance') or "ausschalten" in msg.data.get('utterance') or "aus" in msg.data.get('utterance'):
                        self.send_post_openhab("Kueche_LichtDimmer", "0")          
                        self.speak_dialog("LightsOffG")
                else:               
                    if "einschalten" in msg.data.get('utterance') or "anschalten" in msg.data.get('utterance') or "ein" in msg.data.get('utterance'):         
                        self.send_post_openhab("HueColorLamp1_Color_OnOff", "ON")
                        self.speak_dialog("LightsOnG")  
                    if "machen" in msg.data.get('utterance') or "ausschalten" in msg.data.get('utterance') or "aus" in msg.data.get('utterance'):
                        self.send_post_openhab("HueColorLamp1_Color_OnOff", "OFF")          
                        self.speak_dialog("LightsOffG")                                 
            if "wohnzimmer" in msg.data.get('utterance'):        
                if "mitte" in msg.data.get('utterance'):
                    if "einschalten" in msg.data.get('utterance') or "anschalten" in msg.data.get('utterance') or "ein" in msg.data.get('utterance'):         
                        self.send_post_openhab("WZ_KNX_Licht_Schalten", "ON")
                        self.speak_dialog("LightsOnG")  
                    if "machen" in msg.data.get('utterance') or "ausschalten" in msg.data.get('utterance') or "aus" in msg.data.get('utterance'):
                        self.send_post_openhab("WZ_KNX_Licht_Schalten", "OFF")          
                        self.speak_dialog("LightsOffG")
                elif "ceiling" in msg.data.get('utterance'):   
                    if "einschalten" in msg.data.get('utterance') or "anschalten" in msg.data.get('utterance') or "ein" in msg.data.get('utterance'):          
                        self.send_post_openhab("WZ_LichtDimmer", "100")
                        self.speak_dialog("LightsOnG")  
                    if "machen" in msg.data.get('utterance') or "ausschalten" in msg.data.get('utterance') or "aus" in msg.data.get('utterance'):
                        self.send_post_openhab("WZ_LichtDimmer", "0")          
                        self.speak_dialog("LightsOffG")  
                else:
                    if "einschalten" in msg.data.get('utterance') or "anschalten" in msg.data.get('utterance') or "ein" in msg.data.get('utterance'):          
                        self.send_post_openhab("HueBulb_Color_OnOff", "ON")
                        self.speak_dialog("LightsOnG")  
                    if "machen" in msg.data.get('utterance') or "ausschalten" in msg.data.get('utterance') or "aus" in msg.data.get('utterance'):
                        self.send_post_openhab("HueBulb_Color_OnOff", "OFF")          
                        self.speak_dialog("LightsOffG")          
            elif "raum" in msg.data.get('utterance') or "bedroom" in msg.data.get('utterance'):       
                if "einschalten" in msg.data.get('utterance') or "anschalten" in msg.data.get('utterance') or "ein" in msg.data.get('utterance'):          
                    self.send_post_openhab("HueColorLamp2_Color_OnOff", "ON")  
                    self.speak_dialog("LightsOnG")  
                if "machen" in msg.data.get('utterance') or "ausschalten" in msg.data.get('utterance') or "aus" in msg.data.get('utterance'):
                    self.send_post_openhab("HueColorLamp2_Color_OnOff", "OFF")         
                    self.speak_dialog("LightsOffG")
                

        if "kochfeld" in msg.data.get('utterance'):        
            if "einschalten" in msg.data.get('utterance') or "anschalten" in msg.data.get('utterance') or "ein" in msg.data.get('utterance'):          
                self.send_post_openhab("Kueche_Platte", "ON")
                self.speak_dialog("GeneralOnG")  
            if "machen" in msg.data.get('utterance') or "ausschalten" in msg.data.get('utterance') or "aus" in msg.data.get('utterance'):
                self.send_post_openhab("Kueche_Platte", "OFF")          
                self.speak_dialog("GeneralOffG")

        if "musik" in msg.data.get('utterance') or "stereoanlage" in msg.data.get('utterance') or "yamaha" in msg.data.get('utterance') or "sound system" in msg.data.get('utterance'):
            if "einschalten" in msg.data.get('utterance') or "anschalten" in msg.data.get('utterance') or "ein" in msg.data.get('utterance'):                
                self.send_post_openhab("RXV685Main_Zone_Zone_channels_Power", "ON")
                self.speak_dialog("GeneralOnG")  
            if "machen" in msg.data.get('utterance') or "ausschalten" in msg.data.get('utterance'): 
                self.send_post_openhab("RXV685Main_Zone_Zone_channels_Power", "OFF")
                self.speak_dialog("GeneralOffG")

    def music_controlG(self,msg):

        if "spielen" in msg.data.get('utterance'):
            self.send_post_openhab("RXV685Main_Zone_Playback_channels_PlaybackControl", "Play")
            self.speak_dialog("BlindsAdjustG") 
        if "pausieren" in msg.data.get('utterance'): 
            self.send_post_openhab("RXV685Main_Zone_Playback_channels_PlaybackControl", "Pause")
            self.speak_dialog("BlindsAdjustG") 
        if "nächstes" in msg.data.get('utterance'):
            self.send_post_openhab("RXV685Main_Zone_Playback_channels_PlaybackControl", "Next")
            self.speak_dialog("BlindsAdjustG")                               
        if "vorheriges" in msg.data.get('utterance'):
            self.send_post_openhab("RXV685Main_Zone_Playback_channels_PlaybackControl", "Previous")
            self.speak_dialog("BlindsAdjustG") 
        if "schweigen" in msg.data.get('utterance'):  
            self.send_post_openhab("RXV685Main_Zone_Zone_channels_Mute", "ON")            
            self.speak_dialog("BlindsAdjustG") 
        if "aktiviert" in msg.data.get('utterance'):  
            self.send_post_openhab("RXV685Main_Zone_Zone_channels_Mute", "OFF")            
            self.speak_dialog("BlindsAdjustG")                 


    def stop(self):
        pass


def create_skill():
    return ControlHouseSkill()
