def validate_amount(amount):
    try:
        amount = float(amount)
        return amount > 0
    except:
        return False


def validate_date(date):
    from datetime import datetime
    try:
        datetime.strptime(date, "%Y-%m-%d")
        return True
    except:
        return False