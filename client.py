# load additional Python modules
import socket
import json
import traceback


def send_ipc(function_name, status, error_message=None, error_type=None):
    """
    Write Message to pipes
    """
    assert (error_type in ["WARNING", "CRITICAL", "INFO"]
            or error_type is None), "Unknown Error Type"

    if error_type in ["WARNING", "CRITICAL", "INFO"]:
        text = {"FUNCION": function_name, "STATUS": status,
                "ERROR": traceback.format_exc(),
                "ERROR_TYPE": error_type}
    else:
        text = {"FUNCION": function_name, "STATUS": status,
                "ERROR": error_message,
                "ERROR_TYPE": error_type}
    try:
        content = f"{text}".encode("utf8")
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        local_hostname = socket.gethostname()
        ip_address = socket.gethostbyname(local_hostname)
        server_address = (ip_address, 23456)
        print("Sending DATA : ", text)
        sock.connect(server_address)
        sock.sendall(content)
    except Exception as e:
        print(f"Exception occured {e}")
    sock.close()
    return "DATA SEND"

for i in range(0, 10):
    print(send_ipc("function_name", f"TESTING {i}", error_message=None, error_type=None))