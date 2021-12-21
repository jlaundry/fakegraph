
import argparse
import json
import uuid
from faker import Faker
from datetime import datetime

faker = Faker(['en-US']) #, 'ja-JP', 'ru_RU', 'it_IT', 'de_DE', 'pt_BR'])


COMPANIES = [
    ("Contoso", "contoso.com", 0.9),
    ("Trey Research", "treyresearch.net", 0.1),
]

PARTNERS = [
    ("AdventureWorks", "adventure-works.com"),
    ("Blue Yonder Airlines", "blueyonderairlines.com"),
    ("Fabrikam", "fabrikam.com"),
    ("Northwind Traders", "northwindtraders.com"),
    ("TAILSPIN", "tailspintoys.com"),
]



def create_users(args, company="Contoso", domain="contoso.com", msdomain="contoso.onmicrosoft.com"):
    user_db = []

    for n in range(0, args.people):
        uid = str(uuid.uuid4())

        first_name = faker.first_name()
        last_name = faker.last_name()
        
        username = f"{first_name[0]}{last_name}".lower()
        usercreated = f"{datetime.utcnow().isoformat()}Z"

        user_db.append({
            "id": uid,
            "deletedDateTime": None,
            "accountEnabled": True,
            "ageGroup": None,
            "businessPhones": [],
            "city": None,
            "createdDateTime": usercreated,
            "creationType": None,
            "companyName": company,
            "consentProvidedForMinor": None,
            "country": None,
            "department": None,
            "displayName": f"{first_name} {last_name}",
            "employeeId": None,
            "employeeHireDate": None,
            "employeeType": None,
            "faxNumber": None,
            "givenName": first_name,
            "imAddresses": [],
            "infoCatalogs": [],
            "isManagementRestricted": None,
            "isResourceAccount": None,
            "jobTitle": None,
            "legalAgeGroupClassification": None,
            "mail": f"{username}@{domain}",
            "mailNickname": username,
            "mobilePhone": None,
            "onPremisesDistinguishedName": None,
            "officeLocation": None,
            "onPremisesDomainName": None,
            "onPremisesImmutableId": None,
            "onPremisesLastSyncDateTime": None,
            "onPremisesSecurityIdentifier": None,
            "onPremisesSamAccountName": None,
            "onPremisesSyncEnabled": None,
            "onPremisesUserPrincipalName": None,
            "otherMails": [
                f"{username}@{domain}",
            ],
            "passwordPolicies": None,
            "postalCode": None,
            "preferredDataLocation": None,
            "preferredLanguage": None,
            "proxyAddresses": [],
            "refreshTokensValidFromDateTime": usercreated,
            "showInAddressList": None,
            "signInSessionsValidFromDateTime": usercreated,
            "state": None,
            "streetAddress": None,
            "surname": last_name,
            "usageLocation": None,
            "userPrincipalName": f"{username}@{domain}",
            "externalUserConvertedOn": None,
            "externalUserState": None,
            "externalUserStateChangeDateTime": None,
            "userType": "Member",
            "employeeOrgData": None,
            "passwordProfile": None,
            "assignedLicenses": [],
            "assignedPlans": [],
            "deviceKeys": [],
            "identities": [
                {
                    "signInType": "userPrincipalName",
                    "issuer": msdomain,
                    "issuerAssignedId": f"{username}@{domain}"
                }
            ],
            "onPremisesExtensionAttributes": {
                "extensionAttribute1": None,
                "extensionAttribute2": None,
                "extensionAttribute3": None,
                "extensionAttribute4": None,
                "extensionAttribute5": None,
                "extensionAttribute6": None,
                "extensionAttribute7": None,
                "extensionAttribute8": None,
                "extensionAttribute9": None,
                "extensionAttribute10": None,
                "extensionAttribute11": None,
                "extensionAttribute12": None,
                "extensionAttribute13": None,
                "extensionAttribute14": None,
                "extensionAttribute15": None
            },
            "onPremisesProvisioningErrors": [],
            "provisionedPlans": []
        })

    return user_db

def create_guests(args, company="Fabrikam", domain="fabrikam.com", msdomain="contoso.onmicrosoft.com"):
    guest_db = []

    for n in range(0, args.guests):
        uid = str(uuid.uuid4())

        first_name = faker.first_name()
        last_name = faker.last_name()
        country = "NZ"
        
        username = f"{first_name[0]}{last_name}".lower()
        usercreated = f"{datetime.utcnow().isoformat()}Z"

        guest_db.append({
            "id": uid,
            "userPrincipalName": f"{username}_{domain}#EXT#@{msdomain}",
            "employeeId": None,
            "accountEnabled": True,
            "createdDateTime": usercreated,
            "displayName": f"{first_name} {last_name}",
            "givenName": first_name,
            "surname": last_name,
            "jobTitle": None,
            "department": None,
            "companyName": company,
            "userType": "Guest",
            "mail": f"{username}@{domain}",
            "otherMails": [
                f"{username}@{domain}",
            ],
            "mobilePhone": None,
            "businessPhones": [],
            "externalUserState": "Accepted",
            "externalUserStateChangeDateTime": usercreated,
            "isResourceAccount": None,
            "lastPasswordChangeDateTime": usercreated,
            "onPremisesDistinguishedName": None,
            "onPremisesDomainName": None,
            "onPremisesImmutableId": None,
            "onPremisesLastSyncDateTime": None,
            "onPremisesSamAccountName": None,
            "onPremisesSecurityIdentifier": None,
            "onPremisesUserPrincipalName": None,
            "passwordPolicies": None,
            "refreshTokensValidFromDateTime": usercreated,
            "signInSessionsValidFromDateTime": usercreated,
            "usageLocation": country,
            "preferredName": ""
        })

    return guest_db

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate user data.')

    parser.add_argument(
        '--people',
        type=int,
        default=500,
        help='Number of users'
    )
    parser.add_argument(
        '--guests',
        type=int,
        default=750,
        help='Number of guest users'
    )
    args = parser.parse_args()
    print(f"Creating users.json with {args.people} users and {args.guests} guests")

    DB = []

    DB = DB + create_users(args)
    DB = DB + create_guests(args)

    with open('data/users.json', 'w') as outfile:
        json.dump(DB, outfile, indent=4)