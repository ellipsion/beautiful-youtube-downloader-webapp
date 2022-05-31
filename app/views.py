from pytube import YouTube as yt
from django.shortcuts import redirect, render

# Create your views here.
def indexView(request):
    template_name = 'app/index.html'
    context = {}
    return render(request, template_name, context)

def searchView(request):
    template_name = 'app/index.html'
    vid_url = request.POST.get("yt_url")
    yt_obj = yt(url=vid_url)
    title = yt_obj.title
    thumb_url = yt_obj.thumbnail_url
    streams = yt_obj.streams.filter(progressive=True).filter(mime_type="video/mp4")
    context = {
        "title": title,
        "streams": streams,
        "thumb_url": thumb_url
    }
    return render(request, template_name, context)

def videoView(request):
    return redirect("https://rr1---sn-ci5gup-0qge.googlevideo.com/videoplayback?expire=1653832834&ei=ISiTYraTM8ybg8UPxcyo2Ak&ip=106.205.199.69&id=o-AHhxjFBOjEcAxxZQQGm4hbXbgTXzgDnbYk1DRtktsPL7&itag=397&aitags=133,134,135,136,137,160,242,243,244,247,278,394,395,396,397,398,399&source=youtube&requiressl=yes&mh=f5&mm=31,29&mn=sn-ci5gup-0qge,sn-ci5gup-qxaes&ms=au,rdu&mv=m&mvi=1&pl=22&initcwndbps=225000&spc=4ocVCwkRd8KnX5bg0awMxjZr7KcKTC3SRbGMRutdTg&vprv=1&mime=video/mp4&ns=p-SgHMhTfbHypgOusNA6qw8G&gir=yes&clen=13172763&dur=366.824&lmt=1647367998315464&mt=1653810778&fvip=2&keepalive=yes&fexp=24001373,24007246&c=WEB&txp=4532434&n=aVUOBOsvYSSnlA&sparams=expire,ei,ip,id,aitags,source,requiressl,spc,vprv,mime,ns,gir,clen,dur,lmt&lsparams=mh,mm,mn,ms,mv,mvi,pl,initcwndbps&lsig=AG3C_xAwRAIgQUdfqbXId14rlBf9LkiXbA-UoLg_oB28jiyo56ENQGQCIEmk1I8h8GHcqza0zbgLCBl0j-gvxdYshcaPde3A_k4v&alr=yes&sig=AOq0QJ8wRQIhAM_Noxfme6Tj_gsda2Jih2-y3P2Im47YitWmcqKEIgwxAiAkY8XCwMhm8tHlPov_ZXAelYaZVI3QycIq0ktjfQY7gw==&cpn=DYlDDJn5lXEk3RoY&cver=2.20220527.00.00&range=0-186059&rn=1&rbuf=0")