class Urls:
    BASE_URL = 'https://stellarburgers.nomoreparties.site/'
    LOGIN_PAGE = BASE_URL + 'login'
    FORGOT_PASSWORD = BASE_URL + 'forgot-password'
    RESET_PASSWORD = BASE_URL + 'reset-password'
    PROFILE = BASE_URL + 'account/profile'
    ORDER_HISTORY = BASE_URL + 'account/order-history'
    FEED = BASE_URL + 'feed'
    SIGN_UP = BASE_URL + 'api/auth/register'
    DELETE_USER = BASE_URL + 'api/auth/user'
    SIGN_IN = BASE_URL + 'api/auth/login'

    @classmethod
    def make_ingredient_url(cls, ingredient_id):
        return f'{cls.BASE_URL}ingredient/{ingredient_id}'