#!/bin/sh
curl -s -X POST \
  "https://api.apify.com/v2/acts/tidydata~audio-video-transcription/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"urls": [{"url": "https://upload.wikimedia.org/wikipedia/commons/d/dd/Armstrong_Small_Step.ogg"}], "includeSubtitles": true}'
