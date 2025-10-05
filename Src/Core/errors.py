class argument_exception(Exception):
    ## некорректный аргумент
    def __init__(self, message: str):
        super().__init__(f"Argument error: {message}")
class operation_exception(Exception):
    ## логика или операции
    def __init__(self, message: str):
        super().__init__(f"Operation error: {message}")
class error_proxy(Exception):
    ##ориг ошибка
    def __init__(self, original_exception: Exception):
        super().__init__(f"Proxy error: {str(original_exception)}")
        self.original_exception = original_exception
