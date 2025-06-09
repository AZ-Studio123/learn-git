# Quá trình biên dịch chương trình
- Quá trình tiền xử lý
- Quá trình dịch từ ngôn ngữ bậc cao sang bậc thấp (assembler)
- Dịch từ ngôn ngữ Assemble sang ngôn ngữ bậc thấp hơn (objectfile)
- Linker (liên kết thư viện động và thư viện tĩnh)
<div style="text-align: center;">
  <img src=".\img\image.png" alt="Compplier" width="500">
</div>

## Tiền xử lý
Giai đoạn này các file source code (đuôi .c; .h) sẽ được xử lý trước
- Các #include được xử lý: 
- Comment được loại bỏ
- define macro được xử lý bao gồm (define macro, define like funtion, define conditional,...) 
> Step của bước này : gcc -E main.c -o main.i<br>
Output của step này là -E tức Extended file<br>

Các file sau khi được xử lý sẽ có định dạng mở rộng, extended file có đuôi là (.i/.ii)
## Compie Dịch ngôn ngữ bậc cao sang ngôn ngữ bậc thấp 
Trình biên dịch sẽ dịch systax từ file mã nguồn đã được xử lý trước đó thành file mã nguồn assemble code. Trong quá trình này trình biên dịch sẽ tối ưu các cú pháp câu lệnh, và nếu có lỗi logic thì sẽ phát hiện được trong quá trình này. Mục đích là tối ưu mã nguồn<br>
Các trình biên dịch được dùng phổ biến trong quá trình này là gcc, g++. <br>
> Step của bước này : gcc -S main.c -o main.i<br>
Output của step này là -S dùng để biên dịch thành hợp ngữ<br>
Ngoài ra có thể chọn thêm các option tùy chỉnh của complier như -O2 **mức độ tối ưu hóa**, -std để chọn **chuẩn ngôn ngữ c99, c89,...**, -g tạo thông tin **gỡ lỗi va debug** trong file đầu ra, -Wall Bật tất cả **cảnh báo thông dụng** của gcc, -pedantic tuân thủ theo chuẩn **ISO C/C++**...
- Ví dụ biên dịch đầy đủ hiển thị cảnh báo và chuẩn ISO: 
    + gcc -Wall -O2 -std=c99 -pedantic -Iinclude -o main main.c math.c -lm

Sau khi dã được dịch xong file mã nguồn lúc này sẽ mang cấu trúc của mã assembly và có đuôi tệp là (.s)
##  Dịch từ ngôn ngữ Assembly code sang ngôn ngữ máy Machine code
Ở bước này thì assembler sẽ chuyển đổi mã assembly code thành mã máy (Mã mà CPU có thể hiểu được). assemblẻ phục thuộc vào cấu trúc CPU để tối ưu mã trên phần cứng (x64, x86, ARM),...
> as main.s -o main.o<br>
Output của file này là main.o với nội dung chứa các object code mà máy tính có thể hiểu được

Bước này đơn giản là dịch từ assembly code sang mã máy. Các tệp lúc này sẽ được lưu dưới dạng machine code (.o, .object)
## Giai đoạn liên kết
Giai đoạn này trình liên kết sẽ liên kết các file object lại với nhau và liên kết với các thư viện để tạo ra 1 file thực thi duy nhất.
- Có 2 kiểu liên kết:
    + Liên kết tĩnh <br>
    Liên kết tĩnh là các hàm được sử dụng trong thư viện sẽ được sao chép vào các object code trong quá trình complie
    + Liên kết động <br>
    Đặt tên của thư viện trong file object và linking trong quá trình complie
- Liên kết tĩnh:
    + Quá trình này thư viện sẽ được copy vào trong chương trình chính, như vậy thư viện sẽ luôn nằm trong chương trình của mình trong suốt quá trình run
    + Ưu điểm của việc này là vì thư viện đã có sẵn trong ứng dụng mà mình build vì thế tốc độ chạy của chương trình sẽ nhanh hơn
    + Nhược điểm là vì thư viện được copy vào file chương trình nên kích cõ của ứng dụng sẽ lớn gây chiếm bộ nhớ. 
    + Vì thư viện được thêm vào cùng với ứng dụng nên khi muốn chỉnh sửa thư viện hay trong ứng dụng thì phải rebuild lại toàn bộ chương trình.
<div style="text-align: center;">
    <img src =".\img\Linking.jpg" alt= " Linking" width = "500">
</div>

- Liên kết động:
    + Liên kết động là đợi quá trình linking hoàn tất, khi chạy chương trình thì file thư viện mới được load vào bộ nhớ
    + Khi chạy chương trình trong file object code sẽ có vùng để báo hiệu rằng cần link tới thư viện cần thiết và thư viện sẽ được link trong suốt quá trình chạy.
    + Ưu điểm : Vì thư viện nằm tách biệt so với chương trình chính nên khi cần sửa đổi thư viện thì chỉ cần rebuild lại thư viện ,
    + Tối ưu bộ nhớ hơn nhưng tốc độ thực thi sẽ chậm hơn.<br>
- Cuối cùng sẽ tạo ra một file có thể thực thi được vs như .exe trên windows, hex, srec để nạp xuống vi điều khiển.

## Các lỗi thường gặp khi biên dịch
- Thiếu header file: Thường xuất hiện lỗi như "fatal error: foo.h No such file or directory" nguyên nhanh do gcc không tìm thấy file header trên đường dẫn mặc định. Giải pháp kiểm tra lại đường dẫn hoặc thêm thư mục chứa file header bằng -I trong quá trình complie
- Các lỗi cảnh báo nếu có dùng Flag cảnh bảo như -Wall -Werror.
- Vi phạm chuẩn ngôn ngữ nếu biên dịch dùng chuẩn ISO và chuẩn phiên bản -std thì có thể có các lỗi liên quan đến từ khóa hoặc cú pháp . Giải pháp, sửa lại theo chuẩn .
- Debug chương trình: khi chạy chương trình debug mà chương trình không cán qua break point có thể là do chưa thêm symbol -g để có thông tin debug chi tiết của trình gỡ lỗi, thêm -g giúp cho gdb theo dõi và sửa lỗi hiệu quả.


