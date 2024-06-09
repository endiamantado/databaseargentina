#!/bin/bash
source venv/bin/activate
exec gunicorn -b :$PORT app:app