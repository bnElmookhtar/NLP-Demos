from transformers import pipeline
import torch
import os

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

path = 'chunks/'
full_text = []

def concat_text(pipe, path=path):
    """
    Process all .wav chunks in a folder with a speech-to-text pipeline
    and concatenate the results.
    
    Args:
        pipe: Hugging Face ASR pipeline object
        path: Folder path containing audio chunks
        
    Returns:
        full_text_list: list of transcriptions for each chunk
        full_text_str: concatenated string of all transcriptions
    """
    files = sorted(os.listdir(path))  # sort to maintain chunk order
    full_text_list = []

    for file in files:
        if file.endswith('.wav'):
            audio_file = os.path.join(path, file)
            try:
                transcription = pipe(audio_file, generate_kwargs={"language":"arabic"})["text"]
                full_text_list.append(transcription)
            except Exception as e:
                print(f"Error processing {file}: {e}")
                continue

    full_text_str = " ".join(full_text_list) 
    return full_text_list, full_text_str


