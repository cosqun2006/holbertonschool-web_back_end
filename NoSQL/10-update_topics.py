#!/usr/bin/env python3
"""
Changes all topics of a school document based on the name.
"""


def update_topics(mongo_collection, name, topics):
    """
    Updates the topics attribute of a school document.
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
