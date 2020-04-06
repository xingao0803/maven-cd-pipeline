{
    "files": [
    {
        "aql": {
            "items.find": {
                "repo": "maven-pipeline-release-local",
                "name":{"$match":"multi3-*.war"},
                "@quality.gate.sonarIssue":{"$lt":"4"},
                "@test.approve":{"$eq":"true"}
            }
        }
    }]
}
