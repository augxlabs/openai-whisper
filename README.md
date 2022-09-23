# Open AI Whisper
Whisper is a general-purpose speech recognition model. It is trained on a large dataset of diverse audio and is also a multi-task model that can perform multilingual speech recognition as well as speech translation and language identification. https://github.com/openai/whisper

sample
```sh
Title: 'web demo - storytelling.mp3'
FileName: '861b9e79-dbac-4a63-bfb7-c06e7f82e1c3.mp3',
AugieId '310'
AudioUrl: 'https://augie-public-test.s3.amazonaws.com/27a8d8a9-5624-4b2f-a425-4fb99a891779/ff23affc-9ab7-458f-9792-d7b5a19ef223/861b9e79-dbac-4a63-bfb7-c06e7f82e1c3.mp3'
```

## pre-requisite

- [install docker](https://www.docker.com/get-started/)

# Docker

## run

```sh
docker-compose up --build
```

## data

```sh
./data.json
```

# Cog

## run 

```sh
cog predict -i "https://augie-public-test.s3.amazonaws.com/27a8d8a9-5624-4b2f-a425-4fb99a891779/ff23affc-9ab7-458f-9792-d7b5a19ef223/861b9e79-dbac-4a63-bfb7-c06e7f82e1c3.mp3"
```