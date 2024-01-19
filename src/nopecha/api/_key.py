from re import compile

_gh_key_format = compile(r"[a-z\d]{16}")


def is_github_key(key: str) -> bool:
    return bool(_gh_key_format.fullmatch(key))
