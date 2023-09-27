# suppression-test-python-side-branches

This repository is used to test our analysis code for studying suppressed warnings.
The focus here is on
 * Python repositories
 * Pylint
 * The repositories with side branches

## Ground truth of this repository
Specifically, this is a repository used to test if we can get commits located at the main branch and the corresponding histories. If the commits originally come from the "side-branch", we expect to ignore it.
 * Totally with 2 branches:
     * main
     * side-branch
 * Only 1 Pylint suppression (add and delete at some point)

## Expected output of our analysis scripts
Total with 12 commits.   
Time order: C1, C2, ...,C12  

|    Distribution         | C1      | C2 | C3 | C4 | C5 | C6 | C7 | C8 | C9 | C10 | C11 | C12 |
|--------------|----------|----------|----------|----------|----------|----------|----------|----------|-----------|-----------|-----------|-----------|
|  main        | &check; | &check; | &check; |  |  |  | &check; | &check; |  | &check; | &check; | &check; |
| side-branch  |  |     |  | &check; | &check; | &check; |  |  | &check; |  |  |  | 

What really happened in this repository:
| Event | Commit | main | side-branch |
|----------|----------|----------|----------|
| Add a suppression  | e6dc00b0, C3  | &check; |
| Delete the suppression   | 53e13693, C4  |    | &check; |
| Get the deleted suppression back | 43c62e3b, C5 | | &check; |
| Fix the warning, Delete the suppression | 073f1c76, C6  |  | &check; |
| Delete the suppression | 0d381092, C11  | &check; |  |

## Expected output of our analysis scripts

#### File greeting.py
* Suppression： # pylint: disable=unused-variable
  * Introduced in commit e6dc00b0, C3, main branch
  * Removed in commit 0d381092, C11, main branch
  * **ignore the changes in *side-branch***


