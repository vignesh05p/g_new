# modules/storage.py
import csv
import os
from datetime import datetime

def save_account(email, password, phone_number, proxy):
    data_dir = "data"
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    file_path = os.path.join(data_dir, "accounts.csv")
    header = ["Email", "Password", "Phone", "Proxy IP", "Timestamp"]
    
    file_exists = os.path.isfile(file_path)
    with open(file_path, "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        if not file_exists:
            writer.writerow(header)
        writer.writerow([email, password, phone_number, proxy, datetime.now()])
