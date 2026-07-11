class ToolRegistry:

    TOOLS = {
        "summarizer": "Summarization Tool",
        "sentiment": "Sentiment Analysis Tool",
        "code_explainer": "Code Explanation Tool",
        "youtube_transcript": "YouTube Transcript Tool"
    }

    @classmethod
    def get(cls, tool_name: str):
        return cls.TOOLS.get(tool_name)