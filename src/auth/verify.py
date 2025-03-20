import hashlib
import hmac

from src.auth.exception import AuthDataError
from src.settings import settings
from src.logger import logger


def verify_telegram_auth(data: dict):
    logger.debug(f"Верификация данных: {data}")

    if "hash" not in data:
        raise AuthDataError()
    
    received_hash = data.pop("hash")
    
    data_check_string = "\n".join(
        f"{key}={value}" for key, value in sorted(data.items())
    )

    secret_key = hashlib.sha256(settings.BOT_API_TOKEN.encode()).digest()

    calculated_hash = hmac.new(
        secret_key, 
        data_check_string.encode(), 
        hashlib.sha256
    ).hexdigest()

    if calculated_hash != received_hash:
        raise AuthDataError()

