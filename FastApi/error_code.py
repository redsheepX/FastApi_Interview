class error_exception:
    # 200 OK
    SUCCESS = "success"

    # 400 Bad Request
    EMAIL_NOT_VALID = "Email not valid"
    EMAIL_ALREADY_REGISTERED = "Email already registered"
    DELETE_FAIL = "Delete fail"

    # 404 Not Found
    USER_NOT_FOUND = "User not found"
    FILE_NOT_FOUND = "File not found"


class zh_TW(error_exception):
    SUCCESS = "成功"

    EMAIL_NOT_VALID = "非有效信箱"
    EMAIL_ALREADY_REGISTERED = "信箱已被註冊"
    DELETE_FAIL = "刪除失敗"

    USER_NOT_FOUND = "用戶不存在"
    FILE_NOT_FOUND = "檔案不存在"


class en_US(error_exception):
    def __init__(self) -> None:
        super().__init__()
