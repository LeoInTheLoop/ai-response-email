from pathlib import Path


BASE_DIR = Path(__file__).parent.parent  


DATA_DIR = BASE_DIR / "data"
RAW_EMAILS_PATH = DATA_DIR / "raw/emails.csv"
TRAIN_DATA_PATH = DATA_DIR / "train_dataset/phillip_allen_emails.csv"


TEMPLATE_DIR = BASE_DIR / "templates"  


LOG_DIR = BASE_DIR / "logs"