def xpath_contains_text_ci(xpath_base: str, text: str) -> str:
    """
    Returns a case-insensitive XPath contains() expression.
    """
    return (
        f"{xpath_base}[contains("
        f"translate(normalize-space(.), "
        f"'ABCDEFGHIJKLMNOPQRSTUVWXYZ', "
        f"'abcdefghijklmnopqrstuvwxyz'), "
        f"'{text.lower()}')]"
    )

class SharedClass:
        pass
