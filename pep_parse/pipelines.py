import csv

from collections import defaultdict
from pathlib import Path

from .settings import DATE_TIME

BASE_DIR = Path(__file__).parent.parent


class PepParsePipeline:
    def open_spider(self, spider):
        self.count_status = defaultdict(int)

    def process_item(self, item, spider):
        self.count_status[item['status']] = self.count_status.get(item['status'], 0) + 1
        return item
        
    def close_spider(self, spider):
        RESULTS_DIR = BASE_DIR / 'results'
        with open(f'{RESULTS_DIR}/status_summary_{DATE_TIME}.csv', mode='w', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile, dialect=csv.unix_dialect, quoting=csv.QUOTE_NONE)
            writer.writerow(['status', 'amount'])
            for status, amount in self.count_status.items():
                writer.writerow([status, amount])
            writer.writerow(['Total', sum(self.count_status.values())])
