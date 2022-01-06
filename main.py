"""
@author: Kurt At Work. 
Github: https://github.com/kurtatwork
Version: 1.0
"""
# Colorama module: pip install colorama
import json
from colorama import init, Fore, Style
# Selenium module imports: pip install selenium
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.common.exceptions import TimeoutException as TE
from selenium.common.exceptions import ElementClickInterceptedException as ECIE
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# Python default import.
from time import sleep
from glob import glob
import os

"""Colorama module constants."""
init(convert=True)  # Init colorama module.
red = Fore.RED  # Red color.
green = Fore.GREEN  # Green color.
yellow = Fore.YELLOW  # Yellow color.
reset = Style.RESET_ALL  # Reset color attribute.

# webdriver and metamask paths
webdriver_path = 'assets/chromedriver.exe'
metamask_extension_path = 'assets/MetaMask.crx'

#GLOBAL FUNCTIONS
def cls() -> None:
    """Clear console function."""
    # Clear console for Windows using 'cls' and Linux & Mac using 'clear'.
    os.system('cls' if os.name == 'nt' else 'clear')

def read_file(file_: str, question: str) -> str:
    """Read file or ask for data to write in text file."""
    if not os.path.isfile(f'assets/{file_}.txt'):
        open(f'assets/{file_}.txt', 'a')
    with open(f'assets/{file_}.txt', 'r+', encoding='utf-8') as file:
        text = file.read()
        if text == '':
            text = input(question)
            if input(f'Do you want to save your {file_} in'
                     ' text file? (y/n) ').lower() == 'y':
                file.write(text)
                print(f'{green}Saved.{reset}')
            else:
                print(f'{yellow}Not saved.{reset}')
        return text

def grabJson(file: str) -> None:
    """Open Settings JSON file and read it."""
    from json import loads
    file = loads(open(file, encoding='utf-8').read())['nft']
    return file

def type_parameters(parameters: list, _range: int) -> list:
        """Change element's type of some parameters."""
        if len(parameters) > 0:
            if type(parameters[0]) == list:
                for parameter in range(len(parameters)):
                    for element in range(_range):
                        parameters[parameter][element] = \
                            str(parameters[parameter][element])
            else:
                for element in range(_range):
                    str1 = parameters
                    list1 = list(str1)
                    answer = list1
                    parameters = str(answer) 
        return parameters

def create_parameters(parametersA: list, jsonData: list) -> None:
        """Create parameters."""
        parametersB = parametersA
        filezC = jsonData
        # Upload:
        file_path = str(filezC[0]) 
        nft_name = str(filezC[1])
        external_link = filezC[2]
        description = str(filezC[3])
        collection = str(filezC[4])
        properties = type_parameters(
            parametersB, 2)  # [[type, name], ...]
        # This is where you enter the names of the properties from the NFTs
        # if you change the number of properties, you'll also need to reorder the 
        # integers in the array for each property (the number between the square brackets)... 
        # i.e. if you don't need 14 or 15 different properties and delete some, 
        # just make sure that you they still go in order and catch all the data 
        # from the Json files, matching the names of the paramaters in the Json files as well. 
        background = properties[0]
        subject = properties[1]
        shine = properties[2]
        eyes = properties[3]
        teeth = properties[4]
        mustache = properties[5]
        backOfHead = properties[6]
        lazerEyes = properties[7]
        flammability = properties[8]
        rays = properties[9]
        glasses = properties[10]
        nose = properties[11]
        hat = properties[12]
        frontText = properties[13]
        backText =properties[14]
        #Levels and Stats will need to be added later, as needed.
        unlockable_content: list = filezC[6]  # [bool, text]
        explicit_and_sensitive_content: bool = filezC[7]
        supply: int = filezC[8]
        blockchain: str = filezC[9]
        # Sell:
        type: str = filezC[10]
        price: int = filezC[11]
        duration: list = filezC[12]
        specific_buyer: list = filezC[13]
        quantity: int = filezC[14]
        # Builds a final array using values constructed above, to be returned in the line after 
        finalDataList = [file_path, nft_name, external_link, description, collection, [background[0], background[1], subject[0], subject[1], shine[0], shine[1], eyes[0], eyes[1], teeth[0], teeth[1], mustache[0], mustache[1], backOfHead[0], backOfHead[1], lazerEyes[0], lazerEyes[1], flammability[0], flammability[1], rays[0], rays[1], glasses[0], glasses[1], nose[0], nose[1], hat[0], hat[1], frontText[0], frontText[1], backText[0], backText[1]], unlockable_content, explicit_and_sensitive_content, supply, blockchain, type, price, duration, specific_buyer, quantity]
        return finalDataList

def get_nft(nft: int) -> None:
        """Get all settings of NFT."""
        nftNum = nft
        finalParamsList = json_file(nftNum)
        return finalParamsList

def json_file(nft: int) -> None:
        """Transform JSON list/dict to a whole list."""
        from json import dumps
        filez = grabJson(files[nft])
        filezB = dict_checker(filez)
        filezB = filezB[0]
        # filezB at this point holds all the Json data in a list, 
        # where the data can be pulled by calling filezB[i] 
        params = filezB[5]
        nft_settings = dict_checker(params)
        nft_settings = nft_settings
        # Get key's value from the NFT data.
        _list = []  # Init a new list.
        for element in nft_settings:  # Take each element in list.
            _list.append(dict_checker(element))  # Check element.
        # Create parameters from list.
        paramsList = create_parameters(_list, filezB)
        return paramsList
        
def dict_checker(element):
        """Check if element is a dict or not."""
        if type(element) == list:  # If element is a list.
            final_list = []  # Final list that will be return.
            for item in element:  # For each item in this list.
                temp_list = []  # Store all key's value.
                if type(item) == dict:  # If element is a dict.
                    for key in item:  # For each key in dict (item).
                        temp_list.append(item.get(key))  # Get key's value.
                else:
                    temp_list = item  # Do nothing.
                final_list.append(temp_list)  # Append each temp list.
            return final_list
        else:
            return element  # Else return the same element.

class Opensea(object):
    """Main class of Opensea automatic uploader."""

    def __init__(self, password: str, recovery_phrase: str) -> None:
        """Get the password and the recovery_phrase from the text file."""
        # Get recovery phrase of MetaMask wallet.
        self.recovery_phrase = recovery_phrase
        self.password = password  # Get new password.
        # Used files path.
        self.webdriver_path = 'assets/chromedriver.exe'
        self.metamask_extension_path = 'assets/MetaMask.crx'
        self.driver = self.webdriver()  # Start new webdriver.
        # Opensea URLs.
        self.login_url = 'https://opensea.io/login?referrer=%2Fasset%2Fcreate'
        self.create_url = 'https://opensea.io/asset/create'

    def webdriver(self):
        """Start webdriver and return state of it."""
        options = webdriver.ChromeOptions()  # Configure options for Chrome.
        options.add_extension(self.metamask_extension_path)  # Add extension.
        # Uncomment out the line below if you'd rather selenium runs in 'Headless' mode
        # options.add_argument("headless")  # Headless ChromeDriver. (COMMENTED OUT BY DEFAULT)
        options.add_argument("log-level=3")  # No logs is printed.
        options.add_argument("--mute-audio")  # Audio is muted.
        driver = webdriver.Chrome(self.webdriver_path, options=options)
        driver.maximize_window()  # Maximize window to reach all elements.
        return driver

    def element_clickable(self, element: str) -> None:
        """Click on element if it's clickable using Selenium."""
        try:
            WDW(self.driver, 60).until(EC.element_to_be_clickable(
                (By.XPATH, element))).click()
        except ECIE:
            # Sometimes the element is not clickable.
            self.driver.execute_script(
                "arguments[0].click();",
                self.driver.find_element(By.XPATH, element))

    def element_visible(self, element: str, timer: int = 30):
        """Check if element is visible using Selenium."""
        return WDW(self.driver, timer).until(EC.visibility_of_element_located(
            (By.XPATH, element)))

    def element_send_keys(self, element: str, keys: str) -> None:
        """Send keys to element if it's visible using Selenium."""
        try:
            WDW(self.driver, 5).until(EC.visibility_of_element_located(
                (By.XPATH, element))).send_keys(keys)
        except TE:
            # Some elements are not visible but are still present.
            WDW(self.driver, 5).until(EC.presence_of_element_located(
                (By.XPATH, element))).send_keys(keys)

    def clear_text(self, element) -> None:
        """Clear text from input."""
        self.element_clickable(element)
        webdriver.ActionChains(self.driver).key_down(Keys.CONTROL).perform()
        webdriver.ActionChains(self.driver).send_keys('a').perform()
        webdriver.ActionChains(self.driver).key_up(Keys.CONTROL).perform()

    def window_handles(self, window_number: int) -> None:
        """Check for window handles and wait until a specific tab is opened."""
        wait = 0
        while True:
            # If asked tab is opened.
            sleep(.5)
            if len(self.driver.window_handles) == window_number + 1:
                return True
            elif wait == 10:
                return False
            wait += 1

    def metamask(self) -> None:
        """Login to MetaMask extension."""
        print('Login to MetaMask extension.', end=' ')
        # Switch to MetaMask extension's tab.
        self.driver.switch_to.window(self.driver.window_handles[0])
        # Refresh MetaMask extension's tab while extension is not loaded.
        while True:
            # If page is fully loaded.
            if 'initialize' in self.driver.current_url:
                break
            self.driver.refresh()  # Reload page.
            sleep(1)  # Wait 1 second.
        # Click on "Start" button.
        self.element_clickable(
            '//*[@id="app-content"]/div/div[3]/div/div/div/button')
        # Click on "Import wallet" button.
        self.element_clickable('//*[@id="app-content"]/div/div[3]/div/div/'
                               'div[2]/div/div[2]/div[1]/button')
        # Click on "I agree" button.
        self.element_clickable('//*[@id="app-content"]/div/div[3]/div/div/'
                               'div/div[5]/div[1]/footer/button[2]')
        # Input recovery phrase.
        self.element_send_keys('//*[@id="app-content"]/div/div[3]/div/div/'
                               'form/div[4]''/div[1]/div/input',
                               self.recovery_phrase)
        # Input new password.
        self.element_send_keys('//*[@id="password"]', self.password)
        self.element_send_keys('//*[@id="confirm-password"]', self.password)
        # Check "I have read and agree to the..." checkbox.
        self.element_clickable(
            '//*[@id="app-content"]/div/div[3]/div/div/form/div[7]/div')
        # Click on "Import" button.
        self.element_clickable(
            '//*[@id="app-content"]/div/div[3]/div/div/form/button')
        # Click on "All done" button.
        self.element_clickable(
            '//*[@id="app-content"]/div/div[3]/div/div/button')
        print(f'{green}Logged to Metamask extension.{reset}')

    def opensea_login(self) -> None:
        """Login to Opensea using Metamask."""
        print('Login to Opensea.', end=' ')
        self.driver.switch_to.window(self.driver.window_handles[1]) \
            if self.window_handles(1) else self.retry_login(0)
        self.driver.get(self.login_url)  # Go to Opensea login URL.
        # Click on "Metamask" button in list of wallet.
        ul = len(self.element_visible(
            '//*[@id="__next"]/div[1]/main/div/div/div/div[2]/ul'
        ).find_elements(By.TAG_NAME, 'li'))
        for li in range(ul):
            li += 1  # Add 1 to start li element at li[1].
            # Check if button text contains "MetaMask".
            if self.element_visible(
                    '//*[@id="__next"]/div[1]/main/div/div/div/div[2]/ul/li'
                    f'[{li}]/button/div[2]/span').text == 'MetaMask':
                # Click on Metamask button.
                self.element_clickable('//*[@id="__next"]/div[1]/main/div/div'
                                       f'/div/div[2]/ul/li[{li}]/button')
                break
        # Switch on MetaMask popup tab.
        self.driver.switch_to.window(self.driver.window_handles[2]) \
            if self.window_handles(2) else self.retry_login(0)
        # Click on "Next" button.
        self.element_clickable('//*[@id="app-content"]/div/div[3]/div/'
                               'div[2]/div[4]/div[2]/button[2]')
        # Click on "Connect" button.
        self.element_clickable('//*[@id="app-content"]/div/div[3]/div/'
                               'div[2]/div[2]/div[2]/footer/button[2]')
        self.metamask_sign()
        # Reload page and retry to log in to Opensea if failed.
        try:
            WDW(self.driver, 60).until(EC.url_to_be(self.create_url))
            print(f'{green}Logged to Opensea.{reset}\n')
        except TE:
            self.retry_login()

    def metamask_sign(self) -> None:
        """Metamask confirm connection."""
        # Switch on MetaMask popup tab.
        self.driver.switch_to.window(self.driver.window_handles[2]) \
            if self.window_handles(2) else self.retry_login(0)
        # Click on "Sign" button.
        self.element_clickable(
            '//*[@id="app-content"]/div/div[3]/div/div[3]/button[2]')
        # Switch back to Opensea tab.
        self.driver.switch_to.window(self.driver.window_handles[1]) \
            if self.window_handles(1) else self.retry_login(0)

    def retry_login(self, value: int = 1) -> None:
        """Retry to log in to Opensea after an error occured."""
        print(f'{red}Failed to login to Opensea, Retrying.{reset}')
        if value == 0:
            self.opensea_login()
        else:
            self.metamask_sign()

    def opensea_upload(self, number: int) -> None:
        """Upload multiple NFTs automatically on Opensea."""
        try:
            # Go to Opensea login URL.
            self.driver.get(self.create_url + '?enable_supply=true')
            # Upload NFT file.
            if not os.path.exists(paramsList[0]) \
                    or paramsList[0] == '':
                raise TE('File doesn\'t exist.')
            self.element_send_keys('//*[@id="media"]', paramsList[0])
            # Input NFT name.
            if paramsList[1] == '':
                raise TE('Missing NFT Name.')
            self.element_send_keys('//*[@id="name"]', paramsList[1])
            # Input external link.
            if paramsList[2] != '':
                self.element_send_keys(
                    '//*[@id="external_link"]', paramsList[2])
            # Input description.
            if paramsList[3] != '':
                self.element_send_keys(
                    '//*[@id="description"]', paramsList[3])
            # Input collection and select it.
            if paramsList[4] != '':
                self.element_send_keys(
                    '//*[@id="__next"]/div[1]/main/div/div/section/div/form/'
                    'div[5]/div/div[2]/input', paramsList[4])
                try:
                    self.element_clickable(
                        '//*[contains(@id, "tippy")]/div/div/div/ul/li/button')
                except Exception:
                    raise TE('Collection doesn\'t exist')
            # Add properties, levels and stats.
            parameters = attributes
            print(f'len(parameters) // 2: {len(parameters) // 2}')
            totalParams = len(parameters) // 2
            for index in range(0, 1):
                if len(parameters) > 0:
                    self.element_clickable(
                        '//*[@id="__next"]/div[1]/main/div/div/section/div/'
                        f'form/section/div[{index + 1}]/div/div[2]/button')
                    parameter = 0
                    paramsIndex = 0
                    for element in range(0, totalParams):
                        if totalParams > 0:
                            self.element_clickable(
                                f'/html/body/div[{index + 2}]/div/div/div/'
                                'section/button')
                        parameter += 1
                        self.element_send_keys(
                            f'/html/body/div[{index + 2}]/div/div/div/section/'
                            f'table/tbody/tr[{parameter}]/td[1]/div/div/input',
                            parameters[paramsIndex])
                        actual_element = (
                            f'/html/body/div[{index + 2}]/div/div/div/section/'
                            f'table/tbody/tr[{parameter}]/td[2]/div/div/input')
                        self.clear_text(actual_element)
                        self.element_send_keys(actual_element, parameters[paramsIndex + 1])
                        paramsIndex = paramsIndex + 2
                    # Click on "Save" button.
                    self.element_clickable(f'/html/body/div[{index + 2}]/div'
                                        '/div/div/footer/button')
            # Set number of supply.
            if paramsList[8] != '' and type(paramsList[8]) == int:
                if '?enable_supply=true' in self.driver.current_url \
                        and paramsList[8] > 1:
                    # Set supply modifying value.
                    self.driver.execute_script(
                        f'arguments[0].value = {paramsList[8]};',
                        self.element_visible('//*[@id="supply"]'))
            # Set Blockchain.
            if paramsList[9] != '':
                blockchain = self.element_visible('//*[@id="chain"]')
                if blockchain.get_attribute('value') != paramsList[9]:
                    # Click on bottom sheet.
                    self.element_clickable(
                        '//*[@id="__next"]/div[1]/main/div/div'
                        '/section/div/form/div[7]/div/div[2]')
                    # Get lenght of elements list.
                    ul = len(self.element_visible(
                        '//*[@id="tippy-9"]/div/div/div/ul'
                    ).find_elements(By.TAG_NAME, 'li'))
                    # Find Blockchain in list.
                    for li in range(ul):
                        li += 1  # Add 1 to start li element at li[1].
                        # Check if span text contains Blockchain.
                        if self.element_visible(
                            f'//*[@id="tippy-9"]/div/div/div/ul/li[{li}]'
                            '/button/div[2]/span[1]').text \
                                == paramsList[9]:
                            # Click on specific Blockchain button.
                            self.element_clickable('//*[@id="tippy-9"]/div/div'
                                                   f'/div/ul/li[{li}]/button')
                            break
            # Click on "Create" button.
            self.element_clickable('//*[@id="__next"]/div[1]/main/div/div/'
                                   'section/div/form/div/div[1]/span/button')
            sleep(7)
            # Check if done.
            self.element_visible('/html/body/div[5]/div/div/div/div[1]', 30)
            WDW(webdriver, timeout=2)
            sleep(3)
            print(f'{green}Done.{reset}')
            # If price has been defined.
            print('Selling NFT.', end=' ')
            if paramsList[11] > 0:
                self.sell_nft()  # Sell NFT.
            else:
                print(f'{red}NFT sale cancelled.{reset}')
        except TE as error:
            print(f'{red}Failed: {error}{reset}')

    def sell_nft(self) -> None:
        """Set a price for the NFT, etc."""
        try:
            # Get sell page for the NFT.
            self.driver.get(self.driver.current_url + '/sell')
            self.element_send_keys(
                    '//input[@name="price"]', str(paramsList[11]))
            # Click on "Create" button.
            self.element_clickable('//button[@type="submit"]')
            self.element_clickable('//button[@class="Blockreact__Block-sc-1xf18x6-0 Buttonreact__StyledButton-sc-glfma3-0 bhqEJb fzwDgL"]')
            sleep(.5)
            WDW(webdriver, timeout=1)       
            # Sign Metamask 
            self.metamask_sign()
            WDW(webdriver, timeout=10)
            sleep(3)
            # click 'x' icon to close the popup and bring up the page for the NFT that was just listed
            self.element_clickable('//button[@class="UnstyledButtonreact__UnstyledButton-sc-ty1bh0-0 btgkrL"]')
            sleep(3)
            WDW(webdriver, timeout=20)
            #grabs URL of the NFT you just minted and listed
            justListedNftUrl = self.driver.current_url
            WDW(webdriver, timeout=1)
            sleep(1)
            self.element_clickable('//*[@id="__next"]/div[1]/main/div/div/div[2]/div[1]/div/div[1]/div[1]/article/header/div[2]/i')
            #generate NFT base number and store in variable to pass through to dictionary 
            #(if your NFT name doesn't end with a number, then the next 3 lines of code may not work as designed)
            baseNftNumber = paramsList[1]
            # Get last 6 characters
            lastChars = baseNftNumber[-6:]
            lastChars = int(lastChars)
            #Get current directory path
            cwd = os.getcwd()
            # Generate a Json object to be saved in the /OutputJson folder 
            # for later use with upcoming automated social media uploader
            dictionary ={
                "image_path" : paramsList[0],
                "nft_name" : paramsList[1],
                "main_site_url" : paramsList[2],
                "nft_description" : paramsList[3],
                "collection_name" : paramsList[4],
                "properties" : paramsList[5],
                "unlockable_content" : paramsList[6],
                "explicit_sensitive_content" : paramsList[7],
                "supply" : paramsList[8],
                "blockchain" : paramsList[9],
                "sale_type" : paramsList[10],
                "nft_price" : paramsList[11],
                "duration" : paramsList[12],
                "specific_buyer" : paramsList[13],
                "quantity_sold" : paramsList[14],
                "base_nft_number" : lastChars,
                "collection_link" : "*****CHANGE THIS STRING TO THE URL OF YOUR NFT COLLECTION*****",
                "nft_link" : justListedNftUrl,
                "tags" : ["AddYourTagsHere", "TagsGoHere", "KurtAtWork", "NFT", "NFTs", "OpenSea", "Blockchain", "Like", "Follow", "Share", "Subscribe", "NFTArtist", "NFTCollectors", "LetsGoBrandonNFT" ]               
            }
            # Serializing json 
            json_object = json.dumps(dictionary, indent = 4)
            # Writing to {lastChars}.json
            with open(cwd + "/outputJson/" + str(lastChars) + ".json", "w") as outfile:
                outfile.write(json_object)
            print(f'')
            print(f'{green}successfully wrote {lastChars}.json file.')
            sleep(1)
            print(f'{green}NFT put up for sale.{reset}')
        except TE as error:
            print(f'{red}NFT sale cancelled: {error}{reset}')
#starting variables
folder = [glob(f'data/{extension}')
            for extension in ['*.json']]
files = []
# quick loop that grabs all the file extensions and puts them in the files array
for extension in folder:
    for file in extension:
        files.append(file)
len_file = len(files)  # Length of file.
#initialization
print(f'{green}-------------------------------------------------------------------------------------------')
print(f"")
print(f'{green}Frankensteined together by Kurt At Work. '
          f'\n@Github: https://github.com/kurtatwork{reset}')
print(f"")
print(f"{green}Check out my NFT's on OpenSea")
print(f"{green}https://opensea.io/collection/letsgobrandon-nft")
print(f"{green}https://opensea.io/collection/selected-works-kurt-at-work")
print(f"{green}https://opensea.io/collection/a-sea-slug-called-jamulous")
print(f"")
print(f"{green}If you appreciate my work, consider donating to my MetaMask:")
print(f"{green}0x8736Ee29F772B9A972547C228a5F43E427E783AE")
print(f"""{green}   __ __         __    ___  __    _      __         __  
  / //_/_ ______/ /_  / _ |/ /_  | | /| / /__  ____/ /__
 / ,< / // / __/ __/ / __ / __/  | |/ |/ / _ \/ __/  '_/
/_/|_|\_,_/_/  \__/ /_/ |_\__/   |__/|__/\___/_/ /_/\_\ 
                                                        """)
print(f'-------------------------------------------------------------------------------------------')
print(f'')
password = read_file('password', '\nWhat is your MetaMask password? ')
recovery_phrase = read_file('recovery_phrase', '\nWhat is your MetaMask recovery phrase? ')
upload = Opensea(password, recovery_phrase) 
upload.metamask()
sleep(.5)
upload.opensea_login()
sleep(.5)
for elements in range(len_file):
        paramsList = get_nft(elements)
        attributes = paramsList[5]
        print(f'')
        print(f'Uploading NFT n° {elements + 1}/{len_file} : {paramsList[1]}')
        upload.opensea_upload(elements)  # Upload it.
        print(f'-------------------------------------------------------------------------------------------')     
print(f'')
print(f"{red}Please check the messages of this console to ensure NFT's properly Minted, Listed, and Json files created")
print(f"{red}Also, double check your OpenSea collection as well, to ensure that all NFT's uploaded correctly, no repeats, etc.")
print(f'')
print(f"{green}All {len_file} of the NFT's have been processed.")
print(f'')
