import pandas


def clean_str(val):
    return str(val).strip() if not pandas.isna(val) else ""


def format_row(row, lang="ko"):
    from datetime import datetime

    try:
        raw_date = str(row.get("Scheduled Installment date", "")).replace(".", "-").replace("/", "-")
        date = datetime.strptime(raw_date, "%Y-%m-%d")
        date_str = date.strftime("%Y년 %m월 %d일") if lang == "ko" else date.strftime("%B %d, %Y")
    except:
        date_str = raw_date

    loan_id = row.get("Loan ID", "").strip()
    schedule_no = clean_str((row.get("Schedule Number", ""))).zfill(2)

    principal = clean_str(row.get("Scheduled Principal", "0")).replace(",", "")
    principal = float(principal) if principal else 0.0
    interest =clean_str(row.get("Scheduled Interest", "0")).replace(",", "")
    interest = float(interest) if interest else 0.0
    fees = clean_str(row.get("Scheduled Other Fees", "") or "").replace(",", "")
    fees = float(fees) if fees else 0.0
    tax = clean_str(row.get("Scheduled Tax", "0")).replace(",", "")
    tax = float(tax) if tax else 0.0

    if lang == "ko":
        base_sentence = (
            f"{loan_id}의 {schedule_no}회차는 {date_str}에 "
            f"원금 {principal:,.2f}원, 이자 {interest:,.2f}원"
        )
        if fees:
            base_sentence += f", 기타 수수료 {fees:,.2f}원"
        base_sentence += f", 세금 {tax:,.2f}원을 상환할 예정입니다."
        return base_sentence

    else:
        base_sentence = (
            f"For loan {loan_id}, installment #{schedule_no} is scheduled on {date_str} with "
            f"principal of {principal:,.2f}, interest of {interest:,.2f}"
        )
        if fees:
            base_sentence += f", other fees of {fees:,.2f}"
        base_sentence += f", and tax of {tax:,.2f}."
        return base_sentence