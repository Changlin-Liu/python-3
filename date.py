from datetime import datetime, timedelta
now = datetime.now()
Tom = now + timedelta(hours=1)
Yes = now - timedelta(days=1)
print(Tom, '\n', Yes)