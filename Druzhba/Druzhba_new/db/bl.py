import asyncio
import json
from datetime import date
from enum import Enum
from json import JSONDecodeError

from sqlalchemy import select, func

# **********************************************************************
# Call from backend
# **********************************************************************
class UserStatus(Enum):
    """
    Статус пользователя
    """
    Visitor = 0  # новый посетитель
    TrialUser = 1  # пользователь без оплаты
    User = 2  # пользователь
    Admin = 3  # админ компании, управляет аккаунтом компании
    Donor = 5  # зарегистрированный донор (спонсор)
    AnonymousDonor = 6  # анонимный донор (спонсор)
    DonationCheaf = 7  # отвественный за сбор DonationCheaf
    Unknown = 12  # фиг его знает, кто это такой
