#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Version: 0.1a1
# Owner: Ruslan Korniichuk

import luigi
from luigi.contrib.external_program import ExternalProgramTask


class Task1(ExternalProgramTask):

    dst = 'task1'

    def program_args(self):
        return ['touch', self.dst]

    def output(self):
        return luigi.LocalTarget(self.dst)


class Task2(luigi.Task):

    def requires(self):
        return Task1()

    def run(self):
        dst = self.input().path
        with open(dst, 'a') as f:
            f.write('task2')


if __name__ == '__main__':
    luigi.run()
