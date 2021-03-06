#! /usr/bin/env python2.7
# pylint: disable=relative-beyond-top-level
from ..DataTypes.QualityPerCycle import QualityPerCycle
from ..DataTypes.gcBias import gcBias

class databaseConnectorInterface(object):
    """Database connector interface for multiple database type support"""
    def addSequencingRun(self, run):
        raise NotImplementedError
    
    def addSample(self, sample):
        raise NotImplementedError

    def addProject(self, id):
        raise NotImplementedError

    def addSequencer(self, id):
        raise NotImplementedError

    def addCapturingKit(self, id, startDate = None, endDate = None):
        raise NotImplementedError

    def addAlignmentSummaryEntry(self, AlignmentSummaryMetrics):
        raise NotImplementedError

    def addFlagstatEntry(self, FlagstatMetric):
        raise NotImplementedError

    def addGCbiasEntry(self, gcBias):
        raise NotImplementedError

    def addHsMetric(self, HsMetric):
        raise NotImplementedError

    def addInsertSizeEntry(self, InsertSizeMetric):
        raise NotImplementedError

    def addQualityDistribution(self, QualityDistribution):
        raise NotImplementedError

    def addQualityByCycle(self, QualityByCycleObject): # type: (databaseConnectorInterface, QualityPerCycle) -> int
        raise NotImplementedError
    
    def addRunSummary(self, ID, Summary):
        raise NotImplementedError

    def exit(self):
        pass

