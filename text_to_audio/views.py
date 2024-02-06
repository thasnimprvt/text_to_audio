import os
from django.conf import settings
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
from gtts import gTTS
class ReadTextView(APIView):
    def post(self, request):
        text = request.data.get('text')
        #print(text)
        res = to_audio(text)
        return Response({'text': res}, status=status.HTTP_200_OK)


def to_audio(text):
    output_file = "malayalam_audio.mp3"
    audio_path = os.path.join(settings.MEDIA_ROOT, output_file)
    try:
        # Language parameter set to 'ml' for Malayalam
        tts = gTTS(text=text, lang='ml', slow=False)
        # Ensure the media directory exists
        os.makedirs(settings.MEDIA_ROOT, exist_ok=True)
        # Save the audio file
        tts.save(audio_path)
        print(f"Audio saved as {audio_path}")
        audio_link = os.path.join(settings.MEDIA_URL, output_file)

        
        # Return the audio file as a response
        response_data = {
            'success': True,
            'message': 'Audio generation successful',
            'audio_link': f'http://localhost:8000/{audio_link}',
        }
        return response_data
    except Exception as e:
        response_data = {
            'success': False,
            'message': f'Error: {e}',
        }
        return response_data