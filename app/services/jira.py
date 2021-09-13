from typing import Optional

from jira import JIRA
from app.models.issue import Issue, IssueType

USER_NAME = "some_user@some_domain.net"
PASSWORD = "some_password"
URL = "https://itooknap.atlassian.net/"
PROJECT_ID = "ITN"


class JiraClient:
    def __init__(self) -> None:
        self._client = JIRA(basic_auth=(USER_NAME, PASSWORD), server=URL)

    def create_issue(
        self, name: str, issue_type: IssueType, story_points: Optional[int] = None, parent_id: Optional[str] = None
    ) -> Issue:
        # Docs: https://jira.readthedocs.io/en/master/api.html?highlight=create_issue#jira.client.JIRA.create_issue

        issue = self._client.create_issue(
            project=PROJECT_ID,
            summary=name,
            description="",
            issuetype={"name": issue_type.value},
        )

        if issue_type.value == IssueType.STORY.value and story_points:
            issue.update(customfield_10016=story_points)

        if issue_type.value == IssueType.STORY.value and parent_id:
            issue.update(parent={"id": parent_id})

        return Issue(
            id=issue.id,
            name=issue.fields.summary,
            issue_type=IssueType(issue.fields.issuetype.name),
            url=issue.permalink(),
            story_points=story_points,
            parent_id=parent_id
        )


jira_client = JiraClient()
