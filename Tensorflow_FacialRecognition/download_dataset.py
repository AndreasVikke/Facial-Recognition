import wget
import zipfile

wget.download('http://vis-www.cs.umass.edu/lfw/lfw.tgz')
with zipfile.ZipFile('lfw.tgz', 'r') as zip_ref:
    zip_ref.extractall('data')