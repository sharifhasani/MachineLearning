from pandas.core import series
from pandas.core.frame import DataFrame


class classification:
    def FindDiffrentValue(self, series:series):
        values = set()
        for item in series:
            values.add(item)
        return len(values)

    def Classifier(self, df:DataFrame):
        valuesLen = {}
        result = []
        for colname in df:
            valuesLen[colname] = self.FindDiffrentValue(df[colname])
            if valuesLen[colname] < 5:
                result.append(colname)
        return result

    def BinaryClassifier(self, df:DataFrame):
        valuesLen = {}
        result = []
        for colname in df:
            valuesLen[colname] = self.FindDiffrentValue(df[colname])
            if valuesLen[colname] == 2:
                result.append(colname)
        return result
