# --- IMPORTS PYTHON ---
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os

# --- PARAMÈTRES DE CONNEXION ---
USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")
ZIPCODE = os.environ.get("ZIPCODE")

# --- CONFIGURATION CHROME HEADLESS (sans interface graphique) ---
chrome_options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")
options.add_argument(f"--user-data-dir={tempfile.mkdtemp()}")  # profil temporaire

# --- LANCEMENT DU NAVIGATEUR ---
driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 10)
driver.get("https://m2.paybyphone.fr/login")

wait.until(EC.element_to_be_clickable((By.ID, "onetrust-reject-all-handler"))).click()

# --- CONNEXION ---
driver.find_element(By.ID, "username").send_keys(USERNAME)
driver.find_element(By.ID, "password").send_keys(PASSWORD)
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[span[text()='Se connecter']]"))).click()
driver.save_screenshot("debug.png")

# --- STATIONNEMENT ---
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='park-button']"))).click()
wait.until(EC.element_to_be_clickable((By.ID, "locationNumber"))).send_keys("75011", Keys.ENTER)
wait.until(EC.element_to_be_clickable((By.ID, "duration"))).send_keys("7", Keys.ENTER)
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='notNow-button']"))).click()
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='pay-button']"))).click()

time.sleep(120)
driver.quit()




