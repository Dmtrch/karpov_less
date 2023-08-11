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

    valid_email_regex = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")

    # def is_valid_email(email: str) -> bool:
    #     return bool(re.fullmatch(valid_email_regex, email))

    emails = []

    for email in strings:
        if valid_email_regex.fullmatch(email):
            emails.append(email)
        # if is_valid_email(email):
        #     emails.append(email)

    return emails

st_t =timer()
a = valid_emails(emails_lst)
end_t =timer()
print(end_t-st_t)