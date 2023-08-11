import re
from typing import List
from timeit import default_timer as timer
from multiprocessing import Pool, cpu_count

emails_lst = [
    "test@example.com",
    "invalid_email@",
    "foo@bar.com",
    "инвалидная_почта@",
] * 10000000

def valid_emails(strings: List[str]) -> List[str]:
    valid_email_regex = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    return [email for email in strings if valid_email_regex.fullmatch(email)]

def chunk_list(lst, chunk_size):
    for i in range(0, len(lst), chunk_size):
        yield lst[i:i + chunk_size]

def process_chunk(chunk):
    return valid_emails(chunk)

if __name__ == "__main__":
    chunk_size = len(emails_lst) // cpu_count()
    chunks = list(chunk_list(emails_lst, chunk_size))

    with Pool(cpu_count()) as pool:
        st_t = timer()
        results = pool.map(process_chunk, chunks)
        a = [email for chunk in results for email in chunk]
        end_t = timer()

    print(end_t - st_t)
