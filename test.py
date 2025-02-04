import requests
import os

splunk_url = 'https://httpbin.org'
#auth_token = 
#dashboard = 

def dashboard_data():
    # headers = {'Authorization': f'Splunk {auth_token}'}
    export_url = f'{splunk_url}'
    params = {'output_mode':'json'}
    
    response = requests.get(export_url,params=params)
    #print(response.text)
#print(dashboard_data()) 
    if response.status_code == 200:
        download_url = f'{splunk_url}?output_mode=pdf' 
        pdf_reponse = requests.get(download_url)  
        #print(pdf_reponse.status_code)
#         print(pdf_reponse.text)
# print(dashboard_data()) 
        if pdf_reponse.status_code == 200:
            print(pdf_reponse.status_code)
            pdf_path = 'splunk_dashboard.pdf'
            with open(pdf_path,'wb') as file:
                file.write(pdf_reponse.content)
            # with open(pdf_path,'r+') as file:
            #     print(file.readlines())
            return pdf_path
        else:
            print(f'Error downloading PDF:{pdf_reponse.status_code}')
            return None
    else:
        print(f"Error triggering exoprt: {response.status_code}")
        return None
print(dashboard_data())    
            