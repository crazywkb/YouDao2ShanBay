from ShanBay.ShanBayAPI import ShanBayAPI
from YouDao.YouDaoAPI import YouDaoAPI
from utils.storage import write_result
from utils.storage import read_result
from bs4 import BeautifulSoup


def get_wordlist_by_crawler():
    youdao = YouDaoAPI()

    if not youdao.login():
        raise Exception("Error in login youdao.")

    previous_words = read_result()
    result, words = youdao.get_words()
    differ_words = set(words) - previous_words
    write_result(set(words))

    return differ_words


def get_wordlist_by_file(path):
    """
    xml file only.
    :param path: xml file path
    :return: set
    """
    with open(path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'lxml')
        words = [word.text for word in soup.findAll('word')]

        previous_words = read_result()
        differ_words = set(words) - previous_words
        write_result(set(words))

        return differ_words


def upload(words):
    shanbay = ShanBayAPI()
    failed_list = list()

    if not shanbay.login():
        raise Exception("Error in login Shanbay.")

    words = list(words)
    for word in words:
        result, failed = shanbay.add_to_vocabulary(word)
        if not result:
            print(f'Adding word {word} error.')
            continue
        failed_list.extend(failed)

    return failed_list


if __name__ == '__main__':
    wordlist = get_wordlist_by_crawler()
    failed_words = upload(wordlist)

    print("Words below fail to upload:")
    print(failed_words)
