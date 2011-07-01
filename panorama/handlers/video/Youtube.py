from panorama.wrappers import Video

import gdata.youtube.service


class Youtube(Video):

    def __init__(self, url, options=None):
        self.url = url
        self.id = self.get_video_id()

    def get_video_entry(self):
        if not hasattr(self, "entry"):
            try:
                self.entry = (gdata.youtube.service.YouTubeService().
                              GetYouTubeVideoEntry(video_id=self.id))
            except:
                print "Youtube video with id %s doesn't exists" % self.id
                return
        return self.entry

    def get_video_id(self):
        """
        Returns the video ID from the video URL.

        Returns:
            A string with the youtube video id.
        """
        if not hasattr(self, "id"):
            self.id = self.get_url_parameters('v')
        return self.id

    def get_title(self):
        if not hasattr(self, "title"):
            self.title = self.get_video_entry().media.title.text
        return self.title

    def get_description(self):
        if not hasattr(self, "description"):
            self.description = self.get_video_entry().media.description.text
        return self.description

    def get_thumbnails(self):
        if not hasattr(self, "thumbnail"):
            self.thumbnails = []
            for thumbnail in self.get_video_entry().media.thumbnail:
                self.thumbnails.append(thumbnail.url)
        return self.thumbnails

    def get_thumbnail(self):
        """
        From the list of all thumbnails returns only the first.

        Returns:
            A string with a url for the thumbnail.
        """
        if not hasattr(self, "thumbnail"):
            self.thumbnail = self.get_thumbnails()[0]
        return self.thumbnail

    def get_duration(self):
        if not hasattr(self, "duration"):
            self.duration = self.get_video_entry().media.duration.seconds
        return self.duration

    def get_flv(self):
        """
        With this handler, this function do exactly the same that the
        function get_embed_url()
        """
        if not hasattr(self, "embed_url"):
            self.embed_url = self.get_video_entry().GetSwfUrl()
        return self.embed_url

    def get_embed_url(self):
        if not hasattr(self, "embed_url"):
            self.embed_url = self.get_video_entry().GetSwfUrl()
        return self.embed_url

    def get_embed_html(self, options=None):
        if not hasattr(self, "embed_html"):
            self.embed_html = (
                    '<object width="%(width)s" height="%(height)s">'
                    '<param name="movie" value="%(movie)s">'
                    '<param name="allowFullScreen" value="true">'
                    '<param name="allowscriptaccess" value="always">'
                    '<param name="wmode" value="transparent">'
                    '<embed '
                    'src="%(movie)s" type="application/x-shockwave-flash"'
                    'allowscriptaccess="always" allowfullscreen="true"'
                    'width="%(width)s" height="%(height)s">'
                    '</object>'
                ) % ({
                    'width': options.get('width') or 560 if options else 560,
                    'height': options.get('height') or 349 if options else 349,
                    'movie': self.get_embed_url()
                })
        return self.embed_html

    def get_download_url(self):
        if not hasattr(self, "download_url"):
            self.download_url = self.get_video_entry().GetSwfUrl()
        return self.download_url

    def get_tags(self):
        if not hasattr(self, "tags"):
            self.tags = self.get_video_entry().media.keywords.text.split(',')
        return self.tags
