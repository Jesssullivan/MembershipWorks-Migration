import pandas as pd
import datetime

from member_df import MemberDF

# Converts a subscriber export csv from PayPal
# to bare-minimum member import csv for MembershipWorks.
# Written for Ithaca Generator by Jess Sullivan

# paypal csv obtained from `https://www.paypal.com/reports/statements/custom`
paypal_csv_fp = "./csv/paypal_export.CSV"
paypal_df = pd.read_csv(paypal_csv_fp)

# establish what one month ago was:
thisMonth = datetime.datetime.today()
lastMonth = thisMonth - datetime.timedelta(days=30)
priorMonth = lastMonth.replace(day=1) - datetime.timedelta(days=30)


if __name__ == "__main__":

    current_month_df = MemberDF(start_date=thisMonth,
                                end_date=lastMonth,
                                paypal_df=paypal_df,
                                memershipworks_df=pd.DataFrame(
                                    columns=['Name', 'Email', 'Membership Level', 'Join Date', 'Renewal Date']),
                                membershipworks_import_fp='./csv/membershipworks_import.csv'
                                )

    last_month_df = MemberDF(start_date=lastMonth,
                             end_date=priorMonth,
                             paypal_df=paypal_df,
                             memershipworks_df=pd.DataFrame(
                                 columns=['Name', 'Email', 'Membership Level', 'Join Date', 'Renewal Date']),
                             membershipworks_import_fp='./csv/membershipworks_import_pastmonth.csv'
                             )

    # write out some CSVs:
    current_month_df.to_csv()
    last_month_df.to_csv()
