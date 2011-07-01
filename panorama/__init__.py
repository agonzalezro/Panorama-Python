from urlparse import urlparse


class Resource(object):

    def __init__(self, url, options=None):
        """
        Search the handler and create the object.

        Parameters:
            url - the resource url
            options - the resource options
        """
        def __init__(self, url, options=None):
            self.url = url

    def get_object(self):
        """
        Returns the created object.

        Returns:
            The instance of the class.
        """
        return self.object

    def get_handler_name(self):
        """
        Returns a string with the handler module name.

        Returns:
            A string with the correct handler.
        """
        host = urlparse(self.url).hostname
        try:
            domain_parts = host.split('.')
        except AttributeError:
            raise ValueError('The URL provided is not valid!')
        # If has subdomains return the second part, else the first one
        domain_parts_count = len(domain_parts)
        return domain_parts[domain_parts_count - 2].lower()

    def get_url_parameters(self, only_this_key):
        """
        Get a dictionary with all the parameters in the query.

        Returns:
            A dict() with all the parameters in the query or if a key was
            provided, the value of this key.
        """
        params = urlparse(self.url).query.split('&')
        result = dict()
        for param in params:
            key, value = param.split('=')
            if key == only_this_key:
                return value
            result.update({key: value})
        return result
