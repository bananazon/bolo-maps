#!/usr/bin/env python3

import os
import re
from pathlib import Path

from titlecase import titlecase

for path in Path("/Users/gary.danko/github/bolo-maps").rglob("*.map"):
    basename = os.path.basename(path.name).replace("_", " ")
    dirname = os.path.dirname(path)

    cleaned = re.sub(r"\s+", " ", basename)

    new_basename = titlecase(cleaned)
    new_path = os.path.join(dirname, new_basename)
    print(new_path)
    # os.rename(path, new_path)
