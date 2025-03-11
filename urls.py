class Urls:
    BASE_URL = 'https://stellarburgers.nomoreparties.site/'
    LOGIN_PAGE = BASE_URL + 'login'
    FORGOT_PASSWORD = BASE_URL + 'forgot-password'
    RESET_PASSWORD = BASE_URL + 'reset-password'
    PROFILE = BASE_URL + 'account/profile'
    ORDER_HISTORY = BASE_URL + 'account/order-history'
    FEED = BASE_URL + 'feed'

    @classmethod
    def make_ingredient_url(cls, ingredient_id):
        return f'{cls.BASE_URL}ingredient/{ingredient_id}'