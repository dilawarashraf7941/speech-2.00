import streamlit as st
import speech_recognition as sr

# Create a Streamlit app
st.title("Speech to Text")
st.write("Speak into your microphone, and I'll transcribe what you say!")

# Create a text area to display the transcribed text
text_area = st.text_area("Transcribed text:", value="", height=200)

# Create a button to start the speech recognition
start_button = st.button("Start speaking")

if start_button:
    # Create a speech recognition object
    r = sr.Recognizer()
    # Create a microphone object
    with sr.Microphone() as source:
        # Adjust the microphone settings
        r.adjust_for_ambient_noise(source)
        st.write("Listening...")
        # Record audio from the microphone
        audio = r.listen(source)
        st.write("Processing...")
        # Try to recognize the speech
        try:
            text = r.recognize_google(audio, language="en-US")
            st.write("Transcribed text:")
            # Update the text area with the transcribed text
            st.text_area("Transcribed text:", value=text, height=200)
        except sr.UnknownValueError:
            st.write("Sorry, I didn't understand what you said.")
        except sr.RequestError as e:
            st.write(f"Could not request results; {e}")

# Note: This will only work locally where the microphone access is available
# and Streamlit can capture audio input.

