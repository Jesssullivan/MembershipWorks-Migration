import pandas as pd
import datetime

# Converts a subscriber export csv from PayPal
# to bare-minimum member import csv for MembershipWorks.
# Written for Ithaca Generator Jess Sullivan

# membershipworks csv column headers:
membershipworks_csv_fp = "./membershipworks_import_head.csv"
membershipworks_csv_df = pd.read_csv(membershipworks_csv_fp)
membershipworks_import_fp = './membershipworks_import.csv'

# paypal csv obtained from `https://www.paypal.com/reports/statements/custom`
paypal_csv_fp = "./paypal_export.CSV"
paypal_csv_df = pd.read_csv(paypal_csv_fp)
print('loaded %d records from %s' % (paypal_csv_df.shape[0], paypal_csv_fp))

# convert the Date column strings into datetime64 objects
paypal_csv_df['Date'] = pd.to_datetime(paypal_csv_df['Date'])

# establish what one month ago was:
today = datetime.datetime.today().replace(day=1)
lastMonth = today - datetime.timedelta(days=1)

# keep only rows from the last month:
current_month_df = paypal_csv_df[paypal_csv_df['Date'] >= lastMonth]
print('kept %d records processed within one month of today, %s; discarded %d older records' %
      (current_month_df.shape[0], today.__format__('%d/%m/%y').__str__(),
       paypal_csv_df.shape[0] - current_month_df.shape[0]))

if __name__ == "__main__":
    for idx, row in current_month_df.iterrows():
        if type(row['From Email Address']) == str:
            membership = 'Offline Standard Membership' if eval(row['Net']) < 35 else 'Offline Extra Membership'
            join_date = lastMonth.__format__('%m/%d/%Y').__str__()
            membershipworks_csv_df.loc[idx] = row['Name'], row['From Email Address'], membership, join_date, join_date

    # export the csv for membershipworks to interpret:
    membershipworks_csv_df.to_csv(membershipworks_import_fp)
    print('exported %d Standard Members and %d Extra Members to a membershipworks-readable format at %s' %
          (membershipworks_csv_df[membershipworks_csv_df['Membership Level'] == 'Offline Standard Membership'].shape[0],
           membershipworks_csv_df[membershipworks_csv_df['Membership Level'] == 'Offline Extra Membership'].shape[0],
           membershipworks_import_fp))
