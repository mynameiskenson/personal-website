import hashlib

def gravatar_url(email, size=100, default="retro", rating="g"):
    email = (email or "").strip().lower().encode("utf=8")
    hash_email = hashlib.md5(email).hexdigest()
    return f"https://www.gravatar.com/avatar/{hash_email}?s={size}&d={default}&r={rating}"