import csv
from collections import defaultdict
from pathlib import Path

from .settings import DATE_TIME

BASE_DIR = Path(__file__).parent.parent


class PepParsePipeline:
    def open_spider(self, spider):
        self.count_status = defaultdict(int)

    def process_item(self, item, spider):
        self.count_status[item['status']] = self.count_status.get(
            item['status'], 0
        ) + 1
        return item

    def close_spider(self, spider):
        RESULTS_DIR = BASE_DIR / 'results'
        filename = f'{RESULTS_DIR}/status_summary_{DATE_TIME}.csv'
        with open(filename, mode='w', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(
                (
                    ('Status', 'Amount'),
                    *self.count_status.items(),
                    ('Total', sum(self.count_status.values()))
                )
            )
