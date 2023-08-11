import re
from typing import List
from timeit import default_timer as timer

emails_lst = [
    "test@example.com",
    "invalid_email@",
    "foo@bar.com",
    "инвалидная_почта@",
]*10000000

def valid_emails(strings: List[str]) -> List[str]:
    """Take list of potential emails and returns only valid ones"""

    valid_email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

    def is_valid_email(email: str) -> bool:
        return bool(re.fullmatch(valid_email_regex, email))

    emails = []
    index = 0
    while index < len(strings):
        email = strings[index]
        if is_valid_email(email):
            emails.append(email)
        index += 1

    ##for email in strings:
    ##    if is_valid_email(email):
    ##        emails.append(email)

    return emails

st_t =timer()
a = valid_emails(emails_lst)
end_t =timer()
print(end_t-st_t)