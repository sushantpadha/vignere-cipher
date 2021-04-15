class Vignere:
    def __init__(self, msg: str, key: str):
        self.msg = msg
        self.key = self.get_key(len(msg), key)

    @staticmethod
    def get_table():
        pass

    @staticmethod
    def get_key(length: int, key: str):
        '''Return key with length same as msg

        Args:
            length (int): length of msg
            key (str): original key

        Returns:
            str: expanded key
        '''
        key_len = len(key)
        # repeat
        if key_len < length:
            key *= (length // key_len) + 1
        # slice
        return key[:length]

    def encrypt():
        pass

    def decrypt():
        pass


def main():
    pass


def parse_args():
    pass


if __name__=='__main__':
    pass

