Panorama
========

This is a fork from the original project [Panorama-PHP] (https://raw.github.com/frandieguez/Panorama-PHP) writted by [@frandieguez] (https://twitter.com/#!/frandieguez).

Thank to the [gondor project] (http://gondor.io) I can show you the example working on this page <http://bv969.o1.gondor.io/>

What  is this?
--------------

With this wrapper class you can manage any video service in a uniformed and
unique way. You only need the URL from the video service you are going to use.

A quick first example:

    from panorama.wrappers import Video
    resource = Video('http://www.youtube.com/watch?v=eF0Zb0UvQzU')
    print resource.get_title()
    mirblu maps en TVE
    print resource.get_description()
    Emisión de mirblu maps en el programa: "Castilla y León, huellas de futuro" de TVE


Install it!
-----------

1. Just put in you project as a new module. Perhaps in the future could be good, have the possibility to install it as a pip package.


Dependencies
------------
You can find them on the requeriments.txt file and install with `pip install -r requeriments.txt`.


Use it!
-------

The idea is make it as simple as possible. For a URL video like <http://www.youtube.com/watch?v=eF0Zb0UvQzU>:

    In [1]: from panorama.wrappers import Video
    In [2]: resource = Video('http://www.youtube.com/watch?v=eF0Zb0UvQzU')


Then you have methods to know information about the video in your application:

- `get_download_url()`: get the download url.

        In [3]: resource.get_download_url()
        Out[3]: 'http://www.youtube.com/v/eF0Zb0UvQzU?f=videos&app=youtube_gdata'

- `get_duration()`: get duration of the video in seconds.

        In [4]: resource.get_duration()
        Out[4]: '404'

- `get_embed_html(options=None)`: get embeded html to use in your webpage. You can use a dict to specify the width and height

        In [5]: print resource.get_embed_html()
        Out[5]: '<object width="560" height="349"><param name="movie" value="http://www.youtube.com/v/eF0Zb0UvQzU?f=videos&app=youtube_gdata"><param name="allowFullScreen" value="true"><param name="allowscriptaccess" value="always"><param name="wmode" value="transparent"><embed src="http://www.youtube.com/v/eF0Zb0UvQzU?f=videos&app=youtube_gdata" type="application/x-shockwave-flash" allowscriptaccess="always" allowfullscreen="true" width="560" height="349"></object>'

- `get_embed_url()`: get only the embeded url.

        In [6]: resource.get_embed_url()
        Out[6]: 'http://www.youtube.com/v/eF0Zb0UvQzU?f=videos&app=youtube_gdata'

- `get_flv()`: get a link to download the video.

        In [7]: resource.get_flv()
        Out[7]: 'http://www.youtube.com/v/eF0Zb0UvQzU?f=videos&app=youtube_gdata'

- `get_handler_name()`: get the name of the service in lowercase.

        In [8]: resource.get_handler_name()
        Out[8]: 'youtube'

- `get_description()`: a description of the video.

        In [9]: resource.get_description()
        Out[9]: 'Emisi\xc3\xb3n de mirblu maps en el programa: "Castilla y Le\xc3\xb3n, huellas de futuro" de TVE'

- `get_tags()`: the tags defined in the video.

        In [10]: resource.get_tags()
        Out[10]: ['tve', ' mirblu', ' maps', ' invidentes', ' posicionamiento']

- `get_thumbnail()`: the first thumbails if it has several thumbs.

        In [11]: resource.get_thumbnail()
        Out[11]: 'http://i.ytimg.com/vi/eF0Zb0UvQzU/0.jpg'

- `get_thumbnails()`: all the thumbs.

        In [12]: resource.get_thumbnails()
        Out[12]:
        ['http://i.ytimg.com/vi/eF0Zb0UvQzU/0.jpg',
         'http://i.ytimg.com/vi/eF0Zb0UvQzU/1.jpg',
         'http://i.ytimg.com/vi/eF0Zb0UvQzU/2.jpg',
         'http://i.ytimg.com/vi/eF0Zb0UvQzU/3.jpg']

- `get_title()`: the title of the video.

        In [13]: resource.get_title()
        Out[13]: 'mirblu maps en TVE'

- `get_video_details()`: all the details together.

        In [10]: resource.get_video_details()
        Out[10]:
        {'description': 'Emisi\xc3\xb3n de mirblu maps en el programa: "Castilla y Le\xc3\xb3n, huellas de futuro" de TVE',
         'download_url': 'http://www.youtube.com/v/eF0Zb0UvQzU?f=videos&app=youtube_gdata',
         'duration': '404',
         'embed_html': '<object width="560" height="349"><param name="movie" value="http://www.youtube.com/v/eF0Zb0UvQzU?f=videos&app=youtube_gdata"><param name="allowFullScreen" value="true"><param name="allowscriptaccess" value="always"><param name="wmode" value="transparent"><embed src="http://www.youtube.com/v/eF0Zb0UvQzU?f=videos&app=youtube_gdata" type="application/x-shockwave-flash" allowscriptaccess="always" allowfullscreen="true" width="560" height="349"></object>',
         'embed_url': 'http://www.youtube.com/v/eF0Zb0UvQzU?f=videos&app=youtube_gdata',
         'flv': 'http://www.youtube.com/v/eF0Zb0UvQzU?f=videos&app=youtube_gdata',
         'handler_name': 'youtube',
         'tags': ['tve', ' mirblu', ' maps', ' invidentes', ' posicionamiento'],
         'thumbnail': 'http://i.ytimg.com/vi/eF0Zb0UvQzU/0.jpg',
         'thumbnails': ['http://i.ytimg.com/vi/eF0Zb0UvQzU/0.jpg',
                        'http://i.ytimg.com/vi/eF0Zb0UvQzU/1.jpg',
                        'http://i.ytimg.com/vi/eF0Zb0UvQzU/2.jpg',
                        'http://i.ytimg.com/vi/eF0Zb0UvQzU/3.jpg'],
         'title': 'mirblu maps en TVE'}

Examples
--------

At the moment you can find a example working with django under the path example\_django. The panorama module in this examples uses a symbolic link, if doesn't work for you, erase the link and copy the module inside the example directory.


Supported services
------------------

The original project supports a lot of services, but at the moment this project is beginning, so we must go step-by-step supporting:


- Youtube


And... what else?
-----------------
If you find a bug or want to suggest a new video service, please let us know in [a ticket](http://github.com/agonzalezro/panorama-python/issues).

Thank you!
