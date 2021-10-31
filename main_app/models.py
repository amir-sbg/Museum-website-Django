from django.db import models


class Comment(models.Model):
    writersName = models.CharField(max_length=50)
    text = models.CharField(max_length=2000)
    isAcceptable = models.BooleanField()
    whichImageID = models.CharField(max_length=20)
    audioLink = models.CharField(max_length=300)
    commentID = models.CharField(max_length=40)


class Image(models.Model):
    imageAddress = models.CharField(max_length=200)
    imageID = models.CharField(max_length=40)


class Storie(models.Model):
    storiesText = models.CharField(max_length=2000)
    audioLink = models.CharField(max_length=300)
    storieID = models.CharField(max_length=40)

# https://s4.uupload.ir/files/5_hjp8.jpg
# https://s4.uupload.ir/files/4_s678.jpg
# https://s4.uupload.ir/files/3_28uz.jpg
# https://s4.uupload.ir/files/1_l79s.jpg
# https://s4.uupload.ir/files/1_fez6.jpg
