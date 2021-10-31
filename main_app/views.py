from django.shortcuts import render, HttpResponse
from . import models
from . import cloudServices
import mimetypes


def imagesPage(request):
    if request.method == "POST":
        # @TODO
        if len(request.POST['name']) != 0 and len(request.POST['comment']) != 0:
            audioLink = "Comment" + str(len(models.Comment.objects.all()) + 1) + "Post" + str(request.POST['imageID'])
            print("-------------------------------------------- Is Acceptable ...?", )
            isAcceptable = cloudServices.isCommentAcceptable(request.POST['comment'])
            # isAcceptable = True
            print("-------------------------------------- Acceptable : ",isAcceptable)
            if isAcceptable:
                print("-------------------------------------- Making Audio ...",)
                cloudServices.textToAudio(request.POST['comment'], audioLink)
                print("-------------------------------------- Audio made.")

            comment = models.Comment.objects.create(writersName=request.POST['name'], text=request.POST['comment'],
                                                    isAcceptable=isAcceptable, whichImageID=request.POST['imageID'],
                                                    commentID=str(len(models.Comment.objects.all()) + 1),
                                                    audioLink=audioLink)
            comment.save()



    postsImages = models.Image.objects.all()
    postsComments = models.Comment.objects.all()
    return render(request, 'home/ImagesPage.html', {"postsImages": postsImages, "postsComments": postsComments})


def storiesPage(request):
    if request.method == "POST":
        # @TODO
        if len(request.POST['name']) != 0 and len(request.POST['comment']) != 0:
            audioLink = "Comment" + str(len(models.Comment.objects.all()) + 1) + "Post" + str(request.POST['storyID'])

            print("-------------------------------------------- Is Acceptable ...?", )
            isAcceptable = cloudServices.isCommentAcceptable(request.POST['comment'])
            # isAcceptable = True
            print("-------------------------------------------- Acceptable   : ", isAcceptable)
            if isAcceptable :
                print("-------------------------------------- Making Audio   :", )
                cloudServices.textToAudio(request.POST['comment'], audioLink)
                print("-------------------------------------- Audio Made.")

            comment = models.Comment.objects.create(writersName=request.POST['name'], text=request.POST['comment'],
                                                    isAcceptable=isAcceptable, whichImageID=request.POST['storyID'],
                                                    commentID=str(len(models.Comment.objects.all()) + 1),
                                                    audioLink=audioLink)
            comment.save()

    postsStories = models.Storie.objects.all()
    postsComments = models.Comment.objects.all()
    return render(request, 'home/StoriesPage.html', {"postsStories": postsStories, "postsComments": postsComments})


def download_file(request):
    fl_path = '../statics/audios/'
    filename = request + '.wav'

    fl = open(fl_path, 'r')
    mime_type, _ = mimetypes.guess_type(fl_path)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response
