"""
import os
import time
import pygame
from gtts import gTTS
import streamlit as st
import speech_recognition as sr
from googletrans import LANGUAGES, Translator

isTranslateOn = False

translator = Translator() # Initialize the translator module.
pygame.mixer.init()  # Initialize the mixer module.

# Create a mapping between language names and language codes
language_mapping = {name: code for code, name in LANGUAGES.items()}

def get_language_code(language_name):
    return language_mapping.get(language_name, language_name)

def translator_function(spoken_text, from_language, to_language):
    return translator.translate(spoken_text, src='{}'.format(from_language), dest='{}'.format(to_language))

def text_to_voice(text_data, to_language):
    myobj = gTTS(text=text_data, lang='{}'.format(to_language), slow=False)
    myobj.save("cache_file.mp3")
    audio = pygame.mixer.Sound("cache_file.mp3")  # Load a sound.
    audio.play()
    os.remove("cache_file.mp3")

def main_process(output_placeholder, from_language, to_language):
    
    global isTranslateOn
    
    while isTranslateOn:

        rec = sr.Recognizer()
        with sr.Microphone() as source:
            output_placeholder.text("Listening...")
            rec.pause_threshold = 1
            audio = rec.listen(source, phrase_time_limit=10)
        
        try:
            output_placeholder.text("Processing...")
            spoken_text = rec.recognize_google(audio, language='{}'.format(from_language))
            
            output_placeholder.text("Translating...")
            translated_text = translator_function(spoken_text, from_language, to_language)

            text_to_voice(translated_text.text, to_language)
    
        except Exception as e:
            print(e)

# UI layout
st.title("Language Translator")

# Dropdowns for selecting languages
from_language_name = st.selectbox("Select Source Language:", list(LANGUAGES.values()))
to_language_name = st.selectbox("Select Target Language:", list(LANGUAGES.values()))

# Convert language names to language codes
from_language = get_language_code(from_language_name)
to_language = get_language_code(to_language_name)

# Button to trigger translation
start_button = st.button("Start")
stop_button = st.button("Stop")

# Check if "Start" button is clicked
if start_button:
    if not isTranslateOn:
        isTranslateOn = True
        output_placeholder = st.empty()
        main_process(output_placeholder, from_language, to_language)

# Check if "Stop" button is clicked
if stop_button:
    isTranslateOn = False


$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

import os
import time
import pygame
from gtts import gTTS
import streamlit as st
import speech_recognition as sr
from googletrans import LANGUAGES, Translator

isTranslateOn = False

translator = Translator()  # Initialize the translator module.
pygame.mixer.init()  # Initialize the mixer module.

# Create a mapping between language names and language codes
language_mapping = {name: code for code, name in LANGUAGES.items()}

def get_language_code(language_name):
    return language_mapping.get(language_name, language_name)

def translator_function(spoken_text, from_language, to_language):
    return translator.translate(spoken_text, src='{}'.format(from_language), dest='{}'.format(to_language))

def text_to_voice(text_data, to_language):
    myobj = gTTS(text=text_data, lang='{}'.format(to_language), slow=False)
    myobj.save("cache_file.mp3")
    audio = pygame.mixer.Sound("cache_file.mp3")  # Load a sound.
    audio.play()
    os.remove("cache_file.mp3")

def main_process(output_placeholder, progress_bar, from_language, to_language):
    global isTranslateOn
    
    while isTranslateOn:
        rec = sr.Recognizer()
        with sr.Microphone() as source:
            output_placeholder.text("🎤 Listening...")
            rec.pause_threshold = 1
            audio = rec.listen(source, phrase_time_limit=10)
        
        try:
            output_placeholder.text("🌀 Processing...")
            spoken_text = rec.recognize_google(audio, language='{}'.format(from_language))
            
            output_placeholder.text("🌍 Translating...")
            progress_bar.progress(50)  # Simulate translation progress
            translated_text = translator_function(spoken_text, from_language, to_language)
            
            progress_bar.progress(100)
            text_to_voice(translated_text.text, to_language)
            time.sleep(1)
            progress_bar.empty()  # Clear progress bar after completion

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
            break

# UI layout
st.title("🌐 Real-Time Language Translator")
st.markdown("**Experience seamless translation with speech recognition and text-to-voice synthesis.**")

# UI customization for a more modern feel
with st.expander("🔧 Choose your translation settings", expanded=True):
    # Using columns for better layout
    col1, col2 = st.columns(2)
    
    with col1:
        from_language_name = st.selectbox("🎙️ Select Source Language", list(LANGUAGES.values()))
    
    with col2:
        to_language_name = st.selectbox("🗣️ Select Target Language", list(LANGUAGES.values()))

# Convert language names to language codes
from_language = get_language_code(from_language_name)
to_language = get_language_code(to_language_name)

# Adding buttons in a more streamlined layout
col_start, col_stop = st.columns(2)
start_button = col_start.button("▶️ Start Translation", use_container_width=True)
stop_button = col_stop.button("⏹️ Stop Translation", use_container_width=True)

# Placeholder for translation output and progress bar
output_placeholder = st.empty()
progress_bar = st.progress(0)

# Check if "Start" button is clicked
if start_button:
    if not isTranslateOn:
        isTranslateOn = True
        output_placeholder.success("Translator is active! 🟢")
        main_process(output_placeholder, progress_bar, from_language, to_language)

# Check if "Stop" button is clicked
if stop_button:
    isTranslateOn = False
    output_placeholder.warning("Translator has been stopped! 🛑")
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


import os
import time
import pygame
from gtts import gTTS
import streamlit as st
import speech_recognition as sr
from googletrans import LANGUAGES, Translator

isTranslateOn = False

translator = Translator()  # Initialize the translator module.
pygame.mixer.init()  # Initialize the mixer module.

# Create a mapping between language names and language codes
language_mapping = {name: code for code, name in LANGUAGES.items()}

def get_language_code(language_name):
    return language_mapping.get(language_name, language_name)

def translator_function(spoken_text, from_language, to_language):
    return translator.translate(spoken_text, src='{}'.format(from_language), dest='{}'.format(to_language))

def text_to_voice(text_data, to_language):
    myobj = gTTS(text=text_data, lang='{}'.format(to_language), slow=False)
    myobj.save("cache_file.mp3")
    audio = pygame.mixer.Sound("cache_file.mp3")  # Load a sound.
    audio.play()
    os.remove("cache_file.mp3")

def main_process(output_placeholder, source_caption, target_caption, progress_bar, from_language, to_language):
    global isTranslateOn
    
    while isTranslateOn:
        rec = sr.Recognizer()
        with sr.Microphone() as source:
            output_placeholder.text("🎤 Listening...")
            rec.pause_threshold = 1
            audio = rec.listen(source, phrase_time_limit=10)
        
        try:
            output_placeholder.text("🌀 Processing...")
            spoken_text = rec.recognize_google(audio, language='{}'.format(from_language))
            
            # Update the source caption
            source_caption.text(f"Source ({from_language}): {spoken_text}")
            
            output_placeholder.text("🌍 Translating...")
            progress_bar.progress(50)  # Simulate translation progress
            translated_text = translator_function(spoken_text, from_language, to_language)
            
            # Update the target caption
            target_caption.text(f"Target ({to_language}): {translated_text.text}")
            
            progress_bar.progress(100)
            text_to_voice(translated_text.text, to_language)
            time.sleep(1)
            progress_bar.empty()  # Clear progress bar after completion

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
            break

# UI layout
st.title("🌐 Real-Time Language Translator")
st.markdown("**Experience seamless translation with speech recognition and text-to-voice synthesis.**")

# UI customization for a more modern feel
with st.expander("🔧 Choose your translation settings", expanded=True):
    # Using columns for better layout
    col1, col2 = st.columns(2)
    
    with col1:
        from_language_name = st.selectbox("🎙️ Select Source Language", list(LANGUAGES.values()))
    
    with col2:
        to_language_name = st.selectbox("🗣️ Select Target Language", list(LANGUAGES.values()))

# Convert language names to language codes
from_language = get_language_code(from_language_name)
to_language = get_language_code(to_language_name)

# Adding buttons in a more streamlined layout
col_start, col_stop = st.columns(2)
start_button = col_start.button("▶️ Start Translation", use_container_width=True)
stop_button = col_stop.button("⏹️ Stop Translation", use_container_width=True)

# Placeholder for translation output and progress bar
output_placeholder = st.empty()
progress_bar = st.progress(0)

# Placeholders for displaying source and target language captions
st.markdown("### Translation Captions:")
col_source, col_target = st.columns(2)
source_caption = col_source.empty()
target_caption = col_target.empty()

# Check if "Start" button is clicked
if start_button:
    if not isTranslateOn:
        isTranslateOn = True
        output_placeholder.success("Translator is active! 🟢")
        main_process(output_placeholder, source_caption, target_caption, progress_bar, from_language, to_language)

# Check if "Stop" button is clicked
if stop_button:
    isTranslateOn = False
    output_placeholder.warning("Translator has been stopped! 🛑")
    progress_bar.empty()  # Clear progress bar if active
    source_caption.empty()  # Clear the source language caption
    target_caption.empty()  # Clear the target language caption


    """
import os
import time
import pygame # type: ignore
from gtts import gTTS # type: ignore
import streamlit as st # type: ignore
import speech_recognition as sr # type: ignore
from googletrans import LANGUAGES, Translator # type: ignore

isTranslateOn = False

translator = Translator()  # Initialize the translator module.
pygame.mixer.init()  # Initialize the mixer module.

# Create a mapping between language names and language codes
language_mapping = {name: code for code, name in LANGUAGES.items()}

def get_language_code(language_name):
    return language_mapping.get(language_name, language_name)

def translator_function(spoken_text, from_language, to_language):
    return translator.translate(spoken_text, src='{}'.format(from_language), dest='{}'.format(to_language))

def text_to_voice(text_data, to_language):
    myobj = gTTS(text=text_data, lang='{}'.format(to_language), slow=False)
    myobj.save("cache_file.mp3")
    audio = pygame.mixer.Sound("cache_file.mp3")  # Load a sound.
    audio.play()
    os.remove("cache_file.mp3")

def main_process(output_placeholder, source_caption_box, target_caption_box, progress_bar, from_language, to_language):
    global isTranslateOn
    
    while isTranslateOn:
        rec = sr.Recognizer()
        with sr.Microphone() as source:
            output_placeholder.text("🎤 Listening...")
            rec.pause_threshold = 1
            audio = rec.listen(source, phrase_time_limit=10)
        
        try:
            output_placeholder.text("🌀 Processing...")
            spoken_text = rec.recognize_google(audio, language='{}'.format(from_language))
            
            # Update the source caption box
            source_caption_box.text_area(f"**Source ({from_language}):**", spoken_text, height=150)
            
            output_placeholder.text("🌍 Translating...")
            progress_bar.progress(50)  # Simulate translation progress
            translated_text = translator_function(spoken_text, from_language, to_language)
            
            # Update the target caption box
            target_caption_box.text_area(f"**Target ({to_language}):**", translated_text.text, height=150)
            
            progress_bar.progress(100)
            text_to_voice(translated_text.text, to_language)
            time.sleep(1)
            progress_bar.empty()  # Clear progress bar after completion

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
            break

# UI layout
st.title("🌐 Real-Time Language Translator")
st.markdown("**Experience seamless translation with speech recognition and text-to-voice synthesis.**")

# UI customization for a more modern feel
with st.expander("🔧 Choose your translation settings", expanded=True):
    # Using columns for better layout
    col1, col2 = st.columns(2)
    
    with col1:
        from_language_name = st.selectbox("🎙️ Select Source Language", list(LANGUAGES.values()))
    
    with col2:
        to_language_name = st.selectbox("🗣️ Select Target Language", list(LANGUAGES.values()))

# Convert language names to language codes
from_language = get_language_code(from_language_name)
to_language = get_language_code(to_language_name)

# Adding buttons in a more streamlined layout
col_start, col_stop = st.columns(2)
start_button = col_start.button("▶️ Start Translation", use_container_width=True)
stop_button = col_stop.button("⏹️ Stop Translation", use_container_width=True)

# Placeholder for translation output and progress bar
output_placeholder = st.empty()
progress_bar = st.progress(0)

# Placeholders for displaying source and target language captions with larger text areas
st.markdown("### Translation Captions:")
col_source, col_target = st.columns(2)
source_caption_box = col_source.empty()
target_caption_box = col_target.empty()

# Check if "Start" button is clicked
if start_button:
    if not isTranslateOn:
        isTranslateOn = True
        output_placeholder.success("Translator is active! 🟢")
        main_process(output_placeholder, source_caption_box, target_caption_box, progress_bar, from_language, to_language)

# Check if "Stop" button is clicked
if stop_button:
    isTranslateOn = False
    output_placeholder.warning("Translator has been stopped! 🛑")
    progress_bar.empty()  # Clear progress bar if active
    source_caption_box.text_area("Source Language ", "", height=150)  # Clear the source language caption
    target_caption_box.text_area("Target Language ", "", height=150)  # Clear the target language caption


# Instructions to Run the Translator Application

# Step 1: Navigate to the project directory in the command prompt:
# Command: cd translator

# Step 2: Run the Streamlit application:
# Command: streamlit run main.py

# Step 3: If any errors occur due to missing dependencies, install them as follows:

# --- Recommended Setup ---
# Create a Virtual Environment (optional but recommended to isolate dependencies):
# Command: python -m venv myenv

# Activate the virtual environment:
# Windows: myenv\Scripts\activate
# Linux/Mac: source myenv/bin/activate

# --- Install Required Dependencies ---
# Use the following command to install the required packages:
# Command: pip install gtts pygame streamlit SpeechRecognition googletrans==3.1.0a0

# --- Optional ---
# To make dependency installation easier, you can create a requirements.txt file:
# Example content of requirements.txt:
# gtts
# pygame
# streamlit
# SpeechRecognition
# googletrans==3.1.0a0

# Install all dependencies listed in requirements.txt:
# Command: pip install -r requirements.txt

# --- Verify Installation ---
# Test the installed libraries in a Python script or interactive session:
# Example:
# import gtts
# import pygame
# import streamlit
# import speech_recognition
# from googletrans import Translator

# --- Troubleshooting ---
# If errors like "Command not found" or "Permission denied" occur, ensure pip is installed correctly and you have the required permissions.
# If googletrans==3.1.0a0 installation fails, try upgrading pip first:
# Command: pip install --upgrade pip
# Alternatively, use a compatible Python version (3.6 to 3.10).

