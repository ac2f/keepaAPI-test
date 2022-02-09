import urllib.parse;
import requests as rq;
import json;
import keepa
import numpy as np;
class Keepa:
    url = None;
    urlDecoded = None;
    keepa = None;
    apiKey = None;
    asinList = [];
    def __init__(self, url, apiKey):
        self.url = url;
        self.apiKey = apiKey;
        self.keepa = keepa.Keepa(self.apiKey);

    def ConcatAllKeys(self):
        last = {};
        data = self.UrlParamAsJson();
        for key in data:
            if (not key in ["selection", "key"] ): last[key] = data[key];
        for key in data["selection"]:
            itemData = data["selection"][key];
            if (type(itemData) == type([0,])):
                last[key] = itemData[0];
                continue;
            last[key] = itemData;
        return last;
    def UrlParamAsJson(self):
        self.DecodeUrl();
        urlOpt = {};
        tempParams = self.url.split("?")[1].split("&");                            
        for i in range(len(tempParams)):                                           
            urlOpt[tempParams[i].split("=")[0]] = tempParams[i].split("=")[1];
        urlOpt["selection"] = json.loads(urllib.parse.unquote(urlOpt["selection"]));           
        return urlOpt;
    def DecodeUrl(self):
       self.urlDecoded = urllib.parse.unquote(self.url);

        # self.url = urllib.parse.unquote(self.url);                                       
        # tempParams = self.url.split("?")[1].split("&");                                  
        # for i in range(len(tempParams)):                                                 
        #     self.urlOpt[tempParams[i].split("=")[0]] = tempParams[i].split("=")[1];      
        # self.urlOpt["selection"] = json.loads(self.urlOpt["selection"]);                 
    # def EncodeUrl(self):                                                               
    #     self.urlEncoded = self.headUrl+urllib.parse.urlencode(self.urlOpt)             
    def GetProducts(self, max:int = 10000):
        index = self.url.find("perPage");
        self.url = self.url[:index+13] + str(max) + self.url[index+16:];
        self.asinList = rq.get(self.url).json()["asinList"];
        return self.asinList;
    def GetProductsData(self):
        return self.keepa.query(np.asarray(self.asinList));
    def GetProductData(self, productId:str):
        return self.keepa._product_query();
keepaCustom:Keepa = Keepa("https://api.keepa.com/query?key=8ha1s159q6svbqm9n2qd1toe9uhh3g4st0nl3vrhfs667rjhd6p779gp3hsqhcf5&domain=2&selection=%7B%2"+"2current_SALES_gte%2"+"2%3A1%2C%2"+"2current_SALES_lte%2"+"2%3A10000%2C%2"+"2rootCategory%"+"22%3A340831031%2C%2"+"2sort%"+"22%3A%5B%5B%"+"22current_SALES%"+"22%2C%"+"22asc%"+"22%5D%5D%2C%22productType%"+"22%3A%5B0%2C1%5D%2C%22perPage%"+"22%3A100%2C%22page%"+"22%3A0%7D", "8ha1s159q6svbqm9n2qd1toe9uhh3g4st0nl3vrhfs667rjhd6p779gp3hsqhcf5");
keepaCustom.GetProducts(max = 100);
data = keepaCustom.GetProductsData();
print(data[98].keys()); ## kullanılabilir anahtarlar

#dict_keys(['csv', 'categories', 'imagesCSV', 'manufacturer', 'title', 'lastUpdate', 'lastPriceChange', 'rootCategory', 'productType', 'parentAsin', 
# 'variationCSV', 'asin', 'domainId', 'type', 'hasReviews', 'trackingSince', 'brand', 'productGroup', 'partNumber', 'model', 'color', 'size', 'edition', 
# 'format', 'packageHeight', 'packageLength', 'packageWidth', 'packageWeight', 'packageQuantity', 'isAdultProduct', 'isEligibleForTradeIn', 
# 'isEligibleForSuperSaverShipping', 'offers', 'buyBoxSellerIdHistory', 'isRedirectASIN', 'isSNS', 'author', 'binding', 'numberOfItems', 
# 'numberOfPages', 'publicationDate', 'releaseDate', 'languages', 'lastRatingUpdate', 'ebayListingIds', 'lastEbayUpdate', 'eanList', 'upcList', 
# 'liveOffersOrder', 'frequentlyBoughtTogether', 'features', 'description', 'promotions', 'newPriceIsMAP', 'coupon', 'availabilityAmazon', 'listedSince', 
# 'fbaFees', 'variations', 'itemHeight', 'itemLength', 'itemWidth', 'itemWeight', 'salesRankReference', 'salesRanks', 'salesRankReferenceHistory', 'launchpad', 
# 'isB2B', 'stats', 'offersSuccessful', 'g', 'categoryTree', 'data'])

#print(keepaCustom.ConcatAllKeys())
# print(keepaCustom.GetProducts(max = 100));

# keepa.DecodeUrl();
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