## MembershipWorks-Migration

Converts a subscriber export csv from PayPal to bare-minimum member import csv for MembershipWorks.

*Obtain a subscriber export from PayPal:*
- visit [paypal.com/reports/statements/custom](https://www.paypal.com/reports/statements/custom)
- Download the CSV export as `./csv/paypal_export.CSV`


#### *create a new environment:*
```
python3 -m venv ig_venv
source ig_venv/bin/activate
pip3 install -r requirements.txt
````

#### *Run it:*
```
 python3 src/convert.py
 ```

#### *...If all goes well, the output will look something like:*
```
#> loaded **** paypal records
#> kept ** records processed between 23/12/21 and 23/11/21; discarded **** records
#> loaded **** paypal records
#> kept *** records processed between 23/11/21 and 02/10/21; discarded *** records
#> exported ** Standard Members and ** Extra Members to a membershipworks-readable format at ./csv/membershipworks_import.csv
#> exported ** Standard Members and ** Extra Members to a membershipworks-readable format at ./csv/membershipworks_import_pastmonth.csv
```

#### Notes:
- Not yet sure what the best method is to automatically renew and monitor grandfathered-in paypal accounts from MembershipWorks
