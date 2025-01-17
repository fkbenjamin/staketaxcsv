from kuji.config_kuji import localconfig
from common.progress import Progress

SECONDS_PER_PAGE = 4


class ProgressKuji(Progress):

    def __init__(self):
        super().__init__(localconfig)

    def set_estimate(self, count_pages):
        self.add_stage("default", count_pages, SECONDS_PER_PAGE)
