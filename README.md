# MERGER

Merger is a python utility that helps to find the commit difference between two branches.

##### usage: merger.py [-h] [--froot [FROOT]] [--fhead [FHEAD]] [--fbranch [FBRANCH]] [--sbranch [SBRANCH]] [--sroot [SROOT]] [--shead [SHEAD]]

## Description

The utility compares two ranges of commits FROOT...FHEAD vs SROOT...SHEAD.

Where **FROOT** is the commit to start comparing from for the first branch.

Where **SROOT** is the commit to start comparing from for the second branch.

Where **FHEAD** is the last commit that will be used for comparison from for the first branch.

Where **SHEAD** is the last commit that will be used for comparison from for the second branch.

Where **FBRANCH** is the first branch to compare.

Where **SBRANCH** is the second branch to compare


## Example
```bash
python3 merger.py --fbranch master --sbranch feature_branch --froot 62bc988160b5efbc0874bec6c12c66c3d084607f --fhead 242caf6fd1dd8b5302b76cd950393f3a6aa11a4a --sroot 62bc988160b5efbc0874bec6c12c66c3d084607f --shead 7f0f6307ca0c0a3a1ff18d5edaf84bd9e13e693f 
```

The example output:
```bash
Unique commits in master :

COMMIT 1
COMMIT 2
....

#####################################################################

Unique commits in feature_branch :

COMMIT 3
COMMIT 4
```

