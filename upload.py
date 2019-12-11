from datetime import datetime
from random import random
import hashlib


ALLOWED_EXTENSIONS = set(['pdf', 'txt', 'rtf', 'odf', 'ods', 'gnumeric',
                          'abw', 'doc', 'docx', 'xls', 'xlsx', 'csv', 'zip',
                          'png', 'jpg', 'jpeg', 'gif', 'svg', 'bmp', 'webp',
                          'json', 'plist', 'xml', 'yaml', 'yml', 'c', 'php',
                          'js', 'babelrc', 'eslintrc', 'env', 'java', 'jsp'
                          'kt', 'hs', 'clj', 'go', 'rs', 'asp', 'class',
                          'dex', 'html', 'xhtml', 'toml', 'htm', 'ini',
                          'gitignore', 'gitconfig', 'vimrc', 'vim',
                          'bashrc', 'zshrc', 'd', 'lock', 'md',
                          'psd', 'ai', 'xd', 'wav', 'mp4', 'flac', 'mp3',
                          'avi', 'wmv', 'cgi', 'scheme', 'gradle', 'jar',
                          'phar', 'asar', 'cpp', 'cs', 'c', 'h', 'o',
                          'ico', 'ttf', 'otf', 'woff', 'woff2', 'eot',
                          'hwp'])


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


def generate_file_hash(filename):
    seed = filename + str(datetime.now()) + str(random())
    return hashlib.sha512(seed.encode('utf-8')).hexdigest()
