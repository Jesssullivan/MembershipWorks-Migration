import pandas as pd


class MemberDF(object):

    def __init__(self,
                 start_date,
                 end_date,
                 paypal_df,
                 memershipworks_df,
                 membershipworks_import_fp):

        # this is where we'll keep track of members we have seen
        # while iterating through the paypal dataframe;
        # some members may appear multiple times, so we keep track as we go
        self.members = []

        # this is an empty dataframe we'll fill with values to import into membershipworks:
        self.memershipworks_df=memershipworks_df

        # we'll write out the membershipworks file here:
        self.membershipworks_import_fp=membershipworks_import_fp

        # this is a dataframe of values imported from paypal's csv:
        self.paypal_df = paypal_df
        print('loaded %d paypal records' % self.paypal_df.shape[0])

        # convert the date column values into python datetime objects:
        self.paypal_df['Date'] = pd.to_datetime(self.paypal_df['Date'])
        # print('converted `Date` column to datetime objects')

        # date range to export:
        self.start_date = start_date
        self.end_date = end_date

        # transactions below this value are discarded:
        self.min_net = 10

        # transactions above this threshold are "Extra" tier membership transactions
        self.standard_price = 35
        self.main()

    def main(self):
        # keep only rows from within the range we :
        dates_df = self.paypal_df[self.paypal_df['Date'] <= self.start_date]
        dates_df = dates_df[dates_df['Date'] >= self.end_date]

        print('kept %d records processed between %s and %s; discarded %d records' %
              (dates_df.shape[0],
               self.start_date.__format__('%d/%m/%y').__str__(),
               self.end_date.__format__('%d/%m/%y').__str__(),
               self.paypal_df.shape[0] - dates_df.shape[0]))

        # some members might make multiple transactions per month; only count transactions > $10.
        for idx, row in dates_df.iterrows():
            # make sure this is a valid row
            if type(row['From Email Address']) == str:
                # make sure this is a membership payment, not a lil donation stub
                if eval(row['Net']) > 10 and row['From Email Address'] not in self.members:
                    self.members.append(row['From Email Address'])
                    membership = \
                        'Offline Standard Membership' if eval(row['Net']) < self.standard_price \
                        else 'Offline Extra Membership'
                    join_date = self.end_date.__format__('%m/%d/%Y').__str__()
                    self.memershipworks_df.loc[row['From Email Address']] = row['Name'], row[
                        'From Email Address'], membership, join_date, join_date

    def to_csv(self):
        self.memershipworks_df.to_csv(self.membershipworks_import_fp)
        print('exported %d Standard Members and %d Extra Members to a membershipworks-readable format at %s' %
              (self.memershipworks_df[
                   self.memershipworks_df['Membership Level'] == 'Offline Standard Membership'].shape[
                   0],
               self.memershipworks_df[
                   self.memershipworks_df['Membership Level'] == 'Offline Extra Membership'].shape[0],
               self.membershipworks_import_fp))

