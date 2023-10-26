#
# COSC2671 Social Media and Network Analytics
# @author Jeffrey Chan, RMIT University, 2023
#

import sys
import praw


def redditClient():
    """
        Setup Reedit API authentication.
        Replace username, secrets and passwords with your own.

        @returns: praw Reedit object
    """

    try:
        #
        # TODO: you specify with your details
        #
        clientId = "FYWF9jKmVU-kpUEqeWl8zA"
        clientSecret = "D2crz7cVfxCZ3sWacHkBXAwVsJp9sQ"
        password = "P@ssw0rd55"
        userName = "Su_05"
        userAgents = 'client for SNAM2023'

        redditClient = praw.Reddit(client_id = clientId,
                                   client_secret = clientSecret,
                                   password = password,
                                   username = userName,
                                   user_agent = userAgents)
    except KeyError:
        sys.stderr.write("Key or secret token are invalid.\n")
        sys.exit(1)


    return redditClient
