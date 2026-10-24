# Audio & video transcription API — Whisper, SRT & VTT (examples)

Transcribe **audio and video files** (MP3, M4A, WAV, OGG, FLAC, MP4, MOV, WebM…) or the latest episodes of **podcast RSS feeds** into text, timestamped segments and **SRT / VTT subtitles**. Powered by **Whisper large-v3-turbo**, **99 languages** with auto-detection, files up to 700 MB. Hosted on Apify: **[Audio & Video Transcription](https://apify.com/tidydata/audio-video-transcription)** — **$5 per 1,000 minutes** (a 1-hour file ≈ $0.30). No GPU, no OpenAI key.

## Python

```python
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("tidydata/audio-video-transcription").call(run_input={
    "urls": [{"url": "https://upload.wikimedia.org/wikipedia/commons/5/50/Jfk_rice_university_we_choose_to_go_to_the_moon.ogg"}],
    "language": "en",
    "includeSubtitles": True,
    "includeSegments": True,
})
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item["language"], item["durationMinutes"], "min")
    open("speech.srt", "w").write(item["srt"])
```

More: [`examples/podcast_feed.py`](examples/podcast_feed.py) (latest episodes of any podcast) · [`examples/node.mjs`](examples/node.mjs) · [`examples/curl.sh`](examples/curl.sh)

## Output per file

`text` · `srt` · `vtt` · `segments` (optional, `{start, end, text}`) · `language` · `durationMinutes` · `status` / `error` (failed files are free)

## YouTube?

Use the **[YouTube Transcript Scraper](https://apify.com/tidydata/youtube-transcript-scraper)** — it reads YouTube captions for videos, playlists and channels ($0.50 per 1,000 videos). Code examples: [tidydata-dev/youtube-transcript-scraper](https://github.com/tidydata-dev/youtube-transcript-scraper).

Examples are MIT-licensed.
