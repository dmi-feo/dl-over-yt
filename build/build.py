#!/usr/bin/env python

import argparse
import os
import tempfile
import subprocess
import datetime
import uuid

import yaml


REPO_DIR = "repo"


def main(config_path: str, docker_tag: str | None = None, push_docker: bool = False):
    with open(config_path) as config_file:
        config = yaml.safe_load(config_file)

    patches = list(map(os.path.abspath, config["patches"]))

    docker_tag = docker_tag or datetime.datetime.now().strftime("%Y-%m-%d") + "-" + str(uuid.uuid4())
    full_docker_tag = f"{config["docker_image"]}:{docker_tag}"

    with tempfile.TemporaryDirectory() as build_dir:
        print("Working directory:", build_dir)
        os.chdir(build_dir)
        subprocess.run(["git", "clone", config["repo_url"], REPO_DIR])

        os.chdir(REPO_DIR)

        if config["checkout"] is not None:
            subprocess.run(["git", "checkout", config["checkout"]])

        for patch_file in patches:
            print("Going to apply patch", patch_file)
            subprocess.run(["git", "apply", patch_file])
            print("Patch applied successfully:", patch_file)

        os.chdir(config["docker_context"])
        subprocess.run(["docker", "build", ".", "-t", full_docker_tag])
        if push_docker:
            subprocess.run(["docker", "push", full_docker_tag])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--config-path")
    parser.add_argument("-t", "--docker-tag")
    parser.add_argument("--docker-push", action="store_true")
    args = parser.parse_args()

    main(config_path=args.config_path, docker_tag=args.docker_tag, push_docker=args.docker_push)
