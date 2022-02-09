import urllib.parse;
import requests as rq;
import json;
# import keepa
apiKey = "8ha1s159q6svbqm9n2qd1toe9uhh3g4st0nl3vrhfs667rjhd6p779gp3hsqhcf5";

class Keepa:
    url = None;
    headUrl = "https://api.keepa.com/query?";
    urlEncoded = None;
    urlOpt = {};
    def __init__(self, url):
        self.url = url;


    # def DecodeUrl(self):
    #     self.url = urllib.parse.unquote(self.url);
    #     tempParams = self.url.split("?")[1].split("&");
    #     for i in range(len(tempParams)):
    #         self.urlOpt[tempParams[i].split("=")[0]] = tempParams[i].split("=")[1];
    #     self.urlOpt["selection"] = json.loads(self.urlOpt["selection"]);
    # def EncodeUrl(self):
    #     self.urlEncoded = self.headUrl+urllib.parse.urlencode(self.urlOpt)
    def GetProducts(self, max:int = 10000):
        index = self.url.find("perPage")
        self.url[index:index+13] = str(max);

        # self.EncodeUrl();
        
        return self.urlEncoded;
        # return rq.get(self.urlEncoded).json();
keepa:Keepa = Keepa("https://api.keepa.com/query?key=8ha1s159q6svbqm9n2qd1toe9uhh3g4st0nl3vrhfs667rjhd6p779gp3hsqhcf5&domain=2&selection=%7B%2"+"2current_SALES_gte%2"+"2%3A1%2C%2"+"2current_SALES_lte%2"+"2%3A10000%2C%2"+"2rootCategory%"+"22%3A340831031%2C%2"+"2sort%"+"22%3A%5B%5B%"+"22current_SALES%"+"22%2C%"+"22asc%"+"22%5D%5D%2C%22productType%"+"22%3A%5B0%2C1%5D%2C%22perPage%"+"22%3A100%2C%22page%"+"22%3A0%7D") 
keepa.DecodeUrl();
print(keepa.urlOpt);
print();
print(keepa.GetProducts(max = 10000));
# keepa.DecodeUrl();
print();
print(keepa.url);
# api = keepa.Keepa(apiKey)

# params = {
#     "page": 0,
#     "domainId": 1
# }
# deals  = api.deals(params)

# print(deals, len(deals))

"""
https://api.keepa.com/query?key=8ha1s159q6svbqm9n2qd1toe9uhh3g4st0nl3vrhfs667rjhd6p779gp3hsqhcf5&domain=2&selection=%7B%22current_SALES_gte
%22%3A1%2C%22current_SALES_lte%22%3A10000%2C%22rootCategory%22%3A340831031%2C%22sort%22%3A%5B%5B%22current_SALES%22%2C%22asc%22%5D%5D%2C%22
productType%22%3A%5B0%2C1%5D%2C%22perPage%22%3A10000%2C%22page%22%3A0%7D
"""

"""
https://api.keepa.com/query?key=8ha1s159q6svbqm9n2qd1toe9uhh3g4st0nl3vrhfs667rjhd6p779gp3hsqhcf5&domain=2&selection={"current_SALES_gte
":1,"current_SALES_lte":10000,"rootCategory":340831031,"sort":[["current_SALES","asc"]],"
productType":[0,1],"perPage":100,"page":0}
"""