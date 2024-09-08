# Remote Repositories
## Introduction
Even though about 90% of version control related word is done on local repositories, remote repositories are the ones needed to collaborate with other team members.

Effective collaboration involves knowing how to ...
- ... manage (*add*, *remove*, *etc.*) remote repositories
- ... work with data (*push* and *pull* changes) from remote repositories

Example remote repositories:
- GitHub repository
- a user's fork on a server
- another computer on your local network

**Pushing** and **pulling** to/from remote repositories can be accomplished with HTTP and SSH protocols

Example: Pulling from **GitHub** using the `git clone` command
- With `HTTP` over `SSL` (HTTPS), we would type:
  ```shell
  git clone https://github.com/user/repo.git
  ```
- And with `SSH` you would type:
  ```shell
  git clone git@github.com:user/repo.git
  ```

## Working with Remotes
You can see the remote repositories with your project by calling `git remote`:
```shell
git remote
# origin
```
- Note: `origin` is the default name **Git** gives to thte server you cloned from

You can see the URLs associated with the remotes using the `-v` flag:
```shell
git remote -v
# origin https://github.com/user/rep (fetch)
# origin https://github.com/user/rep (push)
```

You can add new remotes using the `git remote add` command:
```shell
# git remote add <shortname><url>
git remote add xy \
    https://github//github.com/us/repo
git remote -v
# origin https://github.com/user/rep (fetch)
# origin https://github.com/user/rep (push)
# xy https://github.com/user/rep (fetch)
# xy https://github.com/user/rep (push)
```

## Merging
**Merging** = the operation of joining two or more development histories (branches) together
For this, Git provides the `git merge` command:
```shell
git merge [head]
```
Example 1: Suppose you are on a branch called `feature` where you committed some work. However, you want to get the feature to the `master` branch; the main branch of development on your project.
```shell
# current branch  - feature
git checkout master
# current branch - master
git merge feature
# merging feature into master
```
Note: Merging is not always successful
- This can happed when both branches had modifications in the *same* files (changes since the time they diverged).
- In this case, Git doesn't know what version of the file to choose and requires your guidance.
- Use the `git status` command to check what files weren't successfully merged:
  ```shell
  git status
  # On branch master
  # You have unmerged paths.
  #     (fix conflicts and run "git commit")
  # ...
  #     both modified:  file.txt
  # ...
  ```

- In these files you can see the conflict highlighted by the syntax:
  ```shell
  <<<<<<< HEAD # master in our case
  # master version here
  ======= 
  # feature version here
  >>>>>>> feature
  ```

  - Above the `=======` you can see the version of the file in the `HEAD` before the merge
  - Below the `=======` you can see the targeted branch version

## Pushing
**Pushing** = a way to share/push upstream your work on a remote repository
- Basic syntax:
  ```shell
  git push [remote-name] [branch-name]
  ```

Example 1: Suppose you want to push all your local commits to the `origin` server on the `main` branch (both automatically named) you can use,
```shell
git push origin main
```

Example 2: Suppose you want to push to the upstream of you current local branch
```shell
git push
```

Example 3: Suppose you are on a `feature` branch and you want to set its upstream
```shell
git push --set-upstream origin feature
```
- This command will create (if it doesn't already exist) a new remote branch called `feature`, and push all your changes there
s
Notes:
- The `git push` command only works if you have write permissions to the remote repository.
- If the history differe3s from your local - due to somebody pushing changes since your last **pull** or **fetch** - your push will be rejected. To fix this, you must first `fetch`, `merge`, (or just `pull`) theri work. Your push will be accepted once all merging conflicts are resolved.