import logging
import os
from datetime import datetime

LOGFILE =f"logs/{datetime.now().strftime('%Y-%m-%d')}.log"
os.makedirs(os.path.dirname(LOGFILE), exist_ok=True)

LOGFILE = os.path.join(os.getcwd(), LOGFILE)
logging.basicConfig(
    filename=LOGFILE,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S'
)
if __name__ == "__main__":
    logging.info("Logging setup complete.")
    logging.info(f"Log file created at: {LOGFILE}")
else:
    logging.getLogger(__name__).info("Logger initialized for module.")