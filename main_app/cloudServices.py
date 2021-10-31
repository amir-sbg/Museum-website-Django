from ibm_watson import TextToSpeechV1, NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions, CategoriesOptions, \
    EmotionOptions
from django.conf import settings as django_settings
import os
from django.conf import settings
from django.http import HttpResponse, Http404
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import json


def textToAudio(text, fileName):
    # print("---------------------",text,"-----------------------",fileName)
    authenticator = IAMAuthenticator("Pu-4ueMFN38jAdEWWdhxYfTZmqiXwOePPWi5nU8Hb3tR")
    text_to_speech = TextToSpeechV1(authenticator=authenticator)

    text_to_speech.set_service_url(
        'https://api.au-syd.text-to-speech.watson.cloud.ibm.com/instances/ca45dd7f-3fa0-4ac3-99b5-8231d03e833d')


    with open(os.path.join(django_settings.STATIC_ROOT, f'{fileName}.wav'), 'wb') as audio_file:
        audio_file.write(text_to_speech.synthesize(text, accept='audio/mp3').get_result().content)

    # pathAndFileName = "../statics/" + fileName + ".wav"
    #
    # with open(pathAndFileName, 'wb') as audio_file:
    #     audio_file.write(text_to_speech.synthesize(text, accept='audio/mp3').get_result().content)


def isCommentAcceptable(commentText):
    authenticator = IAMAuthenticator("HDE4tDgeqgMjIuuk92R9mPcoZy9uCAtzjZHYYTPnnww3")
    natural_language_understanding = NaturalLanguageUnderstandingV1(authenticator=authenticator, version='2021-08-01')

    natural_language_understanding.set_service_url(
        'https://api.au-syd.natural-language-understanding.watson.cloud.ibm.com/instances/f915172b-7b23-4e29-9084-274e0060bbb9')
    try:
        response = natural_language_understanding.analyze(
            text=commentText,
            features=Features(keywords=KeywordsOptions(sentiment=True, emotion=True, limit=2))).get_result()
        # print(json.dumps(response, indent=2))

        if float(response["keywords"][0]["emotion"]["sadness"]) > 0.6 or float(
                response["keywords"][0]["emotion"]["disgust"]) > 0.6 or float(
            response["keywords"][0]["emotion"]["anger"]) > 0.6 or float(
            response["keywords"][0]["emotion"]["fear"]) > 0.6:

            return False
        else:
            return True

    except:

        return True










# print(isCommentAcceptable("wow this is great"))

# textToAudio("hi", "Story-4")

#Every Saturday Daniel and his family go to the beach. They live far from the beach, but once a week the family gets into the car and Daniel's father drives for hours until they arrive. Daniel's parents love the beach. Daniel and his sister and brother love the beach. The family's dog loves the beach very much. But it is a problem to go to the beach every week. Daniel's father gets tired from driving so many hours. The rest of the family gets tired from sitting in the car for so many hours. Daniel's mother says: It's fun in the beach, but it takes too much time to get there and back! Daniel and his sister and brother are very sad. They want to go to the beach, but it is a problem. They try to go the swimming pool, but it is not the same thing. One day Daniel's parents come to talk with the kids. They say: We have a problem to go to the beach every week, but we love the beach, and you love the beach, and the dog loves the beach. So we have a solution. We need to live near the beach! Daniel and his sister and brother are very happy! Now they live near the beach. They go to the beach every day!
#Jane and Laura are walking to the mall. They want to buy new clothes. Jane has some money and Laura has some money. Suddenly, Jane is calling: Laura! Laura! Look at that dress! Isn't it beautiful? I want that dress, but I don't have enough money. Laura is calling: What are you talking about? This is an ugly dress! It is just horrible! I don't even want to see this dress. Ok, ok…Jane is whispering sadly. Suddenly Laura is calling: Oh my god! Look at this dress! It is beautiful! I want this dress. Oh, but look at the price. It is too expensive for me.Now Jane is calling: What are you talking about? This is an ugly dress! It is really horrible! I don't even want to see it. Ok, ok…Laura is whispering sadly. Now Jane is sad, and Laura is sad. They are walking home. They have no new clothes, but they know that next time they should respect other opinions
#Emily is 8 years old. She lives in a big house. She has a huge room. She has many toys and she has a lot of friends. But Emily is not happy. She has a secret. She doesn't want to tell anyone about her secret. She feels embarrassed. The problem is that if nobody knows about it, there is no one that can help her. Emily doesn't write her homework. When there is an exam – she gets sick. She doesn't tell anyone, but the truth is she can't read and write. Emily doesn't remember the letters of the alphabet. One day, Emily's teacher finds out. She sees that Emily can't write on the board. She calls her after class and asks her to tell the truth. Emily says, It is true. I don't know how to read and write. The teacher listens to her. She wants to help Emily. She tells her, That's ok. You can read and write if we practice together. So Emily and her teacher meet every day after class. They practice together. Emily works hard. Now she knows how to read and write!
#There was a nice little girl. She was 10 years old. Her name was April. One day, April asked her parents why she was called April. Her mother answered that she was called April because she was born in April. The little girl was very happy to hear that. She liked her name. April really liked the month April, too. This was because she had her birthday in that month. Her parents made her a party. All her friends came and celebrated with her, and she received a lot of presents. One day, her mother became pregnant and soon April had a little brother.  Her brother was born in February. Everyone came to visit the family. Everyone suggested names for the new baby. April did not understand what the problem was. This looked very simple to her. She said that if the baby was born in February, the correct name was February!
