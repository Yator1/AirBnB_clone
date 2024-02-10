#!/usr/bin/python3

"""creating a unique FileStorage instance for my app"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
