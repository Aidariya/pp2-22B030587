from datetime import datetime, timedelta
thist = datetime.now().replace(microsecond=0)
othert = timedelta(1)
a = thist - othert
diff = thist - a
print(diff.total_seconds())