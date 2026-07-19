#!/usr/bin/env python3
"""
Returns the list of school having a specific topic.
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns schools that contain the specific topic in their topics list.
    """
    return list(mongo_collection.find({"topics": topic}))
