from youtube_transcript_api import YouTubeTranscriptApi

ytt_api = YouTubeTranscriptApi()
transcript = ytt_api.fetch("tNZnLkRBYA8")

snippets = [entry.text for entry in transcript.snippets if entry.text]

with open("snippets.txt", "w", encoding="utf-8") as f:
    for snippet in snippets:
        f.write(snippet + " ")