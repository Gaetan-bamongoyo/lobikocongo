from itsdangerous import URLSafeSerializer

SECRET_KEY = 'admin243'

def encrypt_id(id):
    s = URLSafeSerializer(SECRET_KEY)
    return s.dumps(id)

def decrypt_id(encrypt_id):
    s = URLSafeSerializer(SECRET_KEY)
    return s.loads(encrypt_id)