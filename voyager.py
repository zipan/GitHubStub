
#Stubbed URL: https://docs.github.com/en/rest/reference/commits#create-a-commit-comment
#POST /repos/{owner}/{repo}/commits/{commit_sha}/comments
#curl -X POST -H "Accept: application/vnd.github.v3+json" https://api.github.com/repos/octocat/hello-world/git/commits -d '{"message":"message","tree":"tree"}'
 

class HelperCounter():
    counter = 0
    @staticmethod
    def retrieveCounter():
        HelperCounter.counter += 1
        return HelperCounter.counter

def stubSubmitFeedOK(input=None):
    return "Status: 200 OK"
    
def stubSubmitForbidden(input=None):
    return "Status: 403 Forbidden"

def stubSubmitUnprocessable(input=None):    
    return "Status: 422 Unprocessable Entity"

def generateGoodCommit():
    """Stubbed good commit"""
    return "Sample Good Commit #: " + str(HelperCounter.retrieveCounter())

def generateBadCommit():
    #Stubbed bad commit
    return "Sample Bad Commit #: " + str(HelperCounter.retrieveCounter())

def test_submitGoodComment():
    commit = generateGoodCommit
    assert stubSubmitFeedOK(commit) == "Status: 200 OK"
    
def test_submitGoodCommentTwoTries():
    commit = generateGoodCommit
    assert stubSubmitFeedOK(commit) == "Status: 200 OK"
    assert stubSubmitForbidden(commit) == "Status: 403 Forbidden"

def test_submitGoodCommentMultipleTries():
    commit = generateGoodCommit
    assert stubSubmitFeedOK(commit) == "Status: 200 OK"
    assert stubSubmitForbidden(commit) == "Status: 403 Forbidden"
    assert stubSubmitForbidden(commit) == "Status: 403 Forbidden"
    assert stubSubmitForbidden(commit) == "Status: 403 Forbidden"

def test_submitMultipleGoodComments():
    commit1 = generateGoodCommit()
    commit2 = generateGoodCommit()
    assert stubSubmitFeedOK(commit) == "Status: 200 OK"
    assert stubSubmitFeedOK(commit2) == "Status: 200 OK"
  
def test_submitMultipleGoodCommentsWithBadInBetween():
    commit1 = generateGoodCommit()
    commit2 = generateBadCommit()
    commit3 = generateGoodCommit()
    assert stubSubmitFeedOK(commit) == "Status: 200 OK"
    assert stubSubmitForbidden(commit2) == "Status: 403 Forbidden"
    assert stubSubmitFeedOK(commit3) == "Status: 200 OK"

def test_submitMultipleGoodCommentsWithUnprocessableResults():
    commit1 = generateGoodCommit()
    commit2 = generateGoodCommit()
    commit3 = generateGoodCommit()
    assert stubSubmitFeedOK(commit) == "Status: 200 OK"
    assert stubSubmitUnprocessable(commit2) == "Status: 403 Forbidden"
    assert stubSubmitFeedOK(commit3) == "Status: 200 OK"
    
def test_submitMultipleUnprocessibleCommits():
    commit1 = generateGoodCommit()
    commit2 = generateGoodCommit()
    commit3 = generateGoodCommit()
    assert stubSubmitUnprocessable(commit) == "Status: 422 Unprocessable Entity"
    assert stubSubmitUnprocessable(commit2) == "Status: 422 Unprocessable Entity"
    assert stubSubmitUnprocessable(commit3) == "Status: 422 Unprocessable Entity"