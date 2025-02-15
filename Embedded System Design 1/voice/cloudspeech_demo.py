#!/usr/bin/env python3
# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""A demo of the Google CloudSpeech recognizer."""
import argparse
import locale
import logging
import aiy.voice.tts

from aiy.board import Board, Led
from aiy.cloudspeech import CloudSpeechClient
from twilio.rest import Client
from picamera import PiCamera
from time import sleep

# Your Account SID from twilio.com/console
account_sid = "AC3f402d05037b7a02e003d21ef1360475"
# Your Auth Token from twilio.com/console
auth_token  = "29193e70744daa1983fd175df4f8fb24"
client1 = Client(account_sid, auth_token)
camera = PiCamera()

def get_hints(language_code):
    if language_code.startswith('en_'):
        return ('turn on the light',
                'turn off the light',
                'blink the light',
                'goodbye',
                'repeat after me')
    
    return None

def locale_language():
    language, _ = locale.getdefaultlocale()
    return language

def main():
    logging.basicConfig(level=logging.DEBUG)

    parser = argparse.ArgumentParser(description='Assistant service example.')
    parser.add_argument('--language', default=locale_language())
    args = parser.parse_args()

    logging.info('Initializing for language %s...', args.language)
    hints = get_hints(args.language)
    client = CloudSpeechClient()
    with Board() as board:
        while True:
            if hints:
                logging.info('Say something, e.g. %s.' % ', '.join(hints))
            else:
                logging.info('Say something.')
            text = client.recognize(language_code=args.language,
                                    hint_phrases=hints)
            if text is None:
                logging.info('You said nothing.')
                continue

            logging.info('You said: "%s"' % text)
            text = text.lower()
            if 'turn on the light' in text:
                board.led.state = Led.ON
            elif 'turn off the light' in text:
                board.led.state = Led.OFF
            elif 'hello' in text:
                message = client1.messages.create(
                              to="+19542491226",
                              from_="+19549459294",
                              body="Hello, Someone is at your door. Click Link 10.12.126.178")
                print(message.sid)
                camera.start_preview()
                sleep(5)
                camera.capture('/var/www/html/image.jpg')
                camera.stop_preview()
            if 'repeat after me' in text:
                # Remove "repeat after me" from the text to be repeated
                to_repeat = text.replace('repeat after me', '', 1)
                aiy.voice.tts.say(to_repeat)    
            elif 'goodbye' in text:
                break

if __name__ == '__main__':
    main()
