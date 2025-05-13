import random
import string

def generate_captcha():
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(6))

def verify_captcha(user_input, correct_answer):
    return user_input.lower() == correct_answer.lower()
