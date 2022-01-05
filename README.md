# KurtAtWork-OpenSea-Automatic-Uploader version-1.0.0                                                          

Hey everyone, I forked a copy of another Auto-Uploader that I downloaded from a github repo. Former code had issues uploading multiple NFTs (i could only get it to do mint and list ONE NFT no matter what i did to the code to change it, tried many many changes), also there were issues with actually listing them (former code only had a comment at the line where the sale was supposed to happen saying 'Do this'), and other problems. 

after weeks of trying to get it to upload more than one NFT at a time and having zero success, I ended up giving up on modifying the old code and decided to rewrite the entire thing from the ground up and using a few bits and pieces from the old code that actually worked. 

Anyway, here it is... it only works with Json files currently because that's what i needed. This project was built more around my own needs and is uploaded to this repo in that way as well... 

its not really designed to be the most user friendly or fully featured, its just a wham-bam-thankyou-ma'am sorta Git'er Done kinda project. 

Changes might come down the road, but for the time being, if you're using multiple json files to upload this will work for you.

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

This script allows you to upload and sell **as many NFTs as you want to Opensea**, all **automatically** and **quickly** (about 2.5 NFTs per minute). **All metadata are integrated**, and the **Ethereum** and **Polygon** Blockchains are supported.  

**You can decide whether you want to upload or sell your NFTs, or both**. If you upload your NFTs and sell them later, a CSV file is created with the URL of the NFT as well as its Blockchain and supply number.

➜ **Feel free to help support the dev of this github repo if it has helped you out in your NFT journey and you feel like giving back (THANK YOU)**:
**0x8736ee29f772b9a972547c228a5f43e427e783ae** (Ethereum).
➜ **Check out one of my collections on OpenSea if you feel like it [Kurt At Work](https://opensea.io/collection/selected-works-kurt-at-work)**.
➜ **Check out another of my collections on OpenSea if you feel like it [SeaSlug Called Jamulous](https://opensea.io/collection/a-sea-slug-called-jamulous)**.
➜ **Check out yet another one of my collections on OpenSea if you feel like it [Let's Go Brandon NFT](https://opensea.io/collection/letsgobrandon-nft)**.

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
          <td>CSV examples</td>
          <td>XLSX examples</td>
       </tr>
       <tr>
          <td><strong>File Path *</strong></td>
          <td>String</td>
          <td></td>
          <td>"file_path": "C:/Users/Admin/Desktop/NFT/nft_0001.png",</td>
          <td>C:/Users/Admin/Desktop/NFT/nft_0001.png;;</td>
          <td>C:/Users/Admin/Desktop/NFT/nft_0001.png</td>
       </tr>
       <tr>
          <td><strong>NFT Name *</strong></td>
          <td>String</td>
          <td></td>
          <td>"nft_name": "NFT #1",</td>
          <td>NFT #1;;</td>
          <td>NFT #1</td>
       </tr>
       <tr>
          <td>External Link</td>
          <td>String</td>
          <td></td>
          <td>"external_link": "https://github.com/kurtatwork/KurtAtWork-OpenSea-Auto-Uploader",
             <br>"external_link": "",
          </td>
          <td>https://github.com/kurtatwork/KurtAtWork-OpenSea-Auto-Uploader;;</td>
          <td>https://github.com/kurtatwork/KurtAtWork-OpenSea-Auto-Uploader</td>
       </tr>
       <tr>
          <td>Description</td>
          <td>String</td>
          <td></td>
          <td>"description": "This is my first NFT.",
             <br>"description": "",
          </td>
          <td>This is my first NFT.;;</td>
          <td>This is my first NFT.</td>
       </tr>
       <tr>
          <td>Collection</td>
          <td>String</td>
          <td></td>
          <td>"collection": "My NFTs",
             <br>"collection": "",
          </td>
          <td>My NFTs;;</td>
          <td>My NFTs.</td>
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
          <td>[["Dog", "Male"], ["Cat", "Female"]];;
             <br>[["Dog", "Male"]];;
             <br>["Dog", "Male"];;
          </td>
          <td>[["Dog", "Male"], ["Cat", "Female"]]
             <br>[["Dog", "Male"]]
             <br>["Dog", "Male"]
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
          <td>[["Speed", 2, 5], ["Width", 1, 10]];;
             <br>[["Speed", 2, 5]];;
             <br>["Speed", 2, 5];;
          </td>
          <td>[["Speed", 2, 5], ["Width", 1, 10]]
             <br>[["Speed", 2, 5]]
             <br>["Speed", 2, 5]
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
          <td>[["Strenght", 10, 100], ["Age", 1, 99]];;
             <br>[["Strenght", 10, 100]];;
             <br>["Strenght", 10, 100];;
          </td>
          <td>[["Strenght", 10, 100], ["Age", 1, 99]]
             <br>[["Strenght", 10, 100]]
             <br>["Strenght", 10, 100]
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
          <td>[True, "Thank you for purchasing my NFT!"];;
             <br>[False];;
             <br>False;;
          </td>
          <td>[True, "Thank you for purchasing my NFT!"]
             <br>[False]
             <br>False
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
          <td>True;;
             <br>False;;
          </td>
          <td>True
             <br>False
          </td>
       </tr>
       <tr>
          <td>Supply</td>
          <td>Integer</td>
          <td></td>
          <td>"supply": 1,
             <br>"supply" : "",
          </td>
          <td>1;;</td>
          <td>1</td>
       </tr>
       <tr>
          <td>Blockchain</td>
          <td>String</td>
          <td></td>
          <td>"blockchain": "Polygon",
             <br>"blockchain" : "",
          </td>
          <td>Polygon;;</td>
          <td>Polygon</td>
       </tr>
       <tr>
          <td>Sale Type (only for Ethereum Blockchain and 1 supply)</td>
          <td>String</td>
          <td></td>
          <td>"sale_type": "Timed Auction",
             <br>"sale_type": "",
          </td>
          <td>Timed Auction;;</td>
          <td>Timed Auction</td>
       </tr>
       <tr>
          <td><strong>Price *</strong></td>
          <td>Float or Integer</td>
          <td></td>
          <td>"price": 5,
             <br>"price": 0.25,
          </td>
          <td>5;;
             <br>0.25;;
          </td>
          <td>5
             <br>0.25
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
          <td>["Sell with declining price", 0.002];;
             <br>["Sell to highest bidder", 0.05];;
             <br>["Sell to highest bidder", ""];;
          </td>
          <td>["Sell with declining price", 0.002]
             <br>["Sell to highest bidder", 0.05]
             <br>["Sell to highest bidder", ""]
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
          <td>["01-01-2022 14:00", "01-04-2022 15:00"];;
             <br>["1 week"];;
             <br>1 week;;
          </td>
          <td>["01-01-2022 14:00", "01-04-2022 15:00"]
             <br>["1 week"]
             <br>1 week
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
          <td>[True, "0xDD135d5be0a23f6daAAE7D2d0580828c9e09402E"];;
             <br>[False];;
             <br>False;;
          </td>
          <td>[True, "0xDD135d5be0a23f6daAAE7D2d0580828c9e09402E"]
             <br>[False]
             <br>False
          </td>
       </tr>
       <tr>
          <td><strong>Quantity * (only for 1+ supplies)</strong></td>
          <td>Integer</td>
          <td></td>
          <td>"quantity": 4
             <br>"quantity": ""
          </td>
          <td>4</td>
          <td>4</td>
       </tr>
    </tbody>
 </table>
 
  And it gives you something like this: [JSON](https://github.com/kurtatwork/KurtAtWork-OpenSea-Auto-Uploader/blob/master/data/json_structure_upload_and_sale.json).
 
* ### Upload only

 <table>
    <tbody>
       <tr>
          <td>Details</td>
          <td>Data Types</td>
          <td>Literal examples</td>
          <td>JSON examples</td>
          <td>CSV examples</td>
          <td>XLSX examples</td>
       </tr>
       <tr>
          <td><strong>File Path *</strong></td>
          <td>String</td>
          <td></td>
          <td>"file_path": "C:/Users/Admin/Desktop/NFT/nft_0001.png",</td>
          <td>C:/Users/Admin/Desktop/NFT/nft_0001.png;;</td>
          <td>C:/Users/Admin/Desktop/NFT/nft_0001.png</td>
       </tr>
       <tr>
          <td><strong>NFT Name *</strong></td>
          <td>String</td>
          <td></td>
          <td>"nft_name": "NFT #1",</td>
          <td>NFT #1;;</td>
          <td>NFT #1</td>
       </tr>
       <tr>
          <td>External Link</td>
          <td>String</td>
          <td></td>
          <td>"external_link": "https://github.com/kurtatwork/KurtAtWork-OpenSea-Auto-Uploader",
             <br>"external_link": "",
          </td>
          <td>https://github.com/kurtatwork/KurtAtWork-OpenSea-Auto-Uploader;;</td>
          <td>https://github.com/kurtatwork/KurtAtWork-OpenSea-Auto-Uploader</td>
       </tr>
       <tr>
          <td>Description</td>
          <td>String</td>
          <td></td>
          <td>"description": "This is my first NFT.",
             <br>"description": "",
          </td>
          <td>This is my first NFT.;;</td>
          <td>This is my first NFT.</td>
       </tr>
       <tr>
          <td>Collection</td>
          <td>String</td>
          <td></td>
          <td>"collection": "My NFTs",
             <br>"collection": "",
          </td>
          <td>My NFTs;;</td>
          <td>My NFTs.</td>
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
          <td>[["Dog", "Male"], ["Cat", "Female"]];;
             <br>[["Dog", "Male"]];;
             <br>["Dog", "Male"];;
          </td>
          <td>[["Dog", "Male"], ["Cat", "Female"]]
             <br>[["Dog", "Male"]]
             <br>["Dog", "Male"]
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
          <td>[["Speed", 2, 5], ["Width", 1, 10]];;
             <br>[["Speed", 2, 5]];;
             <br>["Speed", 2, 5];;
          </td>
          <td>[["Speed", 2, 5], ["Width", 1, 10]]
             <br>[["Speed", 2, 5]]
             <br>["Speed", 2, 5]
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
          <td>[["Strenght", 10, 100], ["Age", 1, 99]];;
             <br>[["Strenght", 10, 100]];;
             <br>["Strenght", 10, 100];;
          </td>
          <td>[["Strenght", 10, 100], ["Age", 1, 99]]
             <br>[["Strenght", 10, 100]]
             <br>["Strenght", 10, 100]
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
          <td>[True, "Thank you for purchasing my NFT!"];;
             <br>[False];;
             <br>False;;
          </td>
          <td>[True, "Thank you for purchasing my NFT!"]
             <br>[False]
             <br>False
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
          <td>True;;
             <br>False;;
          </td>
          <td>True
             <br>False
          </td>
       </tr>
       <tr>
          <td><strong>Supply *</strong></td>
          <td>Integer</td>
          <td></td>
          <td>"supply": 1,</td>
          <td>1;;</td>
          <td>1</td>
       </tr>
       <tr>
          <td><strong>Blockchain *</strong></td>
          <td>String</td>
          <td></td>
          <td>"blockchain": "Polygon"</td>
          <td>Polygon</td>
          <td>Polygon</td>
       </tr>
    </tbody>
 </table>
 
 And it gives you something like this: [JSON](https://github.com/kurtatwork/KurtAtWork-OpenSea-Auto-Uploader/blob/master/data/json_structure_upload_only.json).
 
 * ### Sale only
 
 If you have already uploaded your NFTs with this bot, a file has been generated with containing the URL, the Blockchain and the supply number of each NFT. You have to complete it with sale values.

 <table>
    <tbody>
       <tr>
          <td>Details</td>
          <td>Data Types</td>
          <td>Literal examples</td>
          <td>JSON examples</td>
          <td>CSV examples</td>
          <td>XLSX examples</td>
       </tr>
       <tr>
          <td><strong>NFT URL * </strong></td>
          <td>String</td>
          <td></td>
          <td>"nft_url": "https://opensea.io/assets/matic/0x2953399124f0cbb46d2cbacd8a89cf0599974963/99995353970554757559721471534129028266698199001274859511402524949800648966145",</td>
          <td>https://opensea.io/assets/matic/0x2953399124f0cbb46d2cbacd8a89cf0599974963/99995353970554757559721471534129028266698199001274859511402524949800648966145;;</td>
          <td>https://opensea.io/assets/matic/0x2953399124f0cbb46d2cbacd8a89cf0599974963/99995353970554757559721471534129028266698199001274859511402524949800648966145</td>
       </tr>
       <tr>
          <td><strong>Supply *</strong></td>
          <td>Integer</td>
          <td></td>
          <td>"supply": 1,</td>
          <td>1;;</td>
          <td>1</td>
       </tr>
       <tr>
          <td><strong>Blockchain *</strong></td>
          <td>String</td>
          <td></td>
          <td>"blockchain": "Polygon",</td>
          <td>Polygon;;</td>
          <td>Polygon</td>
       </tr>
       <tr>
          <td>Sale Type (only for Ethereum Blockchain and 1 supply)</td>
          <td>String</td>
          <td></td>
          <td>"sale_type": "Timed Auction",</td>
          <td>Timed Auction;;</td>
          <td>Timed Auction</td>
       </tr>
       <tr>
          <td><strong>Price *</strong></td>
          <td>Float or Integer</td>
          <td></td>
          <td>"price": 5,
             <br>"price: 0.25,</td>
          <td>5;;
             <br>0.25;;
          </td>
          <td>5
             <br>0.25
          </td>
       </tr>
       <tr>
          <td>Method (only for "Timed Auction")</td>
          <td>List[String, Float]</td>
          <td>["method", price]
           <br>["method, ""]</td>
          <td>"method": ["Sell with declining price", 0.002],
             <br>"method": ["Sell to highest bidder", 0.05],
             <br>"method": ["Sell to highest bidder", ""],</td>
          <td>["Sell with declining price", 0.002];;
             <br>["Sell to highest bidder", 0.05];;
             <br>["Sell to highest bidder", ""];;
          </td>
          <td>["Sell with declining price", 0.002]
             <br>["Sell to highest bidder", 0.05]
             <br>["Sell to highest bidder", ""]
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
          </td>
          <td>["01-01-2022 14:00", "01-04-2022 15:00"];;
             <br>["1 week"];;
             <br>1 week;;
          </td>
          <td>["01-01-2022 14:00", "01-04-2022 15:00"]
             <br>["1 week"]
             <br>1 week
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
          <td>"specific_buyer": [true, "0xDD135d5be0a23f6daAAE7D2d0580828c9e09402E"]
              <br>"specific_buyer": [false]
              <br>"specific_buyer": false</td>
          <td>[True, "0xDD135d5be0a23f6daAAE7D2d0580828c9e09402E"];;
             <br>[False];;
             <br>False;;
          </td>
          <td>[True, "0xDD135d5be0a23f6daAAE7D2d0580828c9e09402E"]
             <br>[False]
             <br>False
          </td>
       </tr>
       <tr>
          <td><strong>Quantity * (only for 1+ supplies)</strong></td>
          <td>Integer</td>
          <td></td>
          <td>"quantity": 4</td>
          <td>4</td>
          <td>4</td>
       </tr>
    </tbody>
 </table>

And it gives you something like this: [JSON](https://github.com/kurtatwork/KurtAtWork-OpenSea-Auto-Uploader/blob/master/data/json_structure_sale_only.json).


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
