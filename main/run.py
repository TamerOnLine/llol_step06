# main/run.py
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from main import create_app

app = create_app()

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",   # Use "127.0.0.1" to run locally only
        port=40514,       # Change this port if needed
        debug=True        # Set to False in production
    )
