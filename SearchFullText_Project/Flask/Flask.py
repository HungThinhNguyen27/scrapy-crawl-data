from flask import Flask, render_template, request
import mysql.connector

#Tạo một ứng dụng Flask.
app = Flask(__name__)

# Kết nối đến MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="kuynpi4187",
    database="vne_data"
)

# Khởi tạo con trỏ cho MySQL
mycursor = mydb.cursor()

@app.route('/')
def index():
    return render_template('index.html')

# Tìm kiếm dữ liệu từ MySQL
@app.route('/search', methods=['POST'])
def search():
    #lấy input
    search_keyword = request.form['search']
    
    #  Truy vấn  "MATCH AGAINST" để tìm kiếm với phương pháp toán tử logic BOOLEAN, 
    # ký tự %s  nó sẽ được thay thế bằng từ khóa tìm kiếm mà người dùng nhập vào trang web.
    query = "SELECT * FROM tablename WHERE MATCH(title) AGAINST (%s IN BOOLEAN MODE)"
    mycursor.execute(query, (search_keyword,))
    result = mycursor.fetchall()
    return render_template('results.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
