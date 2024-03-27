class error_exception:
    # 400 Bad Request
    EMAIL_NOT_VALID = "Email not valid"
    EMAIL_ALREADY_REGISTERED = "Email already registered"

    # 404 Not Found
    USER_NOT_FOUND = "User not found"


class zh_TW(error_exception):
    def __init__(self) -> None:
        super().__init__()
        self.EMAIL_ALREADY_REGISTERED = "信箱已被註冊"
        self.USER_NOT_FOUND = "用戶不存在"
        self.EMAIL_NOT_VALID = "非有效信箱"


class en_US(error_exception):
    def __init__(self) -> None:
        super().__init__()
