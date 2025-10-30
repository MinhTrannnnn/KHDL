# Solar Energy Analysis Vietnam 🌞

Phân tích bức xạ mặt trời và tiềm năng năng lượng mặt trời tại Việt Nam (2015-2024)

## 📊 Giới thiệu

Dự án phân tích dữ liệu năng lượng mặt trời từ NASA POWER API cho 12 tỉnh thành Việt Nam trong giai đoạn 2015-2024.

## 🚀 Deploy lên Streamlit Cloud

### Bước 1: Chuẩn bị GitHub Repository

1. **Tạo repository mới trên GitHub:**
   - Truy cập https://github.com/new
   - Đặt tên repository (ví dụ: `solar-energy-vietnam`)
   - Chọn Public
   - Click "Create repository"

2. **Push code lên GitHub:**

```bash
cd D:\ML\KHDL\Giuaky

# Khởi tạo git (nếu chưa có)
git init

# Thêm remote repository
git remote add origin https://github.com/YOUR_USERNAME/solar-energy-vietnam.git

# Thêm tất cả file
git add app_solar.py requirements.txt solar_monthly_vietnam_full.csv solar_annual_vietnam_full.csv README.md

# Commit
git commit -m "Initial commit: Solar Energy Analysis App"

# Push lên GitHub
git branch -M main
git push -u origin main
```

### Bước 2: Deploy trên Streamlit Cloud

1. **Truy cập Streamlit Cloud:**
   - Vào https://share.streamlit.io/
   - Đăng nhập bằng tài khoản GitHub

2. **Tạo app mới:**
   - Click "New app"
   - Chọn repository: `YOUR_USERNAME/solar-energy-vietnam`
   - Branch: `main`
   - Main file path: `app_solar.py`
   - Click "Deploy"

3. **Chờ deploy:**
   - Quá trình deploy mất khoảng 2-5 phút
   - App sẽ tự động cài đặt các thư viện từ `requirements.txt`

### Bước 3: Chia sẻ

Sau khi deploy thành công, bạn sẽ nhận được link dạng:
```
https://YOUR_USERNAME-solar-energy-vietnam-app-solar-XXXXX.streamlit.app
```

Bạn có thể chia sẻ link này với bất kỳ ai!

## 📁 Cấu trúc file

```
Giuaky/
├── app_solar.py                        # Main Streamlit app
├── requirements.txt                    # Python dependencies
├── solar_monthly_vietnam_full.csv      # Dữ liệu theo tháng
├── solar_annual_vietnam_full.csv       # Dữ liệu theo năm
├── bucxa.ipynb                         # Notebook phân tích (không cần deploy)
└── README.md                           # Hướng dẫn
```

## 🔧 Chạy local

```bash
pip install -r requirements.txt
streamlit run app_solar.py
```

## 📊 Nguồn dữ liệu

- NASA POWER API (2015-2024)
- 12 tỉnh thành Việt Nam đại diện cho các vùng khí hậu khác nhau

## 👨‍💻 Tác giả

Dự án phân tích Khoa học Dữ liệu

