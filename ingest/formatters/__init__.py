

def get_formatter(data_type: str, lang: str):
    key = f"{data_type.lower()}_{lang.lower()}"

    formatter_map = {
        "loan_en": "loan",
        "loan_ko": "loan",
        "borrower_en": "borrower",
        "borrower_ko": "borrower",
        "collateral_en": "collateral",
        "collateral_ko": "collateral",
        "expectedpayment_en": "expectedPayment",
        "expectedpayment_ko": "expectedPayment",
        "actualpayment_en": "actualPayment",
        "actualpayment_ko": "actualPayment",
    }

    if key not in formatter_map:
        raise ValueError(f"No formatter found for type '{data_type}' and language '{lang}'")

    module_name = formatter_map[key]
    module = __import__(f"formatters.{module_name}", fromlist=["format_row"])
    return module
