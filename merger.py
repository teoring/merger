#!/usr/bin/env python3

import os
import argparse

from subprocess import call

def build_difference(fbranch, froot, fhead, sbranch, sroot, shead):
    get_changelist(fbranch, froot, fhead)
    get_changelist(sbranch, sroot, shead)

    fchangelist = read_changelist(fbranch)
    schangelist = read_changelist(sbranch)

    diff(fbranch, fchangelist, sbranch, schangelist)

def diff(fbranch, fchange_list, sbranch, schange_list):
    fbranch_unique_commits = []
    sbranch_unique_commits = []

    for line in fchange_list:
        found = False
        for line2 in schange_list:
            if line == line2:
                found = True

        if found == False:
            fbranch_unique_commits.append(line)

    for line in schange_list:
        found = False
        for line2 in fchange_list:
            if line == line2:
                found = True

        if found == False:
            sbranch_unique_commits.append(line)

    print("#####################################################################\n")
    print("Unique commits in " + fbranch + " :\n")
    for line in fbranch_unique_commits:
        print(line + "\n")

    print("#####################################################################\n")
    print("Unique commits in " + sbranch + " :\n")
    for line in sbranch_unique_commits:
        print(line + "\n")

def read_changelist(branch):
    lines = []
    with open(branch + ".txt") as file:
        for line in file:
            line = line.strip()
            lines.append(line)
    return lines

def get_changelist(branch, root, head):
    try:
        os.remove(branch + ".txt")
    except OSError as e:
        pass

    status = call("git checkout " + branch,cwd=os.path.dirname(os.path.realpath(__file__)), shell=True)
    status = call("git pull", cwd=os.path.dirname(os.path.realpath(__file__)), shell=True)
    status = call("git log --pretty=format:%s {0}..{1} > {2}.txt".format(root, head, branch), cwd=os.path.dirname(os.path.realpath(__file__)), shell=True)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Helper script for diffing the commits."
    )

    parser.add_argument(
        "--froot",
        nargs="?",
        default="-"
    )

    parser.add_argument(
        "--fhead",
        nargs="?",
        default="-"
    )

    parser.add_argument(
        "--fbranch",
        nargs="?",
        default="master"
    )

    parser.add_argument(
        "--sbranch",
        nargs="?",
        default="r-4.2.x"
    )

    parser.add_argument(
        "--sroot",
        nargs="?",
        default=""
    )

    parser.add_argument(
        "--shead",
        nargs="?",
        default=""
    )

    args = parser.parse_args()

    build_difference(args.fbranch, args.froot, args.fhead, args.sbranch, args.sroot, args.shead)