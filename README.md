# Control of IoT devices using an openHAB server controlled by Mycroft as a voice assistant

Skill created manually based on sending POST requests from the Mycroft Voice Assistant (OpenSource) to an openHAB server. This particular code includes the control of different devices such as blinds, lights (like Google Hue), a music device and some extra devices but is easily configurable according to the infrastructure of each following the basic structure of the skill.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

In relation to the voice assistant part, different options are allowed for its implementation. In the official Mycroft documentation (https://mycroft.ai/get-started/) you can see five different ways to integrate this part of the system. The tests carried out in this case were based on the installation of Picroft's system on a Raspberry Pi 3+ as we only needed to integrate the voice assistant into the Raspberry as the server part would be separated into another device specially dedicated for this purpose.

The openHAB server part can be installed on different devices, from an own dedicated server to a computer in the voice assistant network environment, in the same way it can be based on different Java platforms (Zulu, Oracle Java, OpenJDK). In this case it has been tested with both possibilities. In both cases it should be noted that to be able to use either of the two forms the corresponding device must be able to be switched on all the time and must be able to connect to the WiFi network.

The system can be installed in most of the available operating systems but you have to take into account that in each of them you have to follow a different installation process as indicated in the official documentation (https://www.openhab.org/docs/installation/)

As an additional comment, there is a predefined Skill for the use of Mycroft's Voice Assistant with the openHAB server (https://www.openhab.org/docs/ecosystem/mycroft/), however it has not been used in this case because it limits the system's possibilities. A clear example is that it does not allow you to change the color of the lights and limits the variability of possible commands for the user to perform a certain command.


### Installing

A step by step series of examples that tell you how to get a development env running

After the installation and the corresponding start of both the server and the voice assistant following the instructions in the official documentation of each one of them, both must be configured in the same WiFi network.

The next step in this case is to obtain the IP address of the server, which can be easily obtained by writing the ifconfig (Linux) or ipconfig (Windows) command in a terminal of the device where the server is located. Other common alternatives can be considered depending on the O.S. of the device. After obtaining this address, the IP address should be changed in the __init__.py file in line of code 45 to the one obtained in this case, this will allow the commands collected by the Mycroft system to be sent directly to the openHAB server for execution.


This is where, depending on the previous configuration of the openHAB server according to the devices you have, you will have to set up the POST requests according to the names you have configured the different IoT elements of your network with. In order to make this task easier, it is recommended to look for the following URL in a browser: http://server_ip:8080/rest/items/ and be able to see the exact name of each one of the devices configured in the server so that you can later replace them in the Python code.

On the other hand, in the vocab folder you will find the key words to execute a certain set of commands depending on the language you want to work with. It is possible to edit them if you want to add or remove some, but it is not recommended to make many changes here.

Something similar happens with the dialog folder, here you can find the different possible answers available in the system depending on the different commands sent by the user, they are gathered in different groups that can be easily configured depending on the type of answers that the user prefers in each case.

The next step would be to copy the entire folder (mycroft_openhab_skill) to the Mycroft skills folder, in case you use the Picroft option it is located in /home/pi/mycroft-core/skills. The final step would be to reboot the entire Mycroft system so that all the skills are reloaded, you could also reboot only the skills part but it sometimes gives problems (use mycroft's own system commands to make it easier).

To make this task easier and to facilitate the configuration of the code, we recommend the option of editing the code on a computer using some editor (VisualStudio) and then copying the whole folder to the Mycroft system using the Windows scp command or the equivalent on each operating system. Editing code on Picroft's own system is more tedious.


All this basic configuration serves to make the skill work in English, just like the rest of the system, since this is the initial basic configuration of Mycroft.

The skill is also prepared to work in German, if you want to use it in this language you must initially configure the system to work in German
```
mycroft-config set lang "de-de"
```

And change the mycroft.conf (something similar to this)

```
mycroft-config edit user
```
```
{
 "lang": "de-de",
 "ipc_path": "/ramdisk/mycroft/ipc/",

 "stt": {
   "module": "mycroft",
   "mycroft": {
     "lang": "de-de"
   }
 },
 "tts": {
   "module": "google",
   "google": {
     "lang": "de"
   }
 },
 "play_wav_cmdline": "aplay -Dhw:0,0 %1",
 "play_mp3_cmdline": "mpg123 -a hw:0,0 %1",
 "enclosure": {
    "platform": "picroft"
 },
 "max_allowed_core_version": 20.3,
 "skills": {
   "auto_update": true
 }
}
```
It should be noted that the basic system is based on the use of English, if you use another language is necessary to resort to other services of other companies to complement the system of Mycroft (following the configuration indicated is used to the services Text To Speech of Google)

## Commands examples

There are avaliable different options to execute the same order (more variability so more natural).

```
(Turn/Switch) (on/off) the (kitchen/living room/bedroom) lights
(Adjust/Regulate/..) (kitchen/living room/bedroom) lights to ("color")
(Adjust/Regulate/..) (kitchen/living room/bedroom) lights to ("number") percent
(Raise/Lower/Roll up...) (kitchen/living room/bedroom) blinds
(Adjust/Regulate/..) (kitchen/living room/bedroom) blinds to ("number") percent
(Turn/Switch) (on/off) the (oven/hob/stereo)
(Play/Pause/Next/Previous/Mute) (Music/Song)

```

Similar commands also avaliable in German.

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

