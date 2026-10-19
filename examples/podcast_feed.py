"""Transcribe the 3 latest episodes of a podcast feed and save Markdown show notes. pip install apify-client"""
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("tidydata/audio-video-transcription").call(run_input={
    "urls": [{"url": "https://feeds.npr.org/510318/podcast.xml"}],
    "maxEpisodes": 3,
    "language": "auto",
})
for i, ep in enumerate(client.dataset(run["defaultDatasetId"]).iterate_items(), 1):
    if ep.get("status") != "ok":
        continue
    with open(f"episode_{i}.md", "w", encoding="utf-8") as f:
        f.write(f"# {ep.get('title') or ep['sourceUrl']}\n\n{ep['text']}\n")
    print("saved episode", i, ep["durationMinutes"], "min")
