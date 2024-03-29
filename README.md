# shopping-cart
Alice's Shopping Cart Project

## Prerequisites
  + Anaconda 3.7
  + Python 3.7
  + Git
  + Visual Studio Code


## Installation

Fork this repository.

Then use GitHub Desktop or the command-line to "clone" or download your fork onto your local computer.

Choose a familiar download location like the Desktop.

After cloning the repo, navigate there from the command-line:

```sh
cd ~/Desktop/shopping-cart
```

Open the environment.
```sh
conda create -n shopping-env python=3.7 # (first time only)
conda activate shopping-env
```

Install Python package dependencies (dotenv package, sendgrid 6.0.5 package):
```sh
pip install -r requirements.txt # (first time only)
```

For Email Receipts:
Using Visual Studio Code, create a ".env" file in the shopping-cart folder and input the following info.

```sh
SENDGRID_API_KEY = "xyz key" # (must input your own SendGrid API Key)

SENDGRID_TEMPLATE_ID = "d-xyz template" # (must input your own SendGrid template)

MY_EMAIL_ADDRESS = "example@gmail.com" # (must input your own email that you want customers to see upon receiving a receipt.)
```

## Usage

1. In the command-line run the program

```sh
python shopping_cart.py
```

2. Input one or more product identifiers.

3. Input "DONE" to complete the transaction. A receipt will appear (Example Output in the section below).

### Example Output

``` sh
$ python shopping_cart.py
Please input a product identifier:1
Please input a product identifier:2
Please input a product identifier:DONE
#> ---------------------------------
#> FOODIEZ GROCER, INC.
#> 88 W 88TH ST, NEW YORK, NY 10024
#> WWW.NYU.EDU/DINING/FOODIEZ
#> ---------------------------------
#> CHECKOUT AT:  2019-06-16 09:56 AM
#> ---------------------------------
#> SELECTED PRODUCTS:
#> Chocolate Sandwich Cookies $3.50
#> All-Seasons Salt $4.99
#> ---------------------------------
#> SUBTOTAL:  $8.49
#> TAX (8.75%):  $0.74
#> TOTAL:  $9.23
#> ---------------------------------
#> THANK YOU! VISIT OUR WEBSITE TO LEARN HOW TO EARN FOODIEZ POINTS #> ON EVERY PURCHASE ;)
```
