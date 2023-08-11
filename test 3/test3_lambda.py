import re
from typing import List
from timeit import default_timer as timer

emails_lst = [
    "test@example.com",
    "invalid_email@",
    "foo@bar.com",
    "инвалидная_почта@",
]*10000000

##def valid_emails(strings: List[str]) -> List[str]:
##    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
##    return list(re.findall(pattern, str(strings)))

valid_emails = lambda strings : list(re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
                                                str(strings)))

st_t =timer()
list = valid_emails(emails_lst)
end_t =timer()
print(end_t-st_t)