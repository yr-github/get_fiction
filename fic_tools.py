def bytes_to_str(bytes):
    if isinstance(bytes,str):
        return bytes
    else:
        return bytes.decode("utf-8")

def str_to_bytes(str):
    if isinstance(str,bytes):
        return str
    else:
        return str.encode("utf-8")