# Git Cheatsheet
Delete branch
```bash
# delete branch locally
git branch -d localBranchName

# delete branch remotely
git push origin --delete remoteBranchName
```

Undo a commit & redo
```bash
git commit -m "Something terribly misguided" # (0: Your Accident)
git reset HEAD~                              # (1)

# Delete the most recent commit, keeping the work you've done:
git reset --soft HEAD~1

# Delete the most recent commit, destroying the work you've done:
git reset --hard HEAD~1
```

Apply the changes introduced by some existing commits
```bash
# apply the change from a particular commit
git cherry-pick <commit-id>     

# summarize changes to be reconciled
git diff        
# cancel the cherry-pick. In other words, return to the pre-cherry-pick state, preserving any local modifications you had in the working tree.                   
git reset --merge ORIG_HEAD  

# try to apply the change introduced by topic^ again, spending extra time to avoid mistakes based on incorrectly matching context lines.
git cherry-pick -Xpatience topic^  
```