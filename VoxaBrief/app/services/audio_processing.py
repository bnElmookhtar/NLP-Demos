import ffmpeg 
import os

def convert_audio_format(input_file_path:str, output_file_path:str, target_format:str):
    """
        Convert Uploaded audio file to format that the model can understand.
        Args:
            input_file_path (str) : Path to the input audio file.
            output_file_path (str) : Path to save the converted audio file.
            target_format (str) : Desired audio format (e.g., 'wav', 'mp3').
    """
    try:
        (
            ffmpeg.input(input_file_path)
            .output(output_file_path, format=target_format,ac = 1 , ar = 16000)
            .overwrite_output().run(quiet=True)
        )
    except ffmpeg.Error as e:
        print(f"Error converting audio file: {e.stderr.decode()}")
        raise

if __name__ == "__main__":
    # Example usage
    input_path = "input_audio.mp3"
    output_path = "output_audio.wav"
    convert_audio_format(input_path, output_path, "wav")
    print(f"Converted {input_path} to {output_path}")
