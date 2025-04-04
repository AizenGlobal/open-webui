import pandas as pd

def clean_str(val):
    return str(val).strip() if not pd.isna(val) else ""

def format_row(row, lang="ko"):
    from datetime import datetime

    try:
        raw_date = str(row.get("Actual payment date", "")).replace(".", "-").replace("/", "-")
        date = datetime.strptime(raw_date, "%Y-%m-%d")
        date_str = date.strftime("%Y년 %m월 %d일") if lang == "ko" else date.strftime("%B %d, %Y")
    except:
        date_str = raw_date

    loan_id = clean_str(row.get("Loan ID"))
    schedule_no = clean_str(row.get("Schedule")).zfill(2)

    principal = clean_str(row.get("Actual Principal", "0")).replace(",", "")
    interest = clean_str(row.get("Actual Interest", "0")).replace(",", "")
    fees = clean_str(row.get("Actual Other Fees", "0")).replace(",", "")
    vat = clean_str(row.get("Actual Interest VAT", "0")).replace(",", "")
    late_fee = clean_str(row.get("Late Fee & Other Charges", "0")).replace(",", "")

    # 숫자 변환
    principal = float(principal) if principal else 0.0
    interest = float(interest) if interest else 0.0
    fees = float(fees) if fees else 0.0
    vat = float(vat) if vat else 0.0
    late_fee = float(late_fee) if late_fee else 0.0

    if lang == "ko":
        sentence = (
            f"{loan_id}의 {schedule_no}회차는 {date_str}에 "
            f"원금 {principal:,.2f}원, 이자 {interest:,.2f}원"
        )
        if fees:
            sentence += f", 기타 수수료 {fees:,.2f}원"
        if vat:
            sentence += f", 이자 VAT {vat:,.2f}원"
        if late_fee:
            sentence += f", 연체료 및 기타 {late_fee:,.2f}원"
        sentence += "을 납부하였습니다."
        return sentence

    else:
        sentence = (
            f"For loan {loan_id}, installment #{schedule_no} was paid on {date_str} with "
            f"principal of {principal:,.2f}, interest of {interest:,.2f}"
        )
        if fees:
            sentence += f", other fees of {fees:,.2f}"
        if vat:
            sentence += f", VAT on interest of {vat:,.2f}"
        if late_fee:
            sentence += f", and late fees or other charges of {late_fee:,.2f}"
        sentence += "."
        return sentence
