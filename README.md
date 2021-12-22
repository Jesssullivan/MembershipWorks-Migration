## MembershipWorks-Migration

Converts a subscriber export csv from PayPal to bare-minimum member import csv for MembershipWorks.

*Obtain a subscriber export from PayPal:*
- visit [paypal.com/reports/statements/custom](https://www.paypal.com/reports/statements/custom)
- Download the CSV export as `./paypal_export.CSV`


#### *create a new environment:*
```
python3 -m venv ig_venv
source ig_venv/bin/activate
pip3 install -r requirements.txt
````

#### *Run it:*
```
python3  paypal_to_membershipworks.py 
```

#### Notes:
Not yet sure what the best method is to automatically renew and monitor grandfathered-in paypal accounts from MembershipWorks.
