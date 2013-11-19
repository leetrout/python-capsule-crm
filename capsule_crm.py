import copy
import json
import os

import requests

BASE_URL = "https://%s.capsulecrm.com/api/"


class ImproperlyConfigured(Exception):
    pass


class CapsuleCRM(object):
    def __init__(self, cap_name=None, cap_key=None):
        env = os.environ
        self.cap_name = cap_name or env.get('CAPSULE_NAME')
        self.cap_key = cap_key or env.get('CAPSULE_KEY')
        if not self.cap_name or not self.cap_key:
            raise ImproperlyConfigured('Missing capsule subdomain name')
        self.auth = requests.auth.HTTPBasicAuth(self.cap_key, self.cap_name)
        self.base_url = BASE_URL % self.cap_name
        self.headers = {
            'accept': 'application/json',
            'content-type': 'application/json'
        }
        self.path = []
        self.qs = {}
        self.method = 'get'
        self.explicit_qs = {}  # needed for posting with a query string

    def __getattr__(self, method):
        # Create a new copy of self
        obj = self._copy()
        # add method to path
        obj.path.append(method)
        return obj.mock_attr

    def _copy(self):
        obj = self.__class__(self.cap_name, self.cap_key)
        obj.path = copy.copy(self.path)
        obj.qs = copy.copy(self.qs)
        return obj

    def mock_attr(self, *args, **kwargs):
        """
        Empty method to call to slurp up args and kwargs.

        `args` get pushed onto the url path.
        `kwargs` are converted to a query string and appended to the URL.
        """
        self.path.extend(args)
        self.qs.update(kwargs)
        return self

    def set_qs(self, data=None, **kwargs):
        """Set the explicit query string"""
        if data is not None:
            kwargs.update(data)
        self.explicit_qs.update(kwargs)
        return self

    @property
    def url(self):
        url = self.base_url + '/'.join(map(str, self.path))
        return url

    @property
    def request(self):
        args = (self.method, self.url)
        kwargs = {
            'auth': self.auth,
            'headers': self.headers,
        }
        if self.method == 'get':
            kwargs['params'] = self.qs
        else:
            kwargs['data'] = json.dumps(self.qs)
            kwargs['params'] = self.explicit_qs

        return requests.request(*args, **kwargs)

    def get(self):
        self.method = 'get'
        return self.request

    def post(self):
        self.method = 'post'
        return self.request

    def put(self):
        self.method = 'put'
        return self.request

    def delete(self):
        self.method = 'delete'
        return self.request

    @property
    def json(self):
        """Short cut to json. Only works for GET requests.

        cap.party().json instead of cap.part().get().json

        """
        return getattr(self, self.method)().json
