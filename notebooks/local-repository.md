# Local Repositories

From the 'perspective' of Git, there are two types of files that may exist:

1. **tracked** $\Rightarrow$ files that were part of the most recent file snapshot
   - Flagged as either...
     1. ... *modified*
         - A tracked file that is detected by Git as different from previous commit will be flagged as **modified**.
     2. ... **unmodified**
     3. ... or, **staged**
2. **untracked** $\Rightarrow$ files that were not part of the most recent file snapshot, nor are in the staging area

- [ ] Determine whether Git 'labels' files in a global repository the same way as described for a local repository

## Working in the local repository

If you want to permanently store changes made to a file in a local repository (or permanently add a new file not in the most recent commit), there are a series of operations that need to be performed.

1. Stage a modified (or new) file in the **staging area**.
   - Use the `git add` command to add a snapshot of the edited (or new) file to the staging area
2. Once you are finished staging all the files you want to modify and/or add, use the `git commit` command to permanently store the **staged** files to the local Git repository.

## Tracking and Staging Files

Use the `git  status` command to track files inside a Git project

- Example 1 : The message in the code snippet is displayed when there are *no tracked or modified files*

    ```shell
    git status
    # On branch master
    # Your branch is up-to-date with 'origin master'.
    # Nothing to commit, working directory clean
    ```

- Example 2: Suppose we add `renzo.txt` to our project. Running the `git status` command will give the following result.

    ```shell
    git status
    # On branch develop
    # Your branch ...
    # Untracked files:
    #   renzo.txt
    # nothing aedded to commit ...
    ```

  - Tell Git to manage changes made in `renzo.txt` (i.e., tell Git to track it) using the `git add` command:

        ```shell
        git add renzo.txt
        ```

  - Running the `git status` command again will give the following result:

        ```shell
        git status
        # ...
        # Changes to be committed:
        #   new file:   renzo.text
        ```

- Example 3: Suppose we want to add multiple files. Here are a few options for adding multiple files at once.

    ```shell
    # stage everything (option 1)
    git add [-A|--all]
    # stage everything (option 2)
    git add .
    # stage everything except new files
    git add [-u|--update]
    ```

### Committing

Commit staged snapshots:

```shell
# option 1
git commit
# option 2
git commit -m "Description of changes"
```

Commit ALL changes of tracked files (even if unstaged):

```shell
git commit -a
```

## Stashing

**Dirty files** = modified tracked files and staged changes

**Stashing** = the action of saving all your dirty files in a special stack of commits

- **stack** = an abstract data type on top of which `git`'s stash is built
  - Name comes from an analogy to a set of physical items (e.g., plates) stacked on top of each other. You can only add an element to the top of the stack or remove the topmost element of the stack. This is called **LIFO** - last in, first out
- Commits in the stash are counted from index `0`. More recent commits, with a higher index, sit above older ones.
- Any of the commits in the stash can be later popped, restoring the state of the working tree

Use the `git stash` command to use this feature.

Example 1: Suppose you have some modified files, you can check on them using `git status`:

```shell
git status
# ...
# Changes to be committed:
#   modified: renzo.txt
```
- To stash your changes:
  ```shell
    git stash
    # Saved working directory and index state
    # HEAD is not at e0bb9432 ...
  ```
- Checking again shows that the working directory is clean:
  ```shell
    git status
    # On branch master
    # You branch is up-to-date with 'origin/master' ...
  ```
- To view all your stashed changes:
  ```shell
    git stash list
    # stash@{0}: WIP on master: 049d078 ...
    # stash@{1}: WIP on master: 21d80a5 ...
  ```
- To apply the latest stashed changes: 
  ```shell
  git stash apply
  ```
- Top apply a specific stashed set of changes, you must specify its name:
    ```shell
    git stash apply stash@{2}
    ```
- You can also remove from the stash stack:
    ```shell
    git stash drop stash@{0}
    ```
- Use the `pop` command to both *apply* and *drop* the stash
  ```shell
    git stash pop
  ````