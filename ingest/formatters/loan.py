def format_row(row, lang="en"):
    from datetime import datetime

    # try:
    raw_date = str(row.get("Disbursement Date", "")).replace(".", "-").replace("/", "-")
    try:
        date = datetime.strptime(raw_date, "%Y-%m-%d")
        date_str = date.strftime("%Y년 %m월 %d일") if lang == "ko" else date.strftime("%B %d, %Y")
    except:
        date_str = raw_date

    borrower = row.get("Borrower ID", "").strip()
    product = row.get("Product type", "").strip()
    amount = str(row.get(" Loan Amount", "")).replace(",", "").strip()
    currency = row.get("Currency", "").strip()
    interest = str(row.get("Effective Interest Rate", "")).strip()
    term = str(row.get("Term", "")).strip()
    unit = row.get("Term Unit", "").strip()
    loan_type = row.get("Loan Type", "").strip()
    lender = row.get("Lender", "").strip()
    use = row.get("Loan Use", "").strip()

    unit_map = {"M": ("개월", "months"), "Y": ("년", "years"), "D": ("일", "days")}
    term_unit = unit_map.get(unit, (unit, unit))[0 if lang == "ko" else 1]

    if lang == "ko":
        return (
            f"{borrower} 고객은 {date_str}에 {currency} {int(amount):,} 금액의 {product} 상품 대출을 받았으며, "
            f"금리는 {interest}이고, {term}{term_unit} 동안 {loan_type} 방식으로 상환합니다. "
            f"이 대출은 {lender}에 의해 제공되었으며, 목적은 {use}입니다."
        )
    else:
        return (
            f"Borrower {borrower} received a {product} loan of {currency} {int(amount):,} on {date_str}, "
            f"with an effective interest rate of {interest}. The loan is to be repaid over {term} {term_unit} using the {loan_type} schedule. "
            f"It was provided by {lender}, and the purpose of the loan is '{use}'."
        )

    # except Exception as e:
    #     return f"[⚠️ Format error] {e}"
