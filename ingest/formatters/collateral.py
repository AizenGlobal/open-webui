def format_row(row, lang="en"):
    loan_id = str(row.get("Loan ID", "")).strip()
    vehicle_type = str(row.get("Type", "")).strip()
    category = str(row.get("Category", "")).strip()
    appraisal_price = str(row.get(" Appraisal Price", "")).replace(",", "").strip()
    currency = str(row.get("Currency", "")).strip()

    if not appraisal_price.isdigit():
        row.get(" Appraisal Price", "")
        return f"[⚠️ Invalid Appraisal Price for {loan_id}]"

    if lang == "ko":
        return (
            f"대출번호 {loan_id}은 '{category}' 카테고리의 {vehicle_type}를 담보로 하며, "
            f"감정가는 {int(appraisal_price):,} {currency}입니다."
        )
    else:
        return (
            f"Loan ID {loan_id} is secured by a {vehicle_type} in the '{category}' category, "
            f"with an appraised value of {currency} {int(appraisal_price):,}."
        )
