#!/usr/bin/env python3
"""Fetch YouTube transcript for a given video URL or ID.

Tries all available languages, preferring English.
Falls back to whatever language is available.
Prints the plain text transcript to stdout.
"""
import re
import sys

from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import NoTranscriptFound, TranscriptsDisabled


def extract_video_id(url_or_id: str) -> str:
    """Extract video ID from various YouTube URL formats."""
    patterns = [
        r"(?:youtube\.com/shorts/)([a-zA-Z0-9_-]{11})",
        r"(?:youtube\.com/watch\?v=)([a-zA-Z0-9_-]{11})",
        r"(?:youtu\.be/)([a-zA-Z0-9_-]{11})",
        r"^([a-zA-Z0-9_-]{11})$",
    ]
    for pattern in patterns:
        match = re.search(pattern, url_or_id)
        if match:
            return match.group(1)
    return url_or_id


def fetch_transcript(video_id: str) -> str:
    """Fetch transcript, trying English first, then any available language."""
    api = YouTubeTranscriptApi()

    # Try English first, then fall back to any language
    for langs in [["en"], ["en-US", "en-GB"], None]:
        try:
            if langs:
                transcript = api.fetch(video_id, languages=langs)
            else:
                # Fetch whatever is available
                transcript_list = api.list(video_id)
                first = next(iter(transcript_list))
                transcript = first.fetch()
            return "\n".join(s.text for s in transcript.snippets)
        except NoTranscriptFound:
            continue

    raise NoTranscriptFound(video_id, ["en"], None)


def main():
    if len(sys.argv) < 2:
        print("Usage: yt-transcript.py <youtube-url-or-id>", file=sys.stderr)
        sys.exit(1)

    video_id = extract_video_id(sys.argv[1])

    try:
        text = fetch_transcript(video_id)
        print(text)
    except TranscriptsDisabled:
        print(f"ERROR: Transcripts are disabled for video {video_id}", file=sys.stderr)
        sys.exit(2)
    except NoTranscriptFound:
        print(f"ERROR: No transcript found for video {video_id}", file=sys.stderr)
        sys.exit(3)
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
