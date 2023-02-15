import requests
import shutil
import time

number = 0

for i in range(123):
    number += 1
    r = requests.get(f'https://randomfox.ca/images/{number}.jpg', stream=True)
    if r.status_code == 200:
        with open(f"img{number}.jpg", 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)
    time.sleep(1)
