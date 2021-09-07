# Standard library imports
import sys
import json

# Devpay imports
import devpay_client
from devpay_client import DevpayClient
from devpay_client import Config

def main():
   paymentDetails = { "amount":132,
                "card":{"cardNum":"XXXX111111000000",
                			  "cardExpiryMonth":"10",
                        "cardExpiryYear":"2024",
                        "cvv":"102"},
                "billingAddress":{"country":"US",
                                    "zip":"38138",
                                    "state":"TN",
                                    "street":"123 ABC Lane",
                                    "city":"Memphis"}
               }

   config = Config(accountId="accountId",
        accessKey="accessKey")
   config.debug = True
   config.sandbox = True
   
   devpayClient = DevpayClient(config)
   try:
     status = devpayClient.confirmPayment(paymentDetails)
     print("Payment status - ",status)
   except Exception as e:
     print("Error - ",e)

if __name__ == "__main__":
    main()
