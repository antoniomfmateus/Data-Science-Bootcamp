import os

def start():
    """returns the right message"""
    env = os.getenv(key = 'FLASK_ENV', default="empty")

    return f"Starting in {env} mode..."


if __name__ == "__main__":
    print(start())
