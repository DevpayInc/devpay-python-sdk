import requests
import logging

API_ENDPOINTS = {
                'DEVPAY':"https://api.devpay.io"
                }

class RestClient:
    def __init__(self, config):
        self.config = config

        if config.debug:
            logging.basicConfig(level=logging.INFO)

    def createPaymentIntentResponse(self, paymentDetail):
        card = paymentDetail["card"]
        cardDetails = {
            "Number":card["cardNum"],
            "ExpMonth":card["cardExpiryMonth"],
            "ExpYear":card["cardExpiryYear"],
            "Cvc":card["cvv"]
        }

        chargeDetails = {
            "amount":paymentDetail["amount"],
            "fee_amount":0,
            "description":paymentDetail.get("description",""),
            "account_id":self.config.accountId,
            "secreate_key":self.config.accessKey
        }

        if self.config.sandbox:
            chargeDetails["environment"] = "sandbox"

        payload = {
            "CardDetails": cardDetails,
            "ChargeDetails": chargeDetails
        }

        uri = API_ENDPOINTS['DEVPAY']
        uri = uri+'/v1/charge/create_Intend'
        logging.info("Reqeust - POST - %s, Data - %s ",uri,str(payload))

        response = requests.post(uri,
            json=payload,
            headers={"Content-Type":"application/json", 'User-Agent': 'dev-pay client'}
            )
        logging.info("Response - %s",response.text)
        return response

    def confirmIntentResponse(self,token, paymentDetail):
        card = paymentDetail["card"]
        cardDetails = {
            "Number":card["cardNum"],
            "ExpMonth":card["cardExpiryMonth"],
            "ExpYear":card["cardExpiryYear"],
            "Cvc":card["cvv"],
            "token":token
        }
        
        chargeDetails = {
            "amount":paymentDetail["amount"],
            "fee_amount":0,
            "description":paymentDetail.get("description",""),
            "account_id":self.config.accountId,
            "secreate_key":self.config.accessKey
        }

        if self.config.sandbox:
            chargeDetails["environment"] = "sandbox"

        payload = {
            "CardDetails": cardDetails,
            "ChargeDetails": chargeDetails
        }

        uri = API_ENDPOINTS['DEVPAY']
        uri = uri+'/v1/charge/confirm_charge'
        logging.info("Reqeust - POST - %s, Data - %s ",uri,str(payload))

        response = requests.post(uri,
            json=payload,
            headers={"Content-Type":"application/json", 'User-Agent': 'dev-pay client'}
            )
        logging.info("Response - %s",response.text)
        return response
