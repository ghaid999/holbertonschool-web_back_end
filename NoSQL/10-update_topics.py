#!/usr/bin/env python3
"""Update school topics in MongoDB."""


def update_topics(mongo_collection, name, topics):
    """Update the topics of a school."""
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
