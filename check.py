def check(exp: bool, err_msg: str, msg2: str = "out of range") -> None:
    if not exp:
        print(f"Type failure: {err_msg} {msg2}")
