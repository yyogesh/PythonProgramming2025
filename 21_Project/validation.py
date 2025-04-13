import re


def validate_email(email):
    """Check if email is valid"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def validate_phone(phone):
    """Check if phone number is valid"""
    pattern = r'^\+?[\d\s-]{10,15}$'
    return re.match(pattern, phone) is not None


def format_phone(phone):
    """Format phone number consistently"""
    digits = re.sub(r'[^\d]', '', phone)
    if len(digits) == 10:
        return f"{digits[:3]}-{digits[3:6]}-{digits[6:]}"
    return phone