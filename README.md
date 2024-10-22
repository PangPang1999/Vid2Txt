# Vid2Txt
This Python script converts MP4 videos without subtitles into text files. Simply input an MP4 video, and it will generate a corresponding .txt file in the same directory. It is free to use for educational purposes. Although the accuracy is high, errors may still occur, so it's not suitable for commercial use.

## Requirements (环境要求)

- Python 3.11
- ffmpeg
- 必须安装以下Python库：
  - moviepy
  - SpeechRecognition
  - pydub

## Installation Guide (安装指南)
### 1. Install Python 3.11 (安装 Python 3.11)
Installing and managing Python versions using pyenv:
```
brew install pyenv
brew install pyenv-virtualenv
```
Modify the configuration file to ensure pyenv loads automatically:
```
# Load pyenv automatically by appending
if command -v pyenv 1>/dev/null 2>&1; then
  eval "$(pyenv init --path)"
  eval "$(pyenv init -)"
  eval "$(pyenv virtualenv-init -)"
fi
```
Refresh the terminal:
```
source ~/.zprofile
```
### 2. Install Python 3.11 and Create Virtual Environment (安装Python 3.11并创建虚拟环境)
Using pyenv to install Python 3.11 and set it as the global version:
```
pyenv install 3.11
pyenv global 3.11
```
Creating a virtual environment:
```
pyenv virtualenv 3.11 myenv
```
### 3. Install ffmpeg (安装 ffmpeg)
```
brew install ffmpeg
```
### 4. Activate Virtual Environment and Install Dependencies (激活虚拟环境并安装依赖)
Reopen the terminal and activate the virtual environment:
```
pyenv activate myenv
```
Install the dependencies in the virtual environment:
```
pip install moviepy SpeechRecognition pydub
```
### 5. Run the Script (运行脚本)
Download the video_to_text.py file and place it on your desktop
Run the following command in the terminal to start the script
```
python3 video_to_text.py
```
Input the path to the MP4 file, and the conversion to text will begin.

### 6.Deactivate the Virtual Environment:
After the conversion is complete, you can exit the virtual environment using the following command:
```
pyenv deactivate
```
## Notes (注意事项)

The script currently uses Google Web Speech API for transcription, and the language can be changed by modifying the language parameter in the recognize_google method.
脚本使用Google Web Speech API进行转录，可以通过修改 recognizer.recognize_google 函数中的 language 参数更改识别语言。
For example, use 'zh-CN' for Mandarin or 'yue-Hant-HK' for Cantonese.
例如，使用 'zh-CN' 进行普通话识别，或使用 'yue-Hant-HK' 进行粤语识别。

