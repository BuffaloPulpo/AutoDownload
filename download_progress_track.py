from main import download_data
from rapid7_downloads import *

list_ports_national_exposure_TCP = ["_5.",  "_21.", "_22.", "_23.", "_25.", "_53.", "_80.", "_81.", "_110.",
                                    "_135.",  "_139.", "_143.", "_389.",
                                    "_443.", "_445.", "_465.", "_587.", "_990.", "_993.",
                                    '_995.', "_1433.", "_1521.", "_1723.", "_3306.", "_3389.", "_5000.",
                                    "_5432.", "_5900.", "_6379.", "_8080.", "_8081.", "_8443.", "_8888.",
                                    "_9100.", "_11211.", "_27017.", "_50000.", "_61439."]
list_ports_national_exposure_UDP = ["_19.", "_53.", "_123.", "_137.", '_389',  "_1900.", "_5060.", "_5353.", '_11211.']

print(len(list_ports_national_exposure_TCP))
print(len(list_ports_national_exposure_UDP))

# for each in list_ports_national_exposure_TCP:
#     download_data(each)


