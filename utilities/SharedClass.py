import time, random

def xpath_contains_text_ci(xpath_base: str, text: str) -> str:
    """
    :param xpath_base: xpath
    :param text: text to be looked for
    :return: a case-insensitive XPath contains() expression.
    """
    return (
        f"{xpath_base}[contains("
        f"translate(normalize-space(.), "
        f"'ABCDEFGHIJKLMNOPQRSTUVWXYZ', "
        f"'abcdefghijklmnopqrstuvwxyz'), "
        f"'{text.lower()}')]"
    )

def random_sleep(min_s=1, max_s=5):
    """
    to simulate human response
    :param min_s: minimum time to sleep
    :param max_s: maximum time to sleep
    """
    time.sleep(random.uniform(min_s, max_s))

class SharedClass:
        pass
