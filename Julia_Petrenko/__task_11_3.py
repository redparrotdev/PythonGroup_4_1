class Logger:

    def log(self, msg: str):
        ...


class SomeDataClass:

    def __init__(self, logger: Logger):
        self.__logger = logger

    def some_data_process(self, data: str):
        print("Starting processing")
        print(f"Processing {data}")
        print("Data process finished")

        # Performing logging
        print("Logging data")
        self.__logger.log(f"[LOG] Data <{data}> processed!")


class ConsoleLogger(Logger):

    def log(self, msg: str):
        print(msg)


class FileLogger(Logger):

    def __init__(self, file: str):
        super().__init__()
        self.file = file

    def log(self, msg: str):
        with open("my_log.txt", "a") as f:
            f.write(msg+"\n")


console_logger = ConsoleLogger()
file_logger = FileLogger("my_log.txt")

l1 = SomeDataClass(console_logger)
l1.some_data_process("Data for class 1")

l2 = SomeDataClass(file_logger)
l2.some_data_process("Data for class 2")



