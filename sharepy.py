# from sharepoint import SharePointSite, basic_auth_opener

# server_url = "https://laureatena.sharepoint.com/sites/psid-ueld/"
# opener = basic_auth_opener(server_url, "lau.corp\jose.perdomo@laureate.net", "Phoenix01")
# site = SharePointSite(server_url, opener)

# sp_list = site.lists['CourseInventory']
# for row in sp_list.rows:
#    print row.id, row.Title, row.Author['name'], row.Created, row.EncodedAbsUrl

from haufe.sharepoint import Connector

url = 'https://laureatena.sharepoint.com/sites/psid-ueld/'
username = 'LAU.CORP\\jose.perdomo@laureate.net'
password = 'Phoenix0asda1'
list_id = '4AE20C22-6195-46C9-AA85-8C4384F84397'
# https://laureatena.sharepoint.com/sites/psid-ueld/_layouts/15/listedit.aspx?List=%7B 4AE20C22-6195-46C9-AA85-8C4384F84397 %7D
service = Connector(url, username, password, list_id)
# all_fields = service.all_fields
# from sharepoint import SharePointSite
# from sharepoint.auth import PreemptiveBasicAuthHandler
# from ntlm import HTTPNtlmAuthHandler
# import urllib2

# server_url = "https://laureatena.sharepoint.com/"
# site_url = server_url + "sites/psid-ueld/"

# password_manager = urllib2.HTTPPasswordMgrWithDefaultRealm()
# password_manager.add_password(None, server_url, "hnsc/jose.perdomo@laureate.net", "Phoenix01")
# auth_handler = HTTPNtlmAuthHandler.HTTPNtlmAuthHandler(password_manager)
# opener = urllib2.build_opener(auth_handler)


# site = SharePointSite(site_url, opener)

# for sp_list in site.lists:
#     print sp_list.id, sp_list.meta['Title']