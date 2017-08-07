import requests
from multiprocessing import Pool
import time

startURL = 'http://i.stanford.edu/~ullman/focs/ch'
extension = '.pdf'
savePath = '' #enter the path for the pdfs to be stored on your system
chapters = range(1,15) #chapters 1-14

def chapterStringManipulate(chapter):
  if chapter < 10 :
    download('0{}'.format(chapter))
  else :
    download('{}'.format(chapter))

  return None


def download(chapter):

  url = '{}{}{}'.format(startURL, chapter, extension)
  r = requests.get(url, stream=True)

  path = '{}{}{}'.format(savePath, chapter, extension)

  with open(path, 'wb') as fd:
    for chunk in r.iter_content(2048):
      fd.write(chunk)
      
  print '{} downloaded'.format(chapter)

  return None


if __name__ == '__main__':
  pool = Pool(processes=len(chapters))
  results = pool.map(chapterStringManipulate, chapters)
