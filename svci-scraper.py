import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq # command to grab the page



# this program was built as part of my work with SVCI - in order to streamline my workload in data entry 

# Function to scrape company information from Crunchbase
def scrape_crunchbase_company(url):
    try:
        # Send a GET request to the Crunchbase URL
        #response = requests.get(url)
        
        uClient = uReq(url)
        # read the html page and save it inside a var, if you don't store, the html is dumped
        response = uClient.read()
        # close the connection
        uClient.close()

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content of the page using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract company information (you can modify this as needed)
            company_name = soup.find('h1', class_='component--field-formatter field-type-identifier-multi').text.strip()
            description = soup.find('span', class_='component--field-formatter field-type-markdown field-label-hidden').text.strip()
            headquarters = soup.find('div', class_='location-icon-2').find_next('span').text.strip()
            founders = soup.find('span', class_='wrappable-label-with-info ng-star-inserted').text.strip()
            website = soup.find('a', rel_='nofollow noopener noreferrer').text.strip()

            # Print the scraped information
            print("Company Name:", company_name)
            print("Description:", description)
            print("Headquarters:", headquarters)
            print("Founders: ", founders)
            print("Website: ", website)
        else:
            print("Couldn't retrieve the page. Status code:", response.status_code)

    except Exception as e:
        print("An error occurred:", str(e))

# URL of the Crunchbase page you want to scrape
crunchbase_url = "https://www.crunchbase.com/organization/databook"

# Call the scrape function with the URL
scrape_crunchbase_company(crunchbase_url)
