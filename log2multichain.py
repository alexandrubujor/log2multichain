import sys
import re
from Savoir import Savoir
import configs as CONFIGS


def multichain_log(item_key, line):
    api = Savoir(CONFIGS.RPCUSER, CONFIGS.RPCPASSWD, CONFIGS.RPCHOST, CONFIGS.RPCPORT, CONFIGS.CHAINNAME)
    message = line.split(':')[-1]
    data_hex = message.encode('utf-8').hex()
    api.publish(CONFIGS.STREAM, item_key, data_hex)


def process_line(line):
    m = re.search(CONFIGS.RE_KEY,
                  line,
                  re.IGNORECASE)
    try:
        item_key = m.group(1)
        multichain_log(item_key, line)
    except Exception:
        pass


if __name__=="__main__":
    for line in sys.stdin:
        process_line(line)
