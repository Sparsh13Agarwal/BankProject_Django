import base64
from .models import Credential

def hash_password(password):
    sample_string_bytes = password.encode("ascii")
    base64_bytes = base64.b64encode(sample_string_bytes)
    base64_string = base64_bytes.decode("ascii")

    return base64_string

def unhash_password(customer_id,password):
    credentials = Credential.objects.all().values()
    for credential in credentials:
        if credential['customer_id_id'] == customer_id:
            base64_bytes = credential['password'].encode("ascii")
            sample_string_bytes = base64.b64decode(base64_bytes)
            sample_string = sample_string_bytes.decode("ascii")
            if sample_string == password:
                return True
    return False