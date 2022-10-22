import pandas as pd
import logging


class Report:
    def __init__(self, data: str):
        try:
            self._df = pd.read_json(data)
            self._df_report = pd.DataFrame()
        except ValueError as err:
            logging.exception('data is not a valid JSON')
            raise

    def __repr__(self):
        pd.set_option("display.max_rows", None, "display.max_columns", None)
        return repr(self._df_report)

    def aggregate_df(self) -> None:
        assert self._df_report.empty, "Expected an empty dataframe"
        self._df_report['aggregated_success'] = self._df.groupby(['application', 'version'], group_keys=False).agg({'success_count': ['sum']})
        self._df_report['aggregated_requests'] = self._df.groupby(['application', 'version'], group_keys=False).agg({'requests_count': ['sum']})
        self._df_report['success_rate'] = 100 * self._df_report['aggregated_success'] / self._df_report.groupby(['application', 'version'])['aggregated_requests'].transform('sum')
        self._df_report = self._df_report.reset_index()
        self._df_report.drop(['aggregated_success', 'aggregated_requests'], axis=1, inplace=True)


if __name__ == '__main__':
    r = Report('../data/output.json')
    r.aggregate_df()
    print(r)
