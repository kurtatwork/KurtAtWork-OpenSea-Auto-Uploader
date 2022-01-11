# KurtAtWork-OpenSea-Automatic-Uploader version-1.0.0                                                          

Hey everyone, I created a Custom selenium python script borrowing bits and pieces from the Maxime OpenSea Auto Uploader script. I had tried using his script as it was, but I ran into many issues, probably mostly user error on my part (who knows)

Anyway, here it is... it only works with Json files currently because that's what i needed. This project was built more around my own needs and is uploaded to this repo in that way as well... It's NOT going to work for everyone, and you'll very highly likely need to modify the code to get it to work with your project. 
I'm sure that i could do some things to make it more user friendly... 

On the other hand, when i wrote it, it wasn't really designed to be the most user friendly or fully featured, its just a wham-bam thank you ma'am sorta "Git'er Done" kinda project. 

Changes might come down the road, but for the time being, if you're using multiple json files to upload to opensea, this should work for you (with a little elbow grease).

The way its supposed to work is, after setting up the folders and files, you add your Json files to the Data folder... you don't use the single Master Json file that's generated from say, the hashlips generator for instance... you would instead use the individual numbered json files. Add as many of those as you want to the data folder, and then run the script and once it starts it'll log into your metamask, go to to opensea, create an NFT (add properties, collection, set which blockchain, etc), it will then MINT that NFT and then LIST the NFT for whatever price set in the Json file... it will then go on to the next Json file in the data folder and do the same process for that until it has gone through all Json files.

Let me know what you think, and how i could improve my code. I'm open to hearing feedback and welcome changes.

➜ **Feel free to support the dev of this repo if it has helped you out in your NFT journey and you feel like giving back (THANK YOU)**: <br>
➜ **0x8736ee29f772b9a972547c228a5f43e427e783ae** (Ethereum).<br>
➜ **Check out one of my collections on OpenSea if you feel like it [Kurt At Work](https://opensea.io/collection/selected-works-kurt-at-work)**.<br>
➜ **Check out another of my collections on OpenSea if you feel like it [SeaSlug Called Jamulous](https://opensea.io/collection/a-sea-slug-called-jamulous)**.<br>
➜ **Check out yet another one of my collections on OpenSea if you feel like it [Let's Go Brandon NFT](https://opensea.io/collection/letsgobrandon-nft)**.<br>

# Automatically upload your NFTs on Opensea using Python Selenium.

* **(_Version 1.0.0 - January 05, 2022_).**
* Sign up on [Opensea](https://opensea.io/?ref=0x8736ee29f772b9a972547c228a5f43e427e783ae) (Affiliate link).
* Sign up on [MetaMask](https://metamask.io/).


# Table of contents

* **[What does this bot do?](https://github.com/kurtatwork/KurtAtWork-OpenSea-Auto-Uploader#what-does-this-bot-do)**
* **[Changelog](https://github.com/kurtatwork/KurtAtWork-OpenSea-Auto-Uploader#changelog).**
* **[To do list](https://github.com/kurtatwork/KurtAtWork-OpenSea-Auto-Uploader#to-do-list).**
* **[Instructions](https://github.com/kurtatwork/KurtAtWork-OpenSea-Auto-Uploader#instructions)**.
  * [Basic installation of Python for beginners](https://github.com/kurtatwork/KurtAtWork-OpenSea-Auto-Uploader#basic-installation-of-python-for-beginners).
  * [Configuration of the bot](https://github.com/kurtatwork/KurtAtWork-OpenSea-Auto-Uploader#configuration-of-the-bot).
* **[Data files structure](https://github.com/kurtatwork/KurtAtWork-OpenSea-Auto-Uploader#data-files-structure).**
  * [Upload and sale](https://github.com/kurtatwork/KurtAtWork-OpenSea-Auto-Uploader#upload-and-sale).
  * [Upload only](https://github.com/kurtatwork/KurtAtWork-OpenSea-Auto-Uploader#upload-only).
  * [Sale only](https://github.com/kurtatwork/KurtAtWork-OpenSea-Auto-Uploader#sale-only).
* **[Configuration of the sales part of the NFTs](https://github.com/kurtatwork/KurtAtWork-OpenSea-Auto-Uploader#configuration-of-the-sales-part-of-the-nfts).**
* **[Known issues and important things to know](https://github.com/kurtatwork/KurtAtWork-OpenSea-Auto-Uploader#known-issues-and-important-things-to-know).**


## What does this bot do?

This script allows you to upload and sell **as many NFTs as you want to Opensea**, all **automatically** and **quickly** (about 2 NFTs per minute) **with metadata integrated**, and **Ethereum** and **Polygon** Blockchains are supported.  

**You can decide whether you want to upload or sell your NFTs, or both**. Currently this code has a hard coded schedule of a 6 month sales listing (the old code was breaking at this point so i figured an easy fix was to just comment out that line of code and let the default value do its thing, since what I wanted was the default anyway)

## Changelog


* **Version 1.0:** 
  * Inital commit.


## To do list

* ✔ <strike>MetaMask automatic login.</strike>
* ✔ <strike>Opensea automatic login with MetaMask.</strike>
* ✔ <strike>Automatic NFT uploader.</strike>
* ✔ <strike>Possibility to set a price for each NFT.</strike>  
* ✔ <strike>Support for 1+ supplies and Polygon blockchain.</strike>
* ✔ <strike>**Actually Lists the NFT for sale**.</strike>
* ✔ <strike>Data file browsing feature.</strike>
* ✔ <strike>JSON structure reader and interpreter.</strike>



## Instructions

* ### Basic installation of Python for beginners:
  * [Download this repository](https://github.com/kurtatwork/KurtAtWork-OpenSea-Auto-Uploader/archive/refs/heads/master.zip) or clone it by typing this command in your command prompt:
```
git clone https://github.com/kurtatwork/KurtAtWork-OpenSea-Auto-Uploader.git
```
  * It requires [Python](https://www.python.org/) 3.7 or a newest version - _developped with Python 3.9.7_.
  * Install [pip](https://pip.pypa.io/en/stable/installation/) to be able to have needed Python modules.
  * Open a command prompt in the repository folder and type:
```
pip install -r requirements.txt
```
* ### Configuration of the bot:
  * Extract the repository folder from the ZIP file, you should have a folder named  `KurtAtWork-OpenSea-Auto-Uploader-master`.
  * Download and install [Google Chrome](https://www.google.com/intl/en_en/chrome/).
  * Download the [ChromeDriver executable](https://chromedriver.chromium.org/downloads) that is compatible with the actual version of your Google Chrome browser and your OS (Operating System). To know your Google Chrome browser version, refer to: **_[What version of Google Chrome do I have?](https://www.whatismybrowser.com/)_**
  * Extract the executable file from the ZIP file and copy/paste it in the `assets/` folder of the repository.
  * Create your NFTs data files containing all details for each NFT. It currently MUST be JSON files. NFT Json files must be located in the `data/` folder.  
    **[What structure should the files have?](https://github.com/kurtatwork/KurtAtWork-OpenSea-Auto-Uploader#data-files-structure)**


## Data files structure

If you do not want to add details to the values not required, leave:

  * **an empty string** for JSON files: 
```json
"file_path": "C:/Users/Admin/Desktop/NFT/nft_0001.png",
"nft_name": "NFT #1",
"description": "",
```

<strong>Required values *</strong>  
  (Mandatory value in certain specified cases)

* ### Upload and sale

 <table>
    <tbody>
       <tr>
          <td>Details</td>
          <td>Data Types</td>
          <td>Literal examples</td>
          <td>JSON examples</td>
       </tr>
       <tr>
          <td><strong>File Path *</strong></td>
          <td>String</td>
          <td></td>
          <td>"file_path": "C:/Users/Admin/Desktop/NFT/nft_0001.png",</td>
       </tr>
       <tr>
          <td><strong>NFT Name *</strong></td>
          <td>String</td>
          <td></td>
          <td>"nft_name": "NFT #1",</td>
       </tr>
       <tr>
          <td>External Link</td>
          <td>String</td>
          <td></td>
          <td>"external_link": "https://yournftwebsite.com/yournftcollection/000001",
             <br>"external_link": "",
          </td>
       </tr>
       <tr>
          <td>Description</td>
          <td>String</td>
          <td></td>
          <td>"description": "This is my first NFT.",
             <br>"description": "",
          </td>
       </tr>
       <tr>
          <td>Collection</td>
          <td>String</td>
          <td></td>
          <td>"collection": "My NFTs",
             <br>"collection": "",
          </td>
       </tr>
       <tr>
          <td>Properties</td>
          <td>List[[String, String], ...]
           <br>List[String, String]</td>
          <td>["type", "name"]
           <br>[["type", "name"], ["type", "name"]]</td>
          <td>"properties": [{ "type": "Dog", "name": "Male" }, { "type": "Cat", "name": "Female" }],
             <br>"properties": [{ "type": "Dog", "name": "Male" }],
             <br>"properties": "",
          </td>
       </tr>
       <tr>
          <td>Levels</td>
          <td>List[[String, Integer, Integer], ...]
           <br>List[String, Integer, Integer]</td>
          <td>["name", value_from, value_to]
           <br>[["name", value_from, value_to], ["name", value_from, value_to]]</td>
          <td>"levels": [{ "name": "Speed", "from": 2, "to": 5 }, { "name": "Width", "from": 1, "to": 10 }],
             <br>"levels": [{ "name": "Speed", "from": 2, "to": 5 }],
             <br>"levels": "",
          </td>
       </tr>
       <tr>
          <td>Stats</td>
          <td>List[[String, Integer, Integer], ...]
           <br>List[String, Integer, Integer]</td>
          <td>["name", value_from, value_to]
           <br>[["name", value_from, value_to], ["name", value_from, value_to]]</td>
          <td>"stats": [{ "name": "Strenght", "from": 10, "to": 100 }, { "name": "Age", "from": 1, "to": 99 }],
             <br>"stats": [{ "name": "Strenght", "from": 10, "to": 100 }],
             <br>"stats": "",
          </td>
       </tr>
       <tr>
          <td>Unlockable Content</td>
          <td>List[Boolean, String]
           <br>List[Boolean]
           <br>Boolean</td>
          <td>[True, "unlockable_content"]
           <br>[False]
           <br>False</td>
          <td>"unlockable_content": [true, "Thank you for purchasing my NFT!"],
             <br>"unlockable_content": [false],
             <br>"unlockable_content": false,
             <br>"unlockable_content": "",
          </td>
       </tr>
       <tr>
          <td>Explicit And Sensitive Content</td>
          <td>Boolean</td>
          <td></td>
          <td>"explicit_and_sensitive_content": true,
             <br>"explicit_and_sensitive_content": false,
             <br>"explicit_and_sensitive_content": "",
          </td>
       </tr>
       <tr>
          <td>Supply</td>
          <td>Integer</td>
          <td></td>
          <td>"supply": 1,
             <br>"supply" : "",
          </td>
       </tr>
       <tr>
          <td>Blockchain</td>
          <td>String</td>
          <td></td>
          <td>"blockchain": "Polygon",
             <br>"blockchain" : "",
          </td>
       </tr>
       <tr>
          <td>Sale Type (only for Ethereum Blockchain and 1 supply)</td>
          <td>String</td>
          <td></td>
          <td>"sale_type": "Timed Auction",
             <br>"sale_type": "",
          </td>
       </tr>
       <tr>
          <td><strong>Price *</strong></td>
          <td>Float or Integer</td>
          <td></td>
          <td>"price": 5,
             <br>"price": 0.25,
          </td>
       </tr>
       <tr>
          <td>Method (only for "Timed Auction")</td>
          <td>List[String, Float]</td>
          <td>["method", price]
           <br>["method, ""]</td>
          <td>"method": ["Sell with declining price", 0.002],
             <br>"method": ["Sell to highest bidder", 0.05],
             <br>"method": ["Sell to highest bidder", ""],
             <br>"method": "",
          </td>
       </tr>
       <tr>
          <td>Duration ("DD-MM-YYYY HH:MM")</td>
          <td>List[String, String]
           <br>List[String]
           <br>String</td>
          <td>["from_date", "to_date"]
           <br>["days/weeks/months"]
           <br>"days/weeks/months"</td>
          <td>"duration": ["01-01-2022 14:00", "01-04-2022 15:00"],
             <br>"duration": ["1 week"],
             <br>"duration": "1 week",
             <br>"duration": "",
          </td>
       </tr>
       <tr>
          <td>Specific Buyer</td>
          <td>List[Boolean, String]
           <br>[Boolean]
           <br>Boolean</td>
          <td>[True, "wallet"]
           <br>[False]
           <br>False</td>
          <td>"specific_buyer": [true, "0xDD135d5be0a23f6daAAE7D2d0580828c9e09402E"],
             <br>"specific_buyer": [false],
             <br>"specific_buyer": false,
             <br>"specific_buyer": "",
          </td>
       </tr>
       <tr>
          <td><strong>Quantity * (only for 1+ supplies)</strong></td>
          <td>Integer</td>
          <td></td>
          <td>"quantity": 4
             <br>"quantity": ""
          </td>
       </tr>
    </tbody>
 </table>
 
  And it gives you something like this: [JSON](https://github.com/kurtatwork/KurtAtWork-OpenSea-Auto-Uploader/blob/master/data/json_structure_upload_and_sale.json).
  

## Configuration of the sale part of the NFTs

When you want to sell your NFTs, Opensea requires various details according to their Blockchain or supply number.

<table>
 <tbody>
  <tr>
   <td colspan="15">Ethereum</td>
   <td colspan="7">Polygon</td>
  </tr>
  <tr>
   <td colspan="11">Supply number equal to 1</td>
   <td colspan="4">Supply number higher than 1</td>
   <td colspan="3">Supply number equal to 1</td>
   <td colspan="4">Supply number higher than 1</td>
  </tr>
  <tr>
   <td colspan="3">Fixed Price</td>
   <td colspan="8">Timed Auction</td>
   <td colspan="4"></td>
   <td colspan="3"></td>
   <td colspan="4"></td>
  </tr>
  <tr>
   <td colspan="3"></td>
   <td colspan="4">Sell to highest bidder</td>
   <td colspan="4">Sell with declining price</td>
   <td colspan="4"></td>
   <td colspan="3"></td>
   <td colspan="4"></td>
  </tr>
  <tr>
   <td><strong>Price</strong> (ETH)</td>
   <td><strong>Duration</strong> (from a date to an other date or 1 day, 3 days, 1 week, 6 months)</td>
   <td>Reserve for a <strong>specific buyer</strong></td>
   
   <td><strong>Price</strong> (ETH)</td>
   <td><strong>Duration</strong> (from a date to an other date or 1 day, 3 days, 1 week)</td>
   <td><i>(Optional)</i> <strong>Reserved Price</strong> (WETH) greater than 1 WETH and greater than <strong>Starting Price</strong>.</td>
   <td>Reserve for a <strong>specific buyer</strong></td>
   
   <td><strong>Starting Price</strong> (ETH)</td>
   <td><strong>Duration</strong> (from a date to an other date or 1 day, 3 days, 1 week)</td>
   <td><strong>Ending Price</strong> (ETH) less than the<strong>Starting Price</strong>.</td>
   <td>Reserve for a <strong>specific buyer</strong></td>
   
   <td><strong>Quantity</strong></td>
   <td><strong>Price</strong> (ETH)</td>
   <td><strong>Duration</strong> (from a date to an other date or 1 day, 3 days, 1 week, 6 months)</td>
   <td>Reserve for a <strong>specific buyer</strong></td>
   
   <td><strong>Price</strong> (ETH)</td>
   <td><strong>Duration</strong> (from a date to an other date or 1 day, 3 days, 1 week, 6 months)</td>
   <td>Reserve for a <strong>specific buyer</strong></td>
   
   <td><strong>Quantity</strong></td>
   <td><strong>Price</strong> (ETH)</td>
   <td><strong>Duration</strong> (from a date to an other date or 1 day, 3 days, 1 week, 6 months)</td>
   <td>Reserve for a <strong>specific buyer</strong></td>
  </tr>
 </tbody>
</table>


## Known issues and important things to know

* Make sure to **deposit Ethereum (ETH/WETH)** or **Polygon (MATIC)** on your wallet before proceeding to the sale. Otherwise the bot will cancel the sale.  
  Opensea needs an **Ethereum** wallet with more than **0.05 ETH** or a **Polygon** wallet with a deposit of **any amount**.
* **The file path should not contain a unique "\\". It can be a "/" or a "\\\\", as you can see for the JSON file *(it applies to all file formats)*:**
```json
// You can use this format for your path:
"file_path": "C:/Users/Admin/Desktop/MyNFTs/nft_0001.png",
// or this one:
"file_path": "C:\\Users\\Admin\\Desktop\\MyNFTs\\nft_0001.png",
// but not this one (you can see that "\" is highlighted in red):
"file_path": "C:\Users\Admin\Desktop\MyNFTs\nft_0001.png",
```
* The bot may crash at the beginning when loading the MetaMask extension (a Selenium module issue), An error like the one below should appear:  
```python
selenium.common.exceptions.WebDriverException:
Message: unknown error: failed to wait for extension background page to load:
chrome-extension://nkbihfbeogaeaoehlefnkodbefpgknn/background.html from timeout:
Timed out receiving message from renderer: 10.000
```
* When lauching the webdriver, Selenium can raise an exception:
```python
driver = webdriver.Chrome(service=Service( # DeprecationWarning using
TypeError: WebDriver.init() got an unexpected keyword argument 'service'
```
You must update your Selenium version to 4.1.0 or higher by typing in the command prompt:
```
pip install selenium --upgrade
```
You can now verify that a more recent version of Selenium is installed by typing:
```
pip show selenium
```  
