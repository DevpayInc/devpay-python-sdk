from rest_client import RestClient

class Config:
    def __init__(self,accountId, accessKey):
        self.accountId = accountId
        self.accessKey = accessKey
        self.debug = False
        self.sandbox = False

class DevpayClient:
  def __init__(self, config):
    self.config = config
    self.restClient = RestClient(config)

  def confirmPayment(self, paymentDetails):

    response = self.restClient.createPaymentIntentResponse(paymentDetails)
    token = response.json()["token"]

    token_resp = self.restClient.confirmIntentResponse(token, paymentDetails)
    status = (token_resp.json()["status"] == 1)
    return status