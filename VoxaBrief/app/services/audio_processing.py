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


def split_audio_ffmpeg(input_file, chunk_length_sec=30, overlap_sec=3, output_dir="chunks"):
    """
    Split an audio file into chunks with overlap using FFmpeg.
    
    Args:
        input_file (str): Path to input audio
        chunk_length_sec (int): Length of each chunk in seconds
        overlap_sec (int): Overlap between chunks in seconds
        output_dir (str): Directory to save chunks
    
    Returns:
        List of output chunk file paths
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Get audio duration using ffprobe
    probe = ffmpeg.probe(input_file)
    duration = float(probe['format']['duration'])

    chunks = []
    start = 0
    idx = 0

    while start < duration:
        end = min(start + chunk_length_sec, duration)
        output_file = os.path.join(output_dir, f"chunk_{idx}.wav")
        (
            ffmpeg
            .input(input_file, ss=start, t=(end-start))
            .output(output_file, ac=1, ar=16000)  # Mono, 16kHz
            .overwrite_output()
            .run(quiet=True)
        )
        chunks.append(output_file)
        start += (chunk_length_sec - overlap_sec)
        idx += 1

    return chunks


if __name__ == "__main__":
   chunks = split_audio_ffmpeg("input_audio.mp3", chunk_length_sec=30, overlap_sec=3)
   print("Chunks created:", chunks)
