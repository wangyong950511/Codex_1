from datetime import datetime


def days_between(date1: str, date2: str, fmt: str = "%Y-%m-%d") -> int:
    """Return the absolute number of days between two dates."""
    d1 = datetime.strptime(date1, fmt).date()
    d2 = datetime.strptime(date2, fmt).date()
    return abs((d2 - d1).days)


if __name__ == "__main__":
    start = input("请输入第一个日期(YYYY-MM-DD): ").strip()
    end = input("请输入第二个日期(YYYY-MM-DD): ").strip()
    print(f"两个日期之间相差 {days_between(start, end)} 天")
