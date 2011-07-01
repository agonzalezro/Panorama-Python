from django.shortcuts import render_to_response

from panorama.wrappers import Video

def index(request):
    video = Video('http://www.youtube.com/watch?v=QH2-TGUlwu4')
    return render_to_response('youtube/index.html',
                              {'details': video.get_video_details()})
