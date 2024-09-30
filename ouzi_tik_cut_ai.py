import os
import whisper
from pytube import YouTube
from transformers import pipeline
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
from google.cloud import translate_v2 as translate

class OuziTikCutAI:
    def __init__(self):
        # Inicialización de modelos y API
        self.model = whisper.load_model("base")
        self.summarizer = pipeline("summarization")
        self.translate_client = translate.Client()

    def download_video(self, url, resolution='720p'):
        # Descargar video de YouTube
        yt = YouTube(url)
        video = yt.streams.filter(res=resolution).first()
        video.download('downloads/')
        print(f'Video descargado: {video.title}')
        return f'downloads/{video.default_filename}'

    def transcribe_video(self, video_path):
        # Transcribir video con Whisper
        result = self.model.transcribe(video_path)
        return result['text']

    def summarize_text(self, text):
        # Resumir el contenido del video
        summary = self.summarizer(text, max_length=130, min_length=30, do_sample=False)
        return summary[0]['summary_text']

    def translate_text(self, text, target_language='es'):
        # Traducir texto con Google Translate
        result = self.translate_client.translate(text, target_language=target_language)
        return result['translatedText']

    def add_subtitles_to_video(self, video_path, subtitles_text, output_path):
        # Agregar subtítulos al video
        video = VideoFileClip(video_path)
        subtitle_clip = TextClip(subtitles_text, fontsize=24, color='white', bg_color='black')
        subtitle_clip = subtitle_clip.set_position(('center', 'bottom')).set_duration(video.duration)
        final_clip = CompositeVideoClip([video, subtitle_clip])
        final_clip.write_videofile(output_path, codec='libx264', fps=24)

    def add_anti_copyright_effects(self, input_video, output_video):
        # Aplicar pequeños cambios al video para evitar problemas de copyright
        command = f'ffmpeg -i {input_video} -vf "eq=brightness=0.06:saturation=1.5" {output_video}'
        os.system(command)
