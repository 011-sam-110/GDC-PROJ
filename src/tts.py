
import json
import os
import re
import time
from datetime import datetime

import simpleaudio as sa
import vlc
from colorama import Fore, Style, init
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

#cedar
def speakText(text_to_speak):
    if type(text_to_speak) == str:
        
        
        client = OpenAI()  # The client now picks up the key from the environment
        speech_file_path = "speech.wav"

    
        with client.audio.speech.with_streaming_response.create(
            model="gpt-4o-mini-tts",
            voice="cedar",
            input=text_to_speak,
            instructions="Speak in a helpful tone"
        ) as response:
            response.stream_to_file(speech_file_path)
    
        player = vlc.MediaPlayer(str(speech_file_path))
        player.play()
        while player.get_state() != vlc.State.Ended:
            time.sleep(0.1)
