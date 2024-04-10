import wave
import pyaudio
from pydub import AudioSegment

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

audio = AudioSegment.from_wav("output.wav")

audio = audio + 6
audio = audio * 2
audio = audio.fade_in(2000)
audio.export("test1.mp3", format="mp3")
audio2 = AudioSegment.from_mp3("test1.mp3")
print("Done")

obj.close()


