from pydub import AudioSegment

audio = AudioSegment.from_wav("output.wav")

audio = audio + 6
audio = audio * 2
audio = audio.fade_in(2000)
audio.export("test1.mp3", format="mp3")
audio2 = AudioSegment.from_mp3("test1.mp3")
print("Done")
