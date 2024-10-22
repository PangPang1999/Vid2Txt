import os
import moviepy.editor as mp
import speech_recognition as sr
from pydub import AudioSegment

def split_audio(audio_path, segment_length_ms=60000):
    """
    将音频文件按指定的时长切割成小段。
    Splits an audio file into smaller segments of a specified length.
    
    :param audio_path: 输入音频的路径 Path to the input audio file
    :param segment_length_ms: 每段音频的时长，默认为60秒（60000毫秒）
                              Duration of each segment in milliseconds (default is 60 seconds, i.e., 60000 ms)
    :return: 分割后的音频段列表 List of audio segments after splitting
    """
    audio = AudioSegment.from_wav(audio_path)
    audio_segments = [audio[i:i+segment_length_ms] for i in range(0, len(audio), segment_length_ms)]
    return audio_segments

def mp4_to_text(mp4_path):
    # 提取 mp4 文件的文件名和路径
    # Extract the MP4 file name and its path
    base_path, file_name = os.path.split(mp4_path)
    file_name_without_ext = os.path.splitext(file_name)[0]

    # 定义输出的 txt 文件路径
    # Define the output path for the .txt file
    txt_output_path = os.path.join(base_path, file_name_without_ext + '.txt')

    # 使用 moviepy 提取音频并保存为 wav 格式
    # Use moviepy to extract the audio and save it as a .wav file
    audio_output_path = os.path.join(base_path, file_name_without_ext + '.wav')
    video = mp.VideoFileClip(mp4_path)
    video.audio.write_audiofile(audio_output_path)

    # 初始化语音识别器
    # Initialize the speech recognizer
    recognizer = sr.Recognizer()

    # 将音频分割成60秒一段
    # Split the audio into 60-second segments
    audio_segments = split_audio(audio_output_path, segment_length_ms=60000)

    full_text = ""

    # 逐段处理音频
    # Process the audio segments one by one
    for i, segment in enumerate(audio_segments):
        # 为每段生成临时文件
        # Generate a temporary file for each segment
        segment_path = os.path.join(base_path, f"segment_{i}.wav")
        segment.export(segment_path, format="wav")

        with sr.AudioFile(segment_path) as source:
            print(f"Processing segment {i+1}/{len(audio_segments)}...")
            # 读取该段音频
            # Load the audio for the current segment
            audio_data = recognizer.record(source)

            try:
                # 使用 Google Web Speech API 进行识别
                # Use Google Web Speech API for speech recognition
                # 将语言更改为中文（普通话） 'zh-CN'，也可以改为其他语言代码
                text = recognizer.recognize_google(audio_data, language='en-US')
                print(f"Segment {i+1} recognized.")
                # 将识别的文本加到最终结果中
                # Append the recognized text to the final result
                full_text += text + "\n"

            except sr.UnknownValueError:
                print(f"Segment {i+1} could not be understood.")
            except sr.RequestError as e:
                print(f"Could not request results from the recognition service for segment {i+1}; {e}")

        # 删除临时音频段文件
        # Delete the temporary audio segment file
        os.remove(segment_path)

    # 将识别的完整文本保存到 txt 文件中
    # Save the full transcription to the .txt file
    with open(txt_output_path, "w") as txt_file:
        txt_file.write(full_text)

    print(f"Full transcription saved to: {txt_output_path}")

    # 删除临时的整体音频文件
    # Delete the temporary audio file
    os.remove(audio_output_path)

if __name__ == "__main__":
    # 用户输入的 mp4 文件路径
    # Prompt the user to enter the path of the MP4 file
    mp4_file_path = input("Enter the path of the mp4 file: ")
    
    if os.path.exists(mp4_file_path):
        mp4_to_text(mp4_file_path)
    else:
        # 如果指定的 MP4 文件不存在
        # If the specified MP4 file does not exist
        print("The specified mp4 file does not exist.")
