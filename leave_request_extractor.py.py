import csv
import json


# Đọc email
def read_emails(input_file):
    emails = []
    with open(input_file, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            emails.append(row)
    return emails


# Lọc các email có liên quan đến "leave"
def filter_leave_requests(emails):
    leave_requests = []
    for email in emails:
        # Ghép subject + body để kiểm tra từ khóa
        content = (email["subject"] + " " + email["body"]).lower()
        if "leave" in content:
            leave_requests.append(
                {
                    "id": int(email["id"]),
                    "sender": email["sender"],
                    "type": "leave_request",
                }
            )
    return leave_requests


# Xuất kết quả ra file leave_request.json
def save_to_json(data, output_file):
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


# Main
def main():
    input_file = "emails.csv"
    output_file = "leave_request.json"

    # Đọc dữ liệu
    emails = read_emails(input_file)

    # Lọc email xin nghỉ phép
    leave_requests = filter_leave_requests(emails)

    # Xuất ra file JSON
    save_to_json(leave_requests, output_file)

    print(f"Đã xuất {len(leave_requests)} leave requests vào file {output_file}")


# Chạy chương trình
if __name__ == "__main__":
    main()
