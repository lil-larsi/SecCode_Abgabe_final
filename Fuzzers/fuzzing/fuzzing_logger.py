import matplotlib.pyplot as plt
import os
import numpy as np

class Logger():
    def __init__(self, fuzzer, runner):
        self.fuzzer = fuzzer
        self.runner = runner
        self.line_coverage = []
        self.branch_coverage = []
        self.call_coverage = []
        self.crashes = 0
        self.crashes_endnumber = 0
        self.passes=0
        self.unresolveds=0
        self.crashfiles=[]
        self.get_information()

    def get_information(self):
        self.line_coverage = self.runner.return_line_coverage()
        self.branch_coverage = self.runner.return_branch_coverage()
        self.call_coverage = self.runner.return_call_coverage()
        self.crashes = self.runner.return_crashes_array()
        self.crashes_endnumber=self.runner.return_outcome_fail()
        self.passes=self.runner.return_outcome_pass()
        self.unresolveds=self.runner.return_outcome_unresolved()
        self.executions = len(self.call_coverage)
        self.timestamp = self.runner.return_timestamp()
        self.start_timestamp = self.timestamp[0]
        self.crashfiles = self.runner.return_crashfile()
        self.config_timestamp()

    def config_timestamp(self):
        for i in range(len(self.timestamp)):
            self.timestamp[i] = (self.timestamp[i] - self.start_timestamp) / (60) 

    def plot(self, path):
        i=0
        for item in self.crashfiles:
            i = i+1
            path_crashfiles=os.path.join(path,'crashes_'+ str(i))
            with open(path_crashfiles, 'wb') as fp:
                fp.write(item)
                
        path_line_cov = os.path.join(path, 'line_coverage.svg')
        print(path_line_cov)
        path_branch_cov = os.path.join(path, 'branch_coverage.svg')
        path_statement_cov = os.path.join(path, 'statement_coverage.svg')
        path_overall_cov = os.path.join(path, 'overall_coverage.svg')
        path_crashes = os.path.join(path, 'crashes.svg')
        print("Executions: "+ str(self.executions))
        exec_per_sec30min = self.executions/(30*60)
        print("\nExecutions per sec für 30min: " + str(exec_per_sec30min))
        print("\nOutcome Pass: "+ str(self.passes))
        print("\nOutcome Fail(Crash): "+ str(self.crashes_endnumber))
        print("\nOutcome Unresolved: "+ str(self.unresolveds))
        plt.figure()
        plt.ylabel("Line Coverage in %")
        plt.xlabel("Zeit in min")
        plt.axis([0, 30, 0,100])
        plt.plot(self.timestamp, self.line_coverage)
        plt.legend(['Line Coverage'])
        plt.savefig(path_line_cov, format='svg')
        plt.clf()
        plt.figure()
        plt.ylabel("Branch Coverage in %")
        plt.xlabel("Zeit in min")
        plt.axis([0, 30, 0,100])
        plt.plot(self.timestamp, self.branch_coverage)
        plt.legend(['Branch Coverage'])
        plt.savefig(path_branch_cov, format='svg')
        plt.clf()
        plt.figure()
        plt.ylabel("Statement Coverage in %")
        plt.xlabel("Zeit in min")
        plt.axis([0, 30, 0,100])
        plt.plot(self.timestamp, self.call_coverage)
        plt.legend(['Statement Coverage'])
        plt.savefig(path_statement_cov, format='svg')
        plt.clf()
        plt.figure()
        plt.ylabel("Coverages in %")
        plt.xlabel("Zeit in min")
        plt.axis([0, 30, 0,100])
        plt.plot(self.timestamp, self.line_coverage)
        plt.plot(self.timestamp, self.branch_coverage)
        plt.plot(self.timestamp, self.call_coverage)
        plt.legend(['Line Coverages', 'Branch Coverage', 'Statement Coverage'])
        plt.savefig(path_overall_cov, format='svg')
        plt.clf()
        if max(self.crashes) > 0:
            plt.figure()
            plt.ylabel("Anzahl an Crashes")
            plt.xlabel("Zeit in min")
            plt.axis([0, 30, 0, max(self.crashes)])
            plt.plot(self.timestamp, self.crashes)
            plt.legend(['Crashes'])
            plt.savefig(path_crashes, format='svg')
            plt.clf()
