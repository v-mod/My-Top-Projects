import os
def install():
    modules=['playsound','piwheels','portaudio','threading','wikipedia','wolfram-alpha','datetime','PyAudio','speechrecognition','wheel','json','requests','pyjokes','flask']
    for module in modules:
        os.system('sudo pip3 install '+module)
    print('Installation Complete')
    