import whisper
import json

def main():    
    print("loading model...")    
    model = whisper.load_model("base")

    print("predicting...")
    #result = model.transcribe("861b9e79-dbac-4a63-bfb7-c06e7f82e1c3.mp3")
    result = model.transcribe("https://augie-public-test.s3.amazonaws.com/27a8d8a9-5624-4b2f-a425-4fb99a891779/ff23affc-9ab7-458f-9792-d7b5a19ef223/861b9e79-dbac-4a63-bfb7-c06e7f82e1c3.mp3")    

    json_object = json.dumps(result, indent=4)
    
    # write to disk
    with open("data.json", "w") as outfile:
        outfile.write(json_object)
    
if __name__ == "__main__":
    main()
