"""
Another way of modifying the behaviour of a Python script (other than command line arguments) is to use **environment variables**.
Here is the expected behavior:

```bash
FLASK_ENV=development python flask_option.py
# => "Starting in development mode..."

FLASK_ENV=production python flask_option.py
# => "Starting in production mode..."

python flask_option.py
# => "Starting in empty mode..."
```
"""

import os

def start():
    """returns the right message"""
    env = os.getenv(key = 'FLASK_ENV', default="empty")

    return f"Starting in {env} mode..."


if __name__ == "__main__":
    print(start())
