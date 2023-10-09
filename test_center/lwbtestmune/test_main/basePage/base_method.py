import requests



class basePages(object):

    def request_post(self, url, data, header=None):
        res = requests.post(url=url, data=data, headers=header).text
        return res

    def request_get(self, url, data, header=None):
        res = requests.get(url=url, params=data, headers=header).text
        return res

    def request_put(self, url, data, header=None):
        res = requests.put(url=url, data=data, headers=header).text
        return res

    def request_delete(self, url, data, header=None):
        res = requests.delete(url=url, data=data, headers=header).text
        return res

    def request_patch(self, url, data, header=None):
        res = requests.patch(url=url, data=data, headers=header).text
        return res

    def request_main(self, method, url, data, header=None):

        if method == 'POST':
            res = self.request_post(url, data, header)
        elif method == 'GET':
            res = self.request_get(url, data, header)
        elif method == 'PUT':
            res = self.request_put(url, data, header)
        elif method == 'PATCH':
            res = self.request_patch(url, data, header)
        else:
            res = self.request_delete(url, data, header)
        return res


base_pages = basePages()
