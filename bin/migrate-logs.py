#!/usr/bin/env python3

import glob
import json
import canonicaljson
import sys
import os


for log_path in glob.glob('./collection/log/*/*.json'):
    log = json.load(open(log_path))
    if "resource" in log:
        path = "collection/resource/" + log["resource"]
        if not os.path.exists(path):
            if os.system(f"make {path}"):
                sys.exit(1)
        bytes = os.path.getsize(path)
        log["bytes"] = bytes
        data = canonicaljson.encode_canonical_json(log)
        print(f"updating {log_path}")
        with open(log_path, "wb") as f:
            f.write(data)
