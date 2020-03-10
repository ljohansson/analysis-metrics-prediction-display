from __future__ import absolute_import, with_statement
import csv
from .parserTools import decomment, createQuickParser
from ..DataTypes.Files import Files
from ..DataTypes.QualityPerCycle import QualityPerCycle
from ..DataBase.SQLiteDatabaseConnector import sqlite3Database as DataBase

def parseQBCFile(file, sampleID, RunID):
    with open(file, u"r") as QBCFile:
        cycles = []
        quality = []

        reader = csv.DictReader(decomment(QBCFile), delimiter="\t")
        for row in reader:
            cycles.append(row["CYCLE"])
            quality.append(row["MEAN_QUALITY"])
    return QualityPerCycle(sampleID, RunID, cycles, quality)

def insertToDB(QBC, database):
    database.addQualityByCycle(QBC)

def main():
    parser = createQuickParser(["input", "database", "sample", "run"], "gets the HS metrics and adds them to sqlite db")
    args = parser.parse_args()
    dbc = DataBase(args.database)
    QBC = parseQBCFile(args.input, args.sample, args.run)
    insertToDB(QBC, dbc)
    dbc.exit()

if __name__ == '__main__':
    main()
