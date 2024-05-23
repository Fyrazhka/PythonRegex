import re


#Validation of phone numbers
def first_task():
    phone_list = ["(123) 456-7890", "(098) 765-4321", "123-456-7890", "(123 456-7890", "(123)456-7890"]
    phone_pattern=re.compile(r'^\(\d{3}\) \d{3}-\d{4}')
    for phone in phone_list:
        print(phone + " is a ")
        if(phone_pattern.match(phone)):
            print("valid phone number")
        else:
            print("not valid phone number")


#url search
def second_task():
    text = """Visit our website at https://example.com or http://www.test.org. You can also find us at http://subdomain.example.net."""
    url_pattern = re.compile(r'https?://[a-zA-Z0-9_.-]+\.[a-zA-Z]{2,}')
    url_in_text = url_pattern.findall(text)
    print(url_in_text)


#correct date search
def third_task():
    text = """Event dates: 05-12-2024, 11-23-2023 and 06-05-2022. Please note the date 01-32-2023 is incorrect."""
    #date_pattern = re.compile(r'\d{2}-\d{2}-\d{4}') #without checking
    date_pattern = re.compile(r'\b(?:0[1-9]|[12][0-9]|3[01])-(?:0[1-9]|1[0-2])-\d{4}\b')
    date = date_pattern.findall(text)
    print(date)


#delete HTML tags
def fourth_task():
    html_text = "<html><body><h1>Heading</h1><p>This is a paragraph.</p><a href=\"https://example.com\">Link</a></body></html >"
    html_pattern = re.compile(r'<.*?>')
    new_text = html_pattern.sub("", html_text)
    print(new_text)


#Extracting information from logs
def fifth_task():
    log_list = ["127.0.0.1 - - [26/May/2024:12:05:22 +0000] \"GET /index.html HTTP/1.1\" 200 1024", "192.168.0.1 - - [26/May/2024:12:06:43 +0000] \"POST /form HTTP/1.1\" 404 512"]
    log_pattern = re.compile(r'(?P<ip>\d+.\d+.\d+.\d+) - - \[(?P<date>.*?)\] "(?P<method>GET|POST|PUT|DELETE|HEAD|OPTIONS|PATCH) .*"')
    for log in log_list:
        match = log_pattern.match(log)
        if match:
            print(f"IP: {match.group("ip")} Date: {match.group("date")} Method: {match.group("method")}")


#Validation and time extraction
def additional_task():
    time_texts = [
        "Время начала: 09:30",
        "Конец события: 18:45",
        "Неверное время: 25:00",
        "Еще одно неверное время: 12:60",
        "Время: 07:07"
    ]
    time_pattern = re.compile(r'\b(?:0[0-9]|1[0-9]|2[0-4]):(?:0[0-9]|[1-5][0-9])\b')
    for t in time_texts:
        if time_pattern.findall(t):
            print(time_pattern.findall(t))


#Validation and extraction of credit card numbers
def additional_task2():
    texts = [
        "Card number: 1234-5678-9012-3456",
        "Invalid number: 1234-5678-9012-345",
        "Another incorrect number: 12345-6789-0123-4567",
        "Correct number: 9876-5432-1098-7654"
    ]
    card_pattern = re.compile(r'\b\d{4}-\d{4}-\d{4}-\d{4}\b')
    for t in texts:
        if(card_pattern.findall(t)):
            print(card_pattern.findall(t))

def main():
    first_task()
    second_task()
    third_task()
    fourth_task()
    fifth_task()
    additional_task()
    additional_task2()

if __name__ == '__main__':
    main()
