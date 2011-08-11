import urllib
import xml.etree.ElementTree as etree

from panorama.wrappers import Video


class Vimeo(Video):

    def __init__(self, url, options=None):
        self.url = url
        self.id = self.get_video_id()
        self.feed = self.get_feed()

    def get_video_id(self):
        """
        Returns the video ID from the video URL.

        Returns:
            A string with the youtube video id.
        """
        if not hasattr(self, "id"):
            id = self.url.split('/')[-1]
            # If somebody add parameters erase them too
            self.id = id.split('?')[-1]
        return self.id

    def get_feed(self):
        if not hasattr(self, "feed"):
            url = "http://vimeo.com/moogaloop/load/clip:%(id)s/embed?"\
                  "param_server=vimeo.com&param_clip_id=%(id)s" % {
                  "id": self.get_video_id()}
            self.feed = etree.parse(urllib.urlopen(url))
        return self.feed

    def get_title(self):
        if not hasattr(self, "title"):
            self.title = self.feed.find('.//caption').text
        return self.title

    def get_thumbnail(self):
        if not hasattr(self, "thumbnail"):
            self.thumbnail = self.feed.find('.//thumbnail').text
        return self.thumbnail

    def get_duration(self):
        if not hasattr(self, "duration"):
            self.duration = self.feed.find('.//duration').text
        return self.duration

    def get_flv(self):
        if not hasattr(self, "embed_url"):
            request_signature = self.feed.find(".//request_signature").text
            request_signature_expires = (
                    self.feed.find('.//request_signature_expires')).text
            self.flv = "http://www.vimeo.com/moogaloop/play/clip:%(id)s/"\
                       "%(request_signature)s/"\
                       "%(request_signature_expires)s/" % {
                       "id": self.get_video_id(),
                       "request_signature": request_signature,
                       "request_signature_expires": request_signature_expires}
        return self.flv

    def get_embed_url(self):
        if not hasattr(self, "embed_url"):
            self.embed_url = "http://vimeo.com/moogaloop.swf?clip_id=%(id)s&"\
                             "server=vimeo.com&fullscreen=1&show_title=1&"\
                             "show_byline=1&show_portrait=1" % {
                             "id": self.get_video_id()}
        return self.embed_url

    def get_embed_html(self, options=None):
        if not hasattr(self, "embed_html"):
            self.embed_html = (
                    '<object width="%(width)s" height="%(height)s">'\
                    '<param name="movie" value="%(movie)s%(options)s"></param>'\
                    '<param name="allowFullScreen" value="true"></param>'\
                    '<param name="allowscriptaccess" value="always"></param>'\
                    '<param name="wmode" value="transparent"></param>'\
                    '<embed '\
                    'src="%(movie)s%(options)s" '\
                    'type="application/x-shockwave-flash"'\
                    'allowscriptaccess="always" allowfullscreen="true"'\
                    'width="%(width)s" height="%(height)s">'\
                    '</embed>'\
                    '</object>'
                ) % ({
                    'width': options.get('width') or 560 if options else 560,
                    'height': options.get('height') or 349 if options else 349,
                    'movie': self.get_embed_url(),
                    'options': None,  # TODO
                })
        return self.embed_html

    def get_download_url(self):
        if not hasattr(self, "download_url"):
            self.download_url = self.get_flv()
        return self.download_url
