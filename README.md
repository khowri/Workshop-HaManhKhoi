# Báo cáo thực tập Hạ Mạnh Khởi

Vietnam IT Job Market · AWS & Analytics

## Xem trên máy

Chạy các lệnh sau trong thư mục này bằng Hugo Extended 0.145.0.

~~~powershell
hugo server
~~~

Mở địa chỉ Hugo in ra, thường là http://localhost:1313/.

## Tạo bản tĩnh

~~~powershell
hugo --minify
~~~

Hugo xuất bản tĩnh vào thư mục public. Khi đưa lên hosting, đặt baseURL trong config.toml theo địa chỉ sẽ sử dụng. Workflow đi kèm build bằng Hugo Extended 0.145.0.

## Cập nhật trang chủ

Hai tệp trang chủ nằm trong content/_index.vi.md và content/_index.en.md. Ảnh chân dung nằm trong static/images/ha-manh-khoi.jpg.
