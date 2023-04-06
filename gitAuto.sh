#!/bin/bash

ch=0
repoPath="-1"

menu()
{
    echo -n "The following commands are currently supported by the script:

1. Add your username and email address
2. View your username and email address
3. Enter/View the current repository path to work on
4. Add files for committing
5. Commit the files
6. Push the commit
7. Pull from the current branch
8. View current and all branches (both remote and local)
9. Create a new branch
10. Change current branch
11. Merge with a branch
12. Delete a local branch
13. Delete a remote branch
14. View status
15. Clone a repository (from default branch)
16. Clone a repository (from a specific branch)
17. View recent commits
18. View a particular commit
19. Exit

Enter the option: "
    read ch
    echo ""
}

inputRepoPath(){
    echo "Enter the repo path: "
    read repoPath
}

viewRepoPath(){
    if [[ "$repoPath" == "-1" ]]
    then
        echo "No path specified!"
    else
        echo "$repoPath"
    fi
}

takeInput(){
    echo -ne "\nEnter the option (Enter 0 to display menu): "
    read ch
    echo ""
}

checkPath(){
    if [[ "$repoPath" == "-1" ]]
    then
    inputRepoPath
    fi
}

addUserEmail(){
    git config --global user.name "$1"
    git config --global user.email "$2"
}

viewUserEmail(){
    git config --global --list
}

addFiles(){
    (cd "$repoPath" && cd "$1" && git add .)
}

commitFiles(){
    (cd "$repoPath" && git commit -m "$1")
}

pushFiles(){
    (cd "$repoPath" && git push -u origin HEAD)
}

pullFiles(){
    (cd "$repoPath" && git pull)
}

viewBranch(){
    (cd "$repoPath" && git branch -a)
}

createBranch(){
    (cd "$repoPath" && git checkout -b "$1")
}

changeBranch(){
    (cd "$repoPath" && git checkout "$1")
}

mergeBranch(){
    (cd "$repoPath" && git merge "$1")
}

deleteLocalBranch(){
    (cd "$repoPath" && git branch -d "$1")
}

deleteRemoteBranch(){
    (cd "$repoPath" && git push origin --delete "$1")
}

viewStatus(){
    (cd "$repoPath" && git status)
}

cloneRepo(){
    git clone "$1" "$2"
}

cloneRepoBranch(){
    git clone -b "$2" "$1"
}

viewRecentCommits(){
    (cd "$repoPath" && git log)
}

viewCommit(){
    (cd "$repoPath" && git show "$1")
}


cases(){
    case $ch in

    1)
    username="test"
    useremail="test"
    echo -n "Enter your GitHub Username: "
    read username
    echo -n "Enter your GitHub E-mail: "
    read useremail
    addUserEmail "$username", "$useremail"
    ;;

    2)
    viewUserEmail
    ;;

    3)
    echo -n "Enter 1 for View, anything else for Inupt: "
    read repoch

    if [ $repoch -eq 1 ]
    then
        viewRepoPath
    else
        inputRepoPath
    fi
    ;;

    4)
    checkPath
    directory="."
    echo "Enter the directory from which to add files relative to the repo (Enter . for current directory): "
    read directory
    addFiles "$directory"
    ;;

    5)
    checkPath
    message="test"
    echo "Enter the commit message: "
    read message
    commitFiles "$message"
    ;;

    6)
    checkPath
    pushFiles
    ;;

    7)
    checkPath
    pullFiles
    ;;

    8)
    checkPath
    viewBranch
    ;;

    9)
    checkPath
    echo -n "Enter the branch name: "
    read branchName
    createBranch "$branchName"
    ;;

    10)
    checkPath
    echo -n "Enter the branch name: "
    read branchName
    changeBranch "$branchName"
    ;;

    11)
    checkPath
    echo -n "Enter the branch name to merge with: "
    read branchName
    mergeBranch "$branchName"
    ;;

    12)
    checkPath
    echo -n "Enter the local branch name to delete: "
    read branchName
    deleteLocalBranch "$branchName"
    ;;

    13)
    checkPath
    echo -n "Enter the remote branch name to delete: "
    read branchName
    deleteRemoteBranch "$branchName"
    ;;

    14)
    checkPath
    viewStatus
    ;;

    15)
    echo "Enter the URL for the repository you wish to clone: "
    read url
    echo "Enter the path where you wish to clone (Enter . for current directory): "
    read path
    cloneRepo "$url" "$path"
    ;;

    16)
    echo "Enter the URL for the repository you wish to clone: "
    read url
    echo "Enter the branch name: "
    read branchName
    echo "Enter the path where you wish to clone (Enter . for current directory): "
    read path
    cloneRepoBranch "$url" "$branchName" "$path"
    ;;

    17)
    checkPath
    viewRecentCommits
    ;;

    18)
    checkPath
    echo -n "Enter the commit hash: "
    read commitHash
    viewCommit "$commitHash"
    ;;

    esac
}

menu

while [[ $ch -ne 19 ]]
do
    cases
    takeInput
    if [ $ch -eq 0 ]
    then
        menu
    fi
done

echo "Thanks for Using!"