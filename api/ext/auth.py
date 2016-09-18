import hug


def init_app(app):
    @hug.request_middleware(api=app)
    def process_data(request, response):
        print('auth_req')

    @hug.response_middleware(api=app)
    def process_data(request, response, resource):
        print('auth_resp')