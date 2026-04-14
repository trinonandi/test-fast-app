from __future__ import annotations

import sys
from pathlib import Path

# Ensure `import app` works when the project isn't installed as a package.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
