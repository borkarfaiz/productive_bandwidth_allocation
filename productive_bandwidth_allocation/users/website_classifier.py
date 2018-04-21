import pandas as pd

from .users_classification import DATA_PATH

data = pd.read_csv(DATA_PATH + r'\users_key.csv', header=None, index_col=False,
                   names=['email_id',
                          'token_no',
                          'remaining_attempts'])


def classify_url():
    user_info = get_info()
    update_info(user_info=user_info, remaining_attempts=17)


def get_info():
    for i in range(len(data)):
        a = data.loc[i]
        if a.remaining_attempts > 0:
            return data.loc[data['email_id'] == a.email_id]
    raise Exception('All Tokens Have been used')


def update_info(user_info, remaining_attempts):
    data._set_value(user_info.index, 'remaining_attempts', remaining_attempts)
    data.to_csv(DATA_PATH + r'\users_key.csv', header=False, index=False)
    print(user_info.remaining_attempts)


classify_url()
