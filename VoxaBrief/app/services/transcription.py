from transformers import pipeline
import torch


def transcribe_audio(audio_file_path: str,model_name :str = "omarxadel/hubert-large-arabic-egyptian" ) -> str:
    """
         Transcribes given audio file to text using a pre-trained ASR model.
            Args:
                audio_file_path (str): Path to the audio file to be transcribed.
            Returns:
                str: Transcribed text.
    """
    device = "cuda:0" if torch.cuda.is_available() else "cpu"

    pipe = pipeline(
        "automatic-speech-recognition",
        model=model_name, 
        device=device
    )
