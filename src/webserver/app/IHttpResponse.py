from abc import abstractmethod


class IHttpResponse:

    @abstractmethod
    def response(self):
        pass