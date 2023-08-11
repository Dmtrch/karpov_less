import re
from typing import List
from timeit import default_timer as timer

emails_lst = [
    "test@example.com",
    "invalid_email@",
    "foo@bar.com",
    "инвалидная_почта@",
]*1000000

pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

st_t =timer()
valid_emails = list(re.findall(pattern, str(emails_lst)))
end_t =timer()
print(end_t-st_t)