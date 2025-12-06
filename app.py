from flask import Flask
from core.db_singleton import DatabaseConnection
from controllers.auth_controller import auth_bp  # استدعاء الكنترولر

app = Flask(__name__)

# تسجيل ملفات التحكم (عشان الروابط تشتغل)
app.register_blueprint(auth_bp)

@app.route("/")
def home():
    return """
    <div style="text-align: center; padding-top: 50px;">
        <h1 style="color: green;">WASET Backend is Online! 🚀</h1>
        <p>Database Connection: <strong style="color: blue;">Active</strong></p>
        <hr>
        <p>Use Postman or Browser to test routes.</p>
    </div>
    """

if __name__ == "__main__":
    # تشغيل الاتصال بالداتا بيز مرة واحدة عند البداية
    print("🔄 Initializing Database Connection...")
    db = DatabaseConnection()
    
    app.run(debug=True)