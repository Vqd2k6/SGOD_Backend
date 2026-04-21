# SGOD Backend (Mock API)

Dự án này là một Backend giả lập (Mock API) được xây dựng bằng **FastAPI**, nhằm phục vụ việc phát triển và kiểm thử giao diện (Frontend) cho dự án SGOD - Smart Generation of Digital.

##  Tính năng chính
- Cung cấp dữ liệu JSON cho các section: Tin tức, Blog, Đội ngũ nhân sự, Thông tin công ty.
- Xử lý gửi form liên hệ (Mock).
- Tài liệu API tự động (Swagger UI).
- Cấu hình linh hoạt qua file `.env`.

##  Cài đặt và Chạy

### 1. Yêu cầu hệ thống
- Python 3.9+
- Virtual Environment (khuyên dùng)

### 2. Các bước cài đặt
1. Giải nén/Clone project.
2. Tạo môi trường ảo:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # macOS/Linux
   # hoặc
   .venv\Scripts\activate     # Windows
   ```
3. Cài đặt thư viện:
   ```bash
   pip install -r requirements.txt
   ```
4. Cấu hình môi trường:
   - Sao chép file `.env.example` thành `.env`.
   - Chỉnh sửa các thông số như `PORT`, `ALLOWED_ORIGINS` nếu cần.

### 3. Chạy Server
```bash
python -m app.main
```
Server sẽ mặc định chạy tại: `http://127.0.0.1:8000`

---

##  Danh sách API (Endpoints)

Tài liệu chi tiết có thể xem tại: `http://127.0.0.1:8000/docs`

### 1. Thông tin Công ty (`/api/company`)
- `GET /api/company/vision`: Lấy dữ liệu Tầm nhìn.
- `GET /api/company/mission`: Lấy dữ liệu Sứ mệnh.
- `GET /api/company/products`: Danh sách các sản phẩm/dịch vụ.
- `GET /api/company/contact-info`: Thông tin liên hệ cơ bản (địa chỉ, email, hotline).

### 2. Tin tức & Blog (`/api/news` & `/api/blog`)
- `GET /api/news`: Danh sách các slide cho banner tin tức.
- `GET /api/blog`: Danh sách các bài viết blog.
  - Query params: `category` (AI, Blockchain, Security), `search` (từ khóa tiêu đề).
- `GET /api/blog/{id}`: Chi tiết một bài viết blog.

### 3. Đội ngũ nhân sự (`/api/team`)
- `GET /api/team`: Danh sách toàn bộ thành viên.
- `GET /api/team/{id}`: Thông tin chi tiết một thành viên.

### 4. Liên hệ (`/api/contact`)
- `POST /api/contact`: Gửi form liên hệ (Gửi lên Name, Email, Message).

### 5. Hệ thống
- `GET /health`: Kiểm tra trạng thái hoạt động của server.

---

##  Cấu trúc thư mục
- `app/data/`: Chứa các file JSON dữ liệu mock.
- `app/routers/`: Định nghĩa các endpoints.
- `app/schemas/`: Định nghĩa kiểu dữ liệu (Pydantic models).
- `app/services/`: Logic xử lý dữ liệu và đọc file JSON.
