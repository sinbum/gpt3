def get_token_with_file(file_path):
    """
    put the patht where the token is
    :param path: token_path. ex) c:\token
    :return: str
    """

    if len(file_path) < 3:
        raise Exception('set the api_token at gpt/config.ini')

    with open(file_path, 'r') as f:
        token = f.read()

    return token
