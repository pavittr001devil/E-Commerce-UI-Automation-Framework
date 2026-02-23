import os


class Config:
    # URLs
    BASE_URL = "https://automationexercise.com"
    LOGIN_URL = f"{BASE_URL}/login"

    # Timeouts (in milliseconds for Playwright)
    DEFAULT_TIMEOUT = 30000  # 30 seconds
    SMALL_TIMEOUT = 5000  # 5 seconds

    # Browser Settings
    BROWSER = "chromium"  # Can be changed to 'firefox' or 'webkit'
    HEADLESS = False  # Set to True for CI/CD pipelines (GitHub Actions)

    # Paths
    # This automatically finds your project root folder
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    DATA_DIR = os.path.join(ROOT_DIR, "testdata")
    LOGS_DIR = os.path.join(ROOT_DIR, "logs")