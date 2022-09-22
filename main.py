import whisper
import json

def main():    
    print("loading model...")    
    model = whisper.load_model("base")

    print("predicting...")
    result = model.transcribe("861b9e79-dbac-4a63-bfb7-c06e7f82e1c3.mp3")
    
    # Serializing json
    json_object = json.dumps(result, indent=4)
    
    # Writing to sample.json
    with open("data.json", "w") as outfile:
        outfile.write(json_object)
    
if __name__ == "__main__":
    main()
