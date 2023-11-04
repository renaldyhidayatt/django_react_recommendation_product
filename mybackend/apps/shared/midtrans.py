import os
from midtransclient import Snap


snap = Snap(
    is_production=False,
    server_key=os.environ.get("MIDTRANS_SERVER_KEY"),
    client_key=os.environ.get("MIDTRANS_CLIENT_KEY"),
)
