import re
import os
import shutil
import data_scripts


test_location = "/Users/adria/Desktop/SpeechToASL/data/test-clean/"
valid_location = "/Users/adria/Desktop/SpeechToASL/data/dev-clean/"
train_location = "/Users/adria/Desktop/SpeechToASL/data/train-clean-100/"

# test_audio_info  = data_scripts.get_directory_info(test_location)
# valid_audio_info = data_scripts.get_directory_info(valid_location)
print('getting audio info')
train_audio_info = data_scripts.get_directory_info(train_location)

print('obtained audio info')
