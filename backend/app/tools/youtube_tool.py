from youtube_transcript_api import YouTubeTranscriptApi


class YouTubeTool:

    def fetch_transcript(self, video_id: str):

        try:

            api = YouTubeTranscriptApi()

            transcript = api.fetch(video_id)

            text = " ".join(
                snippet.text
                for snippet in transcript
            )

            return text

        except Exception as e:

            print("YouTube Transcript Error:", e)
            return ""


youtube_tool = YouTubeTool()