from os.path import join, abspath, dirname, pardir
BASE_DIR = abspath(join(dirname(__file__)))
# print(BASE_DIR)
confdir = join(BASE_DIR,'conf.ini')
outputdir = join(BASE_DIR, 'results/')
randomdir = join(BASE_DIR, 'randomresults/')
LOG_FORMAT = "%(asctime)s %(name)-12s %(levelname)-8s %(message)s"