import re
import datetime
import pytz

UTC = pytz.utc
date = datetime.datetime.now(UTC)

def build(incoming):
    with open(incoming, 'w') as f:
        f.write('\n'.join([str(date)]))
    f.close()
