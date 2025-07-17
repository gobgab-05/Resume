# นำเข้า Flask และฟังก์ชันที่ใช้แสดงหน้า HTML
from flask import Flask, render_template

# สร้างแอป Flask
app = Flask(__name__)

# สร้าง route สำหรับหน้าแรกของเว็บ ("/")
@app.route("/")
def resume():
    """
    ฟังก์ชันสำหรับแสดงหน้า resume (resume.html)
    """
    return render_template("resume.html")

# รันแอปเมื่อเปิดไฟล์นี้โดยตรง
if __name__ == "__main__":
    # เปิด debug mode: เหมาะสำหรับใช้ตอนพัฒนา
    app.run(debug=True)
