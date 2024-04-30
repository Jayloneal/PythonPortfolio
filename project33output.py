from win11toast import toast, notify, update_progress, toast_async
from time import sleep

#toast("What's up, my guy? Just lettin' you know that I'm here! If you need anything, let me know!")

# If you want to include a URL
#toast('Ayo, my boy! Look at this right hea, dawg! This had me dying', 'Click to open url', on_click='https://www.tiktok.com/@yatzelxd/video/7237218437355932974')

# If you want to type a random message out.
#toast('What's up, my guy!', 'Just wanted to remind you that, you have to have fun while coding!')

# If you want to run Python script
#toast('What's up, my guy!', 'Click to run python script', on_click=r'D:\Python\project33output.py')

# If you want to see if someone clicked the notification
#toast("What's up, my guy?", 'Click to open url', on_click=lambda args: print("It's been clicked!", args))

#If you want to send a notification with a circular icon attached to it
#toast('You have been sent to Slytherin House!', 'Sincerely, Python', icon='D:/Python/sortinghat.ico')

# If you want to make the icon look like a square
#icon = {
    #'src': 'D:/Python/draco.ico',
    #'placement': 'appLogoOverride'
#}
#toast('Message from Draco Malfoy', 'Hi there! My name is Draco.', icon=icon)

#If you want to include an image in the notification
#toast('Mascot of Slytherin', 'Slytherin, the house of ambition', image='D:/Python/snake.jpg')

# If you want to add text to your image i.e., create a hero image.
#image = {
    #'src': 'D:/Python/snake.jpg',
    #'placement': 'hero'    
#}
#toast('Mascot of Slytherin', 'The House of Ambition', image=image)

#If you want to create a loading screen
#notify(progress={ 
    #'title': 'YouTube',
    #'status': 'Downloading...', 
    #'value': '0',
    #'valueStringOverride': '0/20 videos'
#})

#for i in range(1, 15+1):
    #sleep(1)
    #update_progress({'value': i/15, 'valueStringOverride': f'{i}/15 videos'})

#update_progress({'status': 'Completed!'})

# If you want to use audio from Microsoft Windows
#toast('Message from Ya Dawg', 'Wassup, my dawg?', audio='ms-winsoundevent:Notification.Looping.Alarm')

# If you would like to use your own audio from a URL link
#toast('Message from Paul', 'What is up, my brotha? Life going good?', audio='https://samplelib.com/lib/preview/mp3/sample-9s.mp3')

#If you want to use a music file from your own computer or electronic device
#toast('Message from Busta Rhymes', 'Yessir! Let me be the first to say that I got you in check!', audio=r'D:\Python\Got You All In Check.mp3')

#If you want to loop the audio that you sent. The audio after this line of code: ms-winsoundevent:Notification.'Looping'.Alarm will loop.
#toast('Music Playback', 'The song will now loop.', audio={'loop': 'true'})

#toast('Hello', 'Hello from Python', audio={'src': 'ms-winsoundevent:Notification.Looping.Alarm', 'loop': 'true'})

#If you want to silence the audio
#toast('This is how you would do it!', audio={'silent': 'true'})

#If you want to hear the dialogue
#toast('Audio message!', dialogue='Hi there!')

#If you want to send a message with OCR
#toast(ocr='https://i.kym-cdn.com/entries/icons/facebook/000/017/414/sampletext.jpg')

# More OCR
#toast(ocr={'lang': 'ja', 'ocr': r'D:\Python\Get Money.jpg'})

#If you want to extend the timeout on a message
#toast('Do this!', duration='long')

#If you don't want the notification to disappear
#toast('Use this!', scenario='incomingCall')

#If you want to add a button to your notification
#toast('Message from a close friend', 'Hi there!', button='Go Away!')

#If you want to access 'YouTube' by hitting this button
#toast('YouTube', 'Press the button to go to YouTube', button={'activationType': 'protocol', 'arguments': 'https://www.youtube.com', 'content': 'Open YouTube'})

# If you wanted to add multiple buttons
#toast('Hi there!', 'Click a button', buttons=['Answer', 'Deny', 'Ignore'])

# If you want to play music or open File Explorer
#buttons = [
    #{'activationType': 'protocol', 'arguments': 'D:\Python\Got You All In Check.mp3', 'content': 'Play'},
    #{'activationType': 'protocol', 'arguments': 'D:\Python', 'content': 'Open Folder'}
#]

#toast('Music Player', 'Download Finished', buttons=buttons)

# If you want to send a message using the 'Send' button
#toast('Hi there!', 'Type something!', input='reply', button='Send')

# If you want to change the input field to something else, have the 'Send' button minimized and directed to the lower - right corner and have the dialog box look sleek
#toast('Hi there!', 'Type something!', input='reply', button={'activationType': 'protocol', 'arguments': 'http:', 'content': 'Send', 'hint-inputId': 'reply'})

# If you want to make a selection
#toast('Hi there! I have a question.', 'Do you like me?', selection=['Yes','No'], button='Submit')

# If you don't want anything in the notification
#toast()

#If you want non-blocking
#notify('Hi there! I heard you like this song!', 'Click to open url', on_click='https://www.youtube.com/watch?v=izGwDsrQ1eQ&ab_channel=georgemichaelVEVO')

#If you want to have asynchronous functionality
#async def main():
    #await toast_async('This is my favorite song!', 'Click to open url', on_click='https://www.youtube.com/watch?v=2g5Hz17C4is&ab_channel=TimelessSound')

#If you want to add Jupyter functionality to it
#notify('', '', on_click='https://www.youtube.com/watch?v=2g5Hz17C4is&ab_channel=TimelessSound')

#If you want to debug the code
#First of all, you have to download 'Notifications Visualizer' so that you can use the xml code.
# Once you've done that, you can change and modify the values to your liking.
# This is what I have done.

xml = """
<toast launch="action=openThread&amp;threadId=92187">

    <visual>
        <binding template="ToastGeneric">
            <text hint-maxLines="1">Jayloneal</text>
            <text>I honestly wish I could've went to this! I feel as though I would've enjoyed myself, dawg!</text>
            <image placement="appLogoOverride" hint-crop="circle" src="https://pbs.twimg.com/profile_images/1515181166990704641/NfAdvV-t_400x400.jpg"/>
            <image placement="hero" src="https://pbs.twimg.com/media/FYjpvOdWYAcoHVo.jpg:large"/>
        </binding>
    </visual>

    <actions>

        <input id="textBox" type="text" placeHolderContent="reply"/>

        <action
          content="Send"
          imageUri="Assets/Icons/send.png"
          hint-inputId="textBox"
          activationType="background"
          arguments="action=reply&amp;threadId=92187"/>

    </actions>

</toast>"""

toast(xml=xml)
