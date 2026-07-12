from app.models.extracted_content import ExtractedContent

from app.tools.youtube_tool import youtube_tool
from app.utils.youtube_utils import YouTubeUtils


class YouTubeService:

    @staticmethod
    def process(text: str):

        video_id = YouTubeUtils.extract_video_id(text)

        if video_id is None:

            return None

        print("\n========== YOUTUBE ==========")
        print("Video ID:", video_id)

        transcript = youtube_tool.fetch_transcript(
            video_id
        )

        if not transcript:

            print("⚠️ Could not fetch transcript.")

            return None

        print("Transcript Length:", len(transcript))

        return ExtractedContent(
            source="youtube",
            content=transcript
        )