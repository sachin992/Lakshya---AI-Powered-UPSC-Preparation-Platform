# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from bs4 import BeautifulSoup
# import pandas as pd
# import time

# # URL to scrape
# url = 'https://www.myscheme.gov.in/search/state/Bihar'

# # Setup Chrome options
# options = webdriver.ChromeOptions()
# options.add_argument('--disable-blink-features=AutomationControlled')
# options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36')
# # Uncomment the line below to run in headless mode (no browser window)
# # options.add_argument('--headless')

# # Initialize driver
# driver = webdriver.Chrome(options=options)

# try:
#     print("Loading page...")
#     driver.get(url)
    
#     # Wait for data to load - adjust the selector and timeout as needed
#     # Look for table, div with schemes, or any container with data
#     print("Waiting for content to load...")
    
#     # Try waiting for common elements (adjust selector based on actual page)
#     try:
#         WebDriverWait(driver, 15).until(
#             EC.presence_of_all_elements_located((By.TAG_NAME, "tr"))
#         )
#     except:
#         print("Timeout waiting for tables, trying alternative selectors...")
    
#     # Give JS time to fully render
#     time.sleep(3)
    
#     # Get page source after JS renders
#     page_source = driver.page_source
#     soup = BeautifulSoup(page_source, 'html.parser')
    
#     # Look for tables
#     tables = soup.find_all('table')
#     print(f"Found {len(tables)} table(s)")
    
#     if tables:
#         all_data = []
        
#         for table_idx, table in enumerate(tables):
#             print(f"\nProcessing table {table_idx + 1}...")
            
#             # Get headers
#             headers = []
#             for th in table.find_all('th'):
#                 headers.append(th.get_text(strip=True))
            
#             # Get rows
#             rows = []
#             for tr in table.find_all('tr')[1:]:  # Skip header row
#                 cols = tr.find_all('td')
#                 row = [col.get_text(strip=True) for col in cols]
#                 if row and any(row):  # Only add non-empty rows
#                     rows.append(row)
            
#             if headers and rows:
#                 df = pd.DataFrame(rows, columns=headers)
#                 all_data.append(df)
#                 print(f"Extracted {len(rows)} rows from table {table_idx + 1}")
#                 print(df.head())
        
#         if all_data:
#             # Combine all tables if multiple exist
#             combined_df = pd.concat(all_data, ignore_index=True)
#             combined_df.to_csv('bihar_temp_schemes.csv', index=False, encoding='utf-8')
#             print(f"\n✓ Total rows saved: {len(combined_df)}")
#             print("✓ Data saved to 'bihar_temp_schemes.csv'")
#         else:
#             print("No table data found")
#     else:
#         print("No tables found. Checking for divs or other containers...")
#         # Look for divs with scheme data
#         divs = soup.find_all('div')
#         print(f"Found {len(divs)} divs. Inspecting page structure...")
#         print("\nPage HTML snippet:")
#         print(soup.prettify()[:1000])

# except Exception as e:
#     print(f"Error: {e}")
#     import traceback
#     traceback.print_exc()

# finally:
#     driver.quit()
#     print("\nBrowser closed.")


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import time
import json

# URL to scrape
url = 'https://www.myscheme.gov.in/search/state/Bihar'

# Setup Chrome options
options = webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36')
# Uncomment for headless mode
# options.add_argument('--headless')

driver = webdriver.Chrome(options=options)

try:
    print("Loading page...")
    driver.get(url)
    
    print("Waiting for content to load...")
    time.sleep(5)
    
    # Get page source after JS renders
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')
    
    # Look for scheme cards/divs (common patterns)
    scheme_divs = soup.find_all('div', class_=lambda x: x and any(keyword in x.lower() for keyword in ['scheme', 'card', 'item', 'grid']))
    
    print(f"Found {len(scheme_divs)} potential scheme containers\n")
    
    schemes = []
    
    # Extract data from divs
    for div in scheme_divs[:20]:  # Sample first 20 to see structure
        text = div.get_text(strip=True)
        if text and len(text) > 10:  # Filter out empty divs
            # Extract links
            links = div.find_all('a')
            scheme_name = div.get_text(strip=True)
            scheme_url = links[0].get('href', '') if links else ''
            
            scheme_data = {
                'scheme_name': scheme_name,
                'scheme_url': scheme_url,
                'description': text[:200]  # First 200 chars as description
            }
            
            if scheme_data not in schemes:  # Avoid duplicates
                schemes.append(scheme_data)
                print(f"Found: {scheme_name[:60]}")
    
    if schemes:
        df = pd.DataFrame(schemes)
        df.to_csv('bihar_schemes.csv', index=False, encoding='utf-8')
        print(f"\n✓ Total schemes extracted: {len(df)}")
        print("✓ Data saved to 'bihar_schemes.csv'")
        print("\nSample data:")
        print(df.head())
    else:
        print("No scheme data found with common selectors.")
        print("\nTrying to find data in JSON format or script tags...")
        
        # Look for JSON data in script tags
        scripts = soup.find_all('script', type='application/json')
        if scripts:
            print(f"Found {len(scripts)} JSON script tags")
            for idx, script in enumerate(scripts[:3]):
                try:
                    data = json.loads(script.string)
                    print(f"\nScript {idx} contains: {list(data.keys())}")
                except:
                    pass
        
        # Print HTML structure for inspection
        print("\n\nHTML Structure (first 2000 chars):")
        print(soup.prettify()[:2000])

except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()

finally:
    driver.quit()
    print("\nBrowser closed.")