import pytest_check as check  # type: ignore
from re import compile


class TestLog:
    def test_log(self):
        with open("../python_education/files/service.log", "r") as file_log:
            found_lines = 0
            pattern_ip_port = compile(r"(?:[0-9]{1,3}\.){3}[0-9]{1,3}:\d{1,5}")
            for line in file_log:
                if "HTTP" in line and "command test_1 was executed successfully" in line:
                    found_lines += 1
                    check.is_in("info", line)
                    check.is_in("code", line)
                    check.is_true(pattern_ip_port.search(line))
                elif "HTTP" in line and "command test_2 was executed successfully" in line:
                    found_lines += 1
                    check.is_in("info", line)
                    check.is_in("code", line)
                    check.is_true(pattern_ip_port.search(line))
                elif "Shell" in line and "command test_1 was executed successfully" in line:
                    found_lines += 1
                    check.is_in("info", line)
                    check.is_in("code", line)
            assert found_lines == 3, f"Найдено {found_lines} строк с кодом code, ожидалось 3"
