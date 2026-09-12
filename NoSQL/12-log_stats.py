#!/usr/bin/env python3
"""Provide statistics about Nginx logs."""

from pymongo import MongoClient


def main():
    """Print Nginx log statistics."""
if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")
    collection = client["logs"]["nginx"]

    print("{} logs".format(collection.count_documents({})))
    print("Methods:")

    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        count = collection.count_documents({"method": method})
        print("\t{}: {}".format(method, count))

    status = collection.count_documents({
        "method": "GET",
        "path": "/status"
    })
    print("{} status check".format(status))



