// npm i apify-client  ·  APIFY_TOKEN=... node examples/node.mjs
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const run = await client.actor('tidydata/audio-video-transcription').call({
    urls: [{ url: 'https://upload.wikimedia.org/wikipedia/commons/d/dd/Armstrong_Small_Step.ogg' }],
    includeSubtitles: true,
});
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(items[0].text);
