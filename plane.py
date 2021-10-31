#! /usr/bin/env python3
from cli import prompt_schema, prompt_profile
from send import PlaneSend

def plane():
    profile = prompt_profile()
    schema = prompt_schema()
    PlaneSend(schema, profile).execute()

if __name__ == "__main__":
    plane()
