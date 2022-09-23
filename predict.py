import string
from cog import BasePredictor, Input, Path
import whisper
import json

class Predictor(BasePredictor):
    def setup(self):
        """Load the model into memory to make running multiple predictions efficient"""
        print("loading model...")    
        self.model = whisper.load_model("base")

    # The arguments and types the model takes as input
    def predict(self,
          contentUrl: str = Input(description="Audio url", default="https://augie-public-test.s3.amazonaws.com/27a8d8a9-5624-4b2f-a425-4fb99a891779/ff23affc-9ab7-458f-9792-d7b5a19ef223/861b9e79-dbac-4a63-bfb7-c06e7f82e1c3.mp3"),
    ) -> str:
        """Run a single prediction on the model"""
        
        print("predicting...")
        result = self.model.transcribe(contentUrl)

        json_object = json.dumps(result, indent=4)
        return json_object