import pandas


def clean_str(val):
    return str(val).strip() if not pandas.isna(val) else ""


def format_row(row, lang="en"):
    borrower_id = clean_str(row.get("Borrower ID"))
    company_name = clean_str(row.get("Company Name"))
    year = clean_str(row.get("Birth/Creation year"))
    income = clean_str(row.get("Income/Revenues"))
    industry = clean_str(row.get("Industry/Occupation"))
    num_dependents = clean_str(row.get("Number of Dependents/Employees"))
    country = clean_str(row.get("Country"))
    city = clean_str(row.get("State/Province/City"))
    settlement = clean_str(row.get("Settlement Type"))

    if lang == "ko":
        return (
            f"{borrower_id} 대출자는 '{company_name}'이라는 이름의 법인으로, "
            f"{country} {city}에 위치해 있습니다."
            f"{year + '년에 설립되었으며, ' if year else ''}"
            f"{industry + ' 업종에 종사합니다. ' if industry else ''}"
            f"{income + '의 수익을 올리고 있으며, ' if income else ''}"
            f"{num_dependents + '명의 직원이 있고, ' if num_dependents else ''}"
            f"{settlement + ' 지역에 위치해 있습니다.' if settlement else ''}"
        ).strip()
    else:
        return (
            f"Borrower ID {borrower_id} refers to a legal entity named '{company_name}', "
            f"located in {city}, {country}. "
            f"{'Established in ' + year + '. ' if year else ''}"
            f"{'Operates in the ' + industry + ' sector. ' if industry else ''}"
            f"{'Reports revenue of ' + income + '. ' if income else ''}"
            f"{'Employs ' + num_dependents + ' people. ' if num_dependents else ''}"
            f"{'Situated in a ' + settlement + ' area.' if settlement else ''}"
        ).strip()