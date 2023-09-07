import whisper
import json
import os

def main():    
    print("loading model...")    
    model = whisper.load_model("base")

    print("predicting...")
    audio_url = os.environ.get("AUDIO_URL")
    
    result = model.transcribe(
        audio_url, word_timestamps=True
    )

    data = json.dumps(result, indent=4)
    
    # write to disk
    with open("data.json", "w") as outfile:
        outfile.write(data)
    
if __name__ == "__main__":
    main()
