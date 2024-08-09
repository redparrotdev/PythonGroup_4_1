'''
S - single responsibility principle
Принцип единственной ответственности

Каждый класс должен быть ответственным только за 1 задачу
'''


class ReportCreator:

    def create_report(self, data):
        print(f"Creating report using {data}")
        return "Report"


class ReportSender:

    def __init__(self, email):
        self.email = email

    def send_report(self, report: str):
        print("Sending report")



