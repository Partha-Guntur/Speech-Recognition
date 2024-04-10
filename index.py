import assemblyai as aai

# Replace with your API key
aai.settings.api_key = "ba157cb544c3448eb90c7e607570331e"

# URL of the file to transcribe
FILE_URL = "https://cdn.assemblyai.com/upload/c1848340-fb5c-462a-ad94-b8191c81672f"

# You can also transcribe a local file by passing in a file path
# FILE_URL = './path/to/file.mp3'

transcriber = aai.Transcriber()
transcript = transcriber.transcribe(FILE_URL)

if transcript.status == aai.TranscriptStatus.error:
    print(transcript.error)
else:
    print(transcript.text)
