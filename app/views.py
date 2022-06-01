from django.http import Http404
from django.shortcuts import redirect, render
from pytube import YouTube as yt

# Create your views here.
def indexView(request):
    template_name = 'app/index.html'
    context = {}
    return render(request, template_name, context)

def searchView(request):
    if request.POST:
        template_name = 'app/index.html'
        vid_url = request.POST.get("yt_url")
        yt_obj = yt(url=vid_url)
        try:
            title = yt_obj.title
            thumb_url = yt_obj.thumbnail_url
            streams = yt_obj.streams
            vid_streams = streams.filter(progressive=True).filter(mime_type="video/mp4")
            audio_stream = streams.filter(type="audio").first()
            audio_size = round(audio_stream.filesize/1000000, 2)
            context = {
                "title": title,
                "streams": vid_streams,
                "thumb_url": thumb_url,
                "audio_stream": audio_stream,
                "audio_size": audio_size
            }
            return render(request, template_name, context)
        except:
            raise Http404('Invalid Youtube URL')
    else:
        return redirect("index")

