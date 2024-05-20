import io
import os
import wave
import json
from google.cloud import speech_v1p1beta1 as speech
from google.cloud import storage
from google.cloud.speech_v1 import RecognizeResponse
from google.protobuf.json_format import MessageToJson,MessageToDict


class diarization():


    def callSpeechAPI (self,filename,form) -> any:
        pathJson = "resources/"
        json_name = "client_secret.json"
        pathSpeech = "uploads/"
        pathSpeechFile = pathSpeech + filename
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = pathJson + json_name
        client = speech.SpeechClient()
        with open(pathSpeechFile, "rb") as audio_file:
            content = audio_file.read()

        audio = speech.RecognitionAudio(content=content)

        diarization_config = speech.SpeakerDiarizationConfig(
            enable_speaker_diarization=True,
            min_speaker_count=2,
            max_speaker_count=10,
        )
        if form["encoding"] == "AMR_WB":
            config = speech.RecognitionConfig(
                encoding=speech.RecognitionConfig.AudioEncoding.AMR_WB,
                sample_rate_hertz=int(form["sampleRateHertz"]),
                language_code="en-US",
                diarization_config=diarization_config,
            )
        else:
            config = speech.RecognitionConfig(
                encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
                sample_rate_hertz=8000,
                language_code="en-US",
                diarization_config=diarization_config,
            )

        print("Waiting for operation to complete...")
        response = client.recognize(config=config, audio=audio)
        # result = response.results[-1]
        #
        # words_info = result.alternatives[0].words

        # Printing out the output:
        # for word_info in words_info:
        #     print(
        #         u"word: '{}', speaker_tag: {}".format(word_info.word, word_info.speaker_tag)
        #     )
        res = MessageToJson(response._pb, preserving_proto_field_name=True)
        return res

