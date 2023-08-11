import re

##text = 'ул. Карпинского, дом № 20, корпус 3, квартира 98'
text_1 = [
    "test@example.com",
    "invalid_email@",
    "foo@bar.com",
    "инвалидная_почта@",
]*4
text_2 = str(text_1)
##pattern = r'\d+'
pattern_1 = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

a = re.findall(pattern_1, text_2)
print(list(a))

