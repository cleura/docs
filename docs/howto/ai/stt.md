---
description: How to use the AI API via Python, for speech-to-text
---
# Using audio transcription

Of the [on-demand models](../../reference/ai/llms.md) we provide, `faster-whisper-large-v3` is optimized for speech-to-text (STT) applications, also known as _audio transcription_.

More specifically, you may use {{brand}}'s OpenAI-compatible API to programmatically upload audio files and get back transcribed texts.

Here's how you can go about it with Python.

## Creating an AI API key

If you do not already have one, [create a new AI API key](api-keys.md).
Make sure the key has access to the `faster-whisper-large-v3` model.

Make a note of the bearer token of the new API key.

## Using the OpenAI Python library

Following is a Python script (`stt-demo.py`) that uses the OpenAI library:

```python
from openai import OpenAI

client = OpenAI(
    api_key="<your-bearer-token>",
    base_url="https://ai.cleura.cloud/v1"
)

with open("/path/to/the-audio-file.mp3", "rb") as audio_file:
    transcription = client.audio.transcriptions.create(
        model="faster-whisper-large-v3",
        file=audio_file,
    )

print(transcription)
```

To test STT, replace `the-audio-file.mp3` with an audio file from [LibriVox](https://librivox.org).
Use, for instance, [_The&nbsp;Aurora&nbsp;Borealis&nbsp;in&nbsp;1719&nbsp;by&nbsp;Sidney&nbsp;Perley&nbsp;(1858-1928)_](https://librivox.org/coffee-break-collection-13-weather-by-various/).
Directly download the file onto your local computer...

```console
$ cd /tmp
$ curl -O https://dn720704.ca.archive.org/0/items/cb13_weather_1712_librivox/cb013_auroraborealis1719_perley_cc_128kb.mp3
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 3927k  100 3927k    0     0  1639k      0  0:00:02  0:00:02 --:--:-- 1639k
```

...and replace `/path/to/the-audio-file.mp3` in `stt-demo.py` with `/tmp/cb013_auroraborealis1719_perley_cc_128kb.mp3`.

Run the script.
After a minute or so, you will get the transcription back.
