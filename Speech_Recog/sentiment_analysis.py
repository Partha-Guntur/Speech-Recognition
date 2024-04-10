import requests
import time
import assemblyai as aai
import wave
import pyaudio


frames_per_buffer = 3500
format = pyaudio.paInt16
channels = 1
rate = 16000

p = pyaudio.PyAudio()

stream = p.open(
    format=format,
    channels=channels,
    rate = rate,
    input = True,
    frames_per_buffer=frames_per_buffer
)

print("Start Recording")

seconds = 5
frames = []
for i in range(1, int(rate/frames_per_buffer*seconds)):
    data = stream.read(frames_per_buffer)
    frames.append(data)

stream.stop_stream()
stream.close()
p.terminate()

obj= wave.open("output.wav", "wb")
obj.setnchannels(channels)
obj.setsampwidth(p.get_sample_size(format))
obj.setframerate(rate)
obj.writeframes(b"".join(frames))
obj.close()

aai.settings.api_key = "ba157cb544c3448eb90c7e607570331e"

base_url = "https://api.assemblyai.com/v2"

headers = {
    "authorization": "ba157cb544c3448eb90c7e607570331e" 
}

with open("./output.wav" , "rb") as f:
  response = requests.post(base_url + "/upload",
                          headers=headers,
                          data=f)

upload_url = response.json()["upload_url"]

audio_url = {
    "audio_url": upload_url # You can also use a URL to an audio or video file on the web
}

print(upload_url)

url = base_url + "/transcript"
response = requests.post(url, json=audio_url, headers=headers)
print(url)
transcript_id = response.json()['id']
polling_endpoint = f"https://api.assemblyai.com/v2/transcript/{transcript_id}"

while True:
  transcription_result = requests.get(polling_endpoint, headers=headers).json()

  if transcription_result['status'] == 'completed':
    print(transcription_result['text'])
    break

  elif transcription_result['status'] == 'error':
    raise RuntimeError(f"Transcription failed: {transcription_result['error']}")

  else:
    time.sleep(3)


config = aai.TranscriptionConfig(sentiment_analysis=True)

transcript = aai.Transcriber().transcribe(audio_url["audio_url"], config)

SENT_LIST = []

try:
   for i in transcript.sentiment_analysis:
      SENT_LIST.append(i.sentiment)

except TypeError:
    print("Audio Not Detected.")

DUP_DICT = {}

for word in SENT_LIST:
    if word in DUP_DICT:
        DUP_DICT[word] += 1
    else:
        DUP_DICT[word] = 1
try:
  most_common_word = max(DUP_DICT)
  print(most_common_word)
except ValueError:
   print("Audio Not Detected.")
