from hashlib import md5

YOUDAO_ACCOUNT_INFO = {
    'username': '',
    'password': ''
}

SHANBAY_ACCOUNT_INFO = {
    'account': '',
    'password': ''
}

SHANBAY_API = {
    'login': 'https://apiv3.shanbay.com/bayuser/login',
    'add_vocabulary': 'https://www.shanbay.com/bdc/vocabulary/add/batch'
}

SHANBAY_DATA = {
    'login': SHANBAY_ACCOUNT_INFO,
    'add_vocabulary': {
        'words': None,
        # _: 'timestamp' optional
    }
}

YOUDAO_API = {
    'login': 'https://logindict.youdao.com/login/acc/login',
    '': ''
}

YOUDAO_DATA = {
    'login': {
        'app': 'web',
        'tp': 'urstoken',
        'cf': 3,
        'product': 'DICT',
        'username': YOUDAO_ACCOUNT_INFO['username'],
        'password': md5(YOUDAO_ACCOUNT_INFO['password'].encode()).hexdigest(),
    },
    '': ''
}
