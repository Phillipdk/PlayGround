""" 
This test is to test the API call and see if it works. It is an 
integration test.
"""

import os
import requests
import json

# Insert your company information
client_id = os.environ.get('CLIENT_ID')
client_secret = os.environ.get('CLIENT_SECRET')
componentId = os.environ.get('COMPONENT_ID')

print(client_id)
print(client_secret)
print(componentId)

######################### Connection details #########################
base_url = "https://edrmedesoapiservice.azurewebsites.net/"
req_type = {"Content-Type": "application/json"}

# First Get token. You need to provide client_id and client_secret:
token_url = "https://login.microsoftonline.com/edrmedesob2c.onmicrosoft.com/oauth2/v2.0/token"
payload='grant_type=client_credentials&client_id=' + client_id + '&scope=https%3A%2F%2Fedrmedesob2c.onmicrosoft.com%2Fapi%2F.default&client_secret=' + client_secret

headers = {'Content-Type': 'application/x-www-form-urlencoded'}
response = requests.request("GET", token_url, headers=headers, data=payload)

# Save the token
token = response.text


######################## Specify input for Gear Damage ##############################
payload ={
	"componentId": componentId,  
	"data":{
        "gear_type":"bevel",
        "initial_data":{
                "Sigma":90.00,
                "a":0.0,
                "z_1":14,
                "z_2":39,
                "d_e2":176.893,
                "b_2":25.4,
                "beta_m2":35,
                "r_c0":114.3,
                "z_0":0,
                "alpha_dD":20,
                "alpha_dC":20,
                "f_alphalim":0,
                "c_ham":0.24737,
                "k_d":2.0,
                "k_c":0.125,
                "k_t":0.0915,
                "j_en":0.127,
                "theta_a2":2.1342,
                "theta_f2":6.4934,
                "rho_a01D":0.8,
                "rho_a01C":0.8,
                "rho_a02D":1.2,                    
                "rho_a02C":1.2,
                "s_pr1D":0,
                "s_pr1C":0,
                "s_pr2D":0,
                "s_pr2C":0},
        "additional_data":{
                "material":1,
                "sigma_H_lim":1500,
                "sigma_F_lim":480,
                "Rz_1":8,
                "Rz_2":8,
                "Rz_f1":16,
                "Rz_f2":16,
                "f_pt1":12,
                "f_pt2":26,
                "rho":7.86e-6,
                "nu_40":150
            },
        "operation_parameters":
            {"T_1":300,"n_1":1200,"K_A":1.1,"N_1":0}
        }
    }


##################### Sending and Getting the simulation results ###############
# Sending data to the module. You need to provide module name and component ID with the data
url = "{}gear-damage?token={}".format(base_url, token)
response = requests.request("POST", url, headers=req_type, data=json.dumps(payload))
print(response.text)

# Getting the results
payload["timestamp"] = json.loads(response.text)["timestamp"]
url = "{}GetResultByTimeStamp?token={}".format(base_url, token)
response = requests.request('GET', url, headers=req_type, data=json.dumps(payload))
print(response.text)

# Making pretty
result_dict = json.loads(response.text)
result_json = json.dumps(result_dict, indent=4)


