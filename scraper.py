# Import libraries

from bs4 import BeautifulSoup
import requests

# This header is to bypass CAPCHA
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

# Dataframe headers
df_headers = ["Name", "Mileage", "Address", "Rating", "Fuel Type", "City MPG",
              "Highway MPG", "Drivetrain", "Engine", "Exterior Color", "Interior Color",
              "Transmission", "Entertainment", "Safety", "Price"]


# Create the function to get all urls of 1 page

def get_one_page_urls(page_link):
    """
    ----------------------------
    Get all item's urls that are listed in one page
    ----------------------------
    Parameter: the link to our desired page
    ----------------------------
    Return: The list of all item's urls that are listed in the page

    """

    response = requests.get(page_link, headers=header)

    data = response.text

    soup = BeautifulSoup(data, "html.parser")

    one_page_urls = []

    # Loop through all the items inside the listing container of the html page
    # and find the link (href) inside the anchor tag and append it
    # into the list. Since the link is shortened, we have to put it
    # after the main url (https://www.cars.com/)

    for i in range(len(soup.find_all(class_="shop-srp-listings__listing-container"))):
        url = soup.find_all(class_="shop-srp-listings__listing-container")[i].find('a')['href']
        one_page_urls.append(f"https://www.cars.com/{url}")

    return one_page_urls


def get_all_urls(start_page, num_of_pages, radius, zipcode):
    """
    ----------------------------
    Get all wanted urls based on the specific area.
    ----------------------------
    Parameters: the staring page, the number of pages we want to loop through,
    the radius from the center of the zipcode, the area's zipcode.
    ----------------------------
    Return: The list of all item's urls.

    """

    all_urls_list = []

    for i in range(num_of_pages):
        # Define the root url and pass in 3 parameters: start_page, num_of_pages, zipcode
        root_url = "https://www.cars.com/for-sale/searchresults.action/?page={}&perPage=100&rd={}&searchSource=GN_BREADCRUMB&sort=relevance&zc={}".format(
            i + start_page, radius, zipcode)

        # Append all urls to the list
        all_urls_list.append(get_one_page_urls(root_url))

    # Depends on how many pages we loop through, we will get the list with that
    # many sublists inside of all_urls_list. We want the function to return
    # one single list, so we use list comprehension.
    all_urls = [item for sub_list in all_urls_list for item in sub_list]

    return all_urls


def get_car_features(url):
    """
    ----------------------------
    Get car's features based on the car's url
    ----------------------------
    Parameters: the url that is linked to the item.
    ----------------------------
    Return: The list of dictionaries where the keys are the features and the values are the features' values.

    """
    cars_list = []

    response = requests.get(url, headers=header)

    data = response.text

    soup = BeautifulSoup(data, "html.parser")

    # Navigate to the basic features containers and grab all of them, put them in a list
    basic_features = soup.find_all('li', class_='vdp-details-basics__item')
    basic_feature_list = []

    for i in range(len(basic_features)):
        basic_feature_list.append(soup.find_all('li', class_='vdp-details-basics__item')[i].text.strip().split(':'))

    # Navigate to the extra features container and grab all of them, put them in a list
    extra_features = soup.find_all(class_='details-feature-list details-feature-list--normalized-features')
    extra_feature_list = []
    for i in range(len(extra_features)):
        extra_feature_list.append(
            soup.find_all(class_='details-feature-list details-feature-list--normalized-features')[
                i].text.strip().split('\n\n'))

    # Sort through the structure of the page to and grab features
    name = soup.find('h1', class_='cui-heading-2--secondary vehicle-info__title').text
    mileage = soup.find(class_='vdp-cap-price__mileage--mobile vehicle-info__mileage mileage_margin').text.split(" ")[0]
    address = soup.find(class_='get-directions-link seller-details-location__text').text.strip()
    rating = soup.find(class_='rating__link rating__link--has-reviews').text.split('(')[1].split(')')[0]

    # Define default values for these features in case any of them missing from specific item's page
    # the default value will be -1
    fuel_type = -1
    city_MPG = -1
    highway_MPG = -1
    drivetrain = -1
    engine = -1
    exterior_color = -1
    interior_color = -1
    transmission = -1
    entertainment = -1
    safety = -1
    price = soup.find(class_='vehicle-info__price-display vehicle-info__price-display--dealer cui-heading-2').text

    # Loop through the basic feature list and assign value for each of them
    for basic in basic_feature_list:
        if basic[0] == "Fuel Type":
            fuel_type = basic[1]
        if basic[0] == 'City MPG':
            city_MPG = basic[1].split(" ")[1]
        if basic[0] == 'Highway MPG':
            highway_MPG = basic[1].split(" ")[1]
        if basic[0] == 'Drivetrain':
            drivetrain = basic[1]
        if basic[0] == 'Engine':
            engine = basic[1]
        if basic[0] == 'Exterior Color':
            exterior_color = basic[1]
        if basic[0] == 'Interior Color':
            interior_color = basic[1]
        if basic[0] == 'Transmission':
            transmission = basic[1]

    # Same for extra feature
    for extra in extra_feature_list:
        if extra[0] == "Entertainment":
            entertainment = extra[1].split('\n')
        if extra[0] == "Safety":
            safety = extra[1].split('\n')

    # Put all features in a dictionary
    car_dict = dict(zip(df_headers, [name,
                                     mileage,
                                     address,
                                     rating,
                                     fuel_type,
                                     city_MPG,
                                     highway_MPG,
                                     drivetrain,
                                     engine,
                                     exterior_color,
                                     interior_color,
                                     transmission,
                                     entertainment,
                                     safety,
                                     price]))

    # Return the list of dictionaries
    return cars_list.append(car_dict)
