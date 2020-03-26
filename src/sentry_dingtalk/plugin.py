# coding: utf-8

import json

import requests
from sentry.plugins.bases.notify import NotificationPlugin

import Sentry_DingTalk
from .forms import DingTalkOptionsForm

DingTalk_API = "https://oapi.dingtalk.com/robot/send?access_token={token}"


class DingTalkPlugin(NotificationPlugin):
    """
    Sentry plugin to send error counts to DingTalk.
    """
    author = 'ansheng'
    author_url = 'https://github.com/rockerpine/sentry-dingtalk'
    version = Sentry_DingTalk.VERSION
    description = 'Send error counts to DingTalk.'
    resource_links = [
        ('Source', 'https://github.com/rockerpine/sentry-dingtalk'),
        ('Bug Tracker', 'https://github.com/rockerpine/sentry-dingtalk/issues'),
        ('README', 'https://github.com/rockerpine/sentry-dingtalk/README.md'),
    ]

    slug = 'DingTalk'
    title = 'DingTalk'
    conf_key = slug
    conf_title = title
    project_conf_form = DingTalkOptionsForm

    def is_configured(self, project):
        """
        Check if plugin is configured.
        """
        return bool(self.get_option('access_token', project))

    def notify_users(self, group, event, *args, **kwargs):
        self.post_process(group, event, *args, **kwargs)

    def post_process(self, group, event, *args, **kwargs):
        """
        Process error.
        """
        if not self.is_configured(group.project):
            return

        if group.is_ignored():
            return

        access_token = self.get_option('access_token', group.project)
        send_url = DingTalk_API.format(token=access_token)
        title = u"New alert from {}".format(event.project.slug)

        data = {
            "msgtype": "markdown",
            "markdown": {
                "title": title,
                "text": u"#### {title} \n > {message} [href]({url})".format(
                    title=title,
                    message=event.message,
                    url=u"{}events/{}/".format(group.get_absolute_url(), event.id),
                )
            }
        }
        requests.post(
            url=send_url,
            headers={"Content-Type": "application/json"},
            data=json.dumps(data).encode("utf-8")
        )
