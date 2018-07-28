var tag=document.createElement('script');
tag.src = "https://www.youtube.com/iframe_api"
var firstScriptTag = document.getElementsByTagName('script')[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

function onYouTubeIframeAPIReady(){
    ytPlayer = newYT.player(
        'youtube',
        {
            width: 640,
            height: 390,
            videoId: 
        }
    );
}