from panorama import Resource


class Video(Resource):
    """
    Wrapper class to get the correct video handler.
    """

    NOT_IMPLEMENTED_ERROR =\
        'This function isn\'t implemented with this handler.'

    def __init__(self, url, options=None):
        self.url = url
        super(Video, self).__init__(url, options)

        # We get the handler name and capitalize it
        handler_name = self.get_handler_name().title()
        try:
            handler = __import__('panorama.handlers.video.%s' % handler_name,
                                 fromlist=['q'])
            # Create a instance of the object handler_name from handler
            self.object = getattr(handler, handler_name)(url, options)
        except ImportError:
            print 'The handler: %s doesn\'t exists.' % handler_name

    def get_download_url(self):
        """
        Returns the video flv url.

        Returns:
            A string with the flv url.
        """
        if hasattr(self.object, "get_download_url"):
            return self.object.get_download_url()
        else:
            raise NotImplementedError(self.NOT_IMPLEMENTED_ERROR)

    def get_duration(self):
        """
        Returns the duration of the video.

        Returns:
            A string with the duration of the video in seconds.
        """
        if hasattr(self.object, "get_duration"):
            return self.object.get_duration()
        else:
            raise NotImplementedError(self.NOT_IMPLEMENTED_ERROR)

    def get_embed_html(self, options=None):
        """
        Returns the embeded html code.

        Returns:
            A string with the embeded html.
        """
        if hasattr(self.object, "get_embed_html"):
            return self.object.get_embed_html(options)
        else:
            raise NotImplementedError(self.NOT_IMPLEMENTED_ERROR)

    def get_embed_url(self):
        """
        Returns the video embed url for the instantiated object.

        Returns:
            A string with the embed of the video.
        """
        if hasattr(self.object, "get_embed_url"):
            return self.object.get_embed_url()
        else:
            raise NotImplementedError(self.NOT_IMPLEMENTED_ERROR)

    def get_flv(self):
        """
        Returns the url of the video.

        Returns:
            A string with the url of the video.
        """
        if hasattr(self.object, "get_flv"):
            return self.object.get_flv()
        else:
            raise NotImplementedError(self.NOT_IMPLEMENTED_ERROR)

    def get_description(self):
        """
        Returns the description for this video.

        Returns:
            A string with the video's description.
        """
        if hasattr(self.object, "get_description"):
            return self.object.get_description()
        else:
            raise NotImplementedError(self.NOT_IMPLEMENTED_ERROR)

    def get_tags(self):
        """
        Returns a list with tags.

        Returns:
            A list with the tags.
        """
        if hasattr(self.object, "get_tags"):
            return self.object.get_tags()
        else:
            raise NotImplementedError(self.NOT_IMPLEMENTED_ERROR)

    def get_thumbnail(self):
        """
        Returns the video thumbnail url.

        Returns:
            A url with a thumbnail.
        """
        if hasattr(self.object, "get_thumbnail"):
            return self.object.get_thumbnail()
        else:
            raise NotImplementedError(self.NOT_IMPLEMENTED_ERROR)

    def get_thumbnails(self):
        """
        Returns the video thumbnail urls.

        Returns:
            A list with the thumbnails.
        """
        if hasattr(self.object, "get_thumbnails"):
            return self.object.get_thumbnails()
        else:
            raise NotImplementedError(self.NOT_IMPLEMENTED_ERROR)

    def get_title(self):
        """
        Returns the video title.

        Returns:
            A string with the video title.
        """
        if hasattr(self.object, "get_title"):
            return self.object.get_title()
        else:
            raise NotImplementedError(self.NOT_IMPLEMENTED_ERROR)

    def get_video_details(self):
        """
        Returns the video details.

        If some of the attribs that the function tried to get aren't
        implemented, they will not be returned as key on the dict.

        Returns:
            A dictionary with all the video info.
        """
        list_to_retrieve = ('title', 'thumbnail', 'thumbnails', 'embed_url',
                            'embed_html', 'flv', 'download_url',
                            'handler_name', 'duration', 'description', 'tags')

        if not hasattr(self, "details"):
            self.details  = dict()
            for attrib in list_to_retrieve:
                try:
                    self.details.update({
                        attrib: getattr(self.object, 'get_%s' % attrib)()
                        })
                except NotImplementedError:
                    pass
        return self.details
