import hug
import jwt

def init_app(app):
    @hug.request_middleware(api=app)
    def process_data(request, response):
        try:
            auth_header = request.headers['AUTHORIZATION']
            bearer, token = auth_header.split()
            # TODO: Verify Key
            # jwt.verify_jwt(token)

        except KeyError as e:
            print('no Authorization')


    @hug.response_middleware(api=app)
    def process_data(request, response, resource):
        print('auth_resp')