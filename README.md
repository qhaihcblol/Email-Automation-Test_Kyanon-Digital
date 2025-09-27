# Mini Workflow - Email Leave Request Extractor

## Giới thiệu
Đây là chương trình Python nhỏ dùng để:
- Đọc dữ liệu email từ file CSV.
- Lọc ra các email liên quan đến đơn xin nghỉ phép (leave request).
- Xuất kết quả ra file JSON với cấu trúc gọn gàng, dễ xử lý tiếp theo.

Bài tập được thực hiện trong khuôn khổ **AI/Automation Intern - Entrance Assessment**.

---

## Cấu trúc dữ liệu đầu vào
File `emails.csv` có dạng:

```csv
id,sender,subject,body
1,alice@company.com,Leave request,"I would like to take leave on 2025-09-28"
2,bob@company.com,IT issue,"My laptop cannot connect to wifi"
3,charlie@client.com,New leave request,"I would like to take day off on 2025-09-30"
```

---

## Kết quả đầu ra
File `leave_request.json` có dạng:

```json
[
  {"id": 1, "sender": "alice@company.com", "type": "leave_request"},
  {"id": 3, "sender": "charlie@client.com", "type": "leave_request"}
]
```

---

## Cách chạy chương trình

1. Cài đặt Python (phiên bản 3.8 trở lên).  
2. Đảm bảo có file `emails.csv` đặt cùng thư mục với script Python.  
3. Chạy lệnh sau trong terminal:

```bash
python leave_request_extractor.py
```

4. Sau khi chạy, chương trình sẽ tạo file `leave_request.json` chứa danh sách các email xin nghỉ phép.

---

## Giải thích code
- `read_emails()` : Đọc dữ liệu từ file CSV.  
- `filter_leave_requests()` : Lọc các email có chứa từ khóa "leave" trong subject hoặc body.  
- `save_to_json()` : Ghi dữ liệu kết quả ra file JSON.  
- `main()` : Gọi toàn bộ quy trình.  
