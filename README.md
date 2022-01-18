## MembershipWorks-Migration

#### The objectives of this notebook and its scripts are:
- Merge PayPal & Membershipworks members in a sorta intelligent way to create kinda accurate financial reports
- Convert a PayPal transaction export into an upsert-able csv to import into membershipworks
- Keep tabs on PayPal memberships as they become deprecated

*Obtain a subscriber export from PayPal:*
- visit [paypal.com/reports/statements/custom](https://www.paypal.com/reports/statements/custom)
- Download the CSV export as `./csv/paypal_export.CSV`


*Obtain a member export from membershipworks:*
- Download the CSV export as `./csv/mw_export.CSV`

#### *create a new environment:*
```
python3 -m venv ig_venv
source ig_venv/bin/activate
pip3 install -r requirements.txt
```


```
# do the rest in jupyter notebook:
cp financial_vis.void financial_vis.ipynb
jupyter lab # ...
```


#### *...If all goes well, the output will look something like:*
```
loaded **** paypal records
loaded ** existing membershipworks records
converted Date column to datetime objects
kept *** records processed between 01/01/22 and 22/11/21; discarded **** records
discarded **'s Donation Payment record for **, continuing...
discarded **'s PreApproved Payment Bill User Payment record for **, continuing...
** ** already in member list! continuing...
discarded ** **'s Payment Refund record for -**.00, continuing...
discarded ** **'s Donation Payment record for **.00, continuing...
exported: ** Members! 
 - ** Standard Members 
 - ** Offline Standard Members 
 - ** Extra Members 
 - ** Offline Extra Members 
 ...to a membershipworks-readable format at ./csv/membershipworks_import.csv
```

