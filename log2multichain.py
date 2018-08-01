import sys
import re
from Savoir import Savoir

STREAM="audit"
RPCUSER="multichainrpc"
RPCPASSWD="H2Up87TFAu9armrk6hnvdV8WrbAtTC4smAZpHoo5W1Sv"
RPCHOST="stage.b4.bluedrive.ro"
RPCPORT="14326"
CHAINNAME="chain-b4"


def multichain_log(app_id, line):
    api = Savoir(RPCUSER, RPCPASSWD, RPCHOST, RPCPORT, CHAINNAME)
    stream_key = "app_{}".format(app_id)
    data_hex = line.encode('utf-8').hex()
    api.publish(STREAM, stream_key, data_hex)

def process_line(line):
    m = re.search("\[ Application (\d+) \]",
                  line,
                  re.IGNORECASE)
    try:
        app_id = m.group(1)
        multichain_log(app_id, line)
    except Exception:
        pass


if __name__=="__main__":
    for line in sys.stdin:
        process_line(line)
