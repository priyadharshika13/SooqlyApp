# promote_admin.py
from app.db import SessionLocal
from app.models import User
db = SessionLocal()
u = db.query(User).filter(User.email=="admin@sooqly.app").first()
if not u:
    print("User not found. Create one via /auth/register first.")
else:
    u.role = "admin"
    db.commit()
    print("Promoted:", u.email, "-> admin")
