# SWE1 Django Polls App

[![Build Status](https://app.travis-ci.com/LaxmanSRawat/swe1-app.svg?branch=main)](https://app.travis-ci.com/github/LaxmanSRawat/swe1-app)
[![Coverage Status](https://coveralls.io/repos/github/LaxmanSRawat/swe1-app/badge.svg?branch=main)](https://coveralls.io/github/LaxmanSRawat/swe1-app?branch=main)

## CI/CD

- Travis CI runs on push and pull requests.
- CI checks include:
  - `black --check`
  - `flake8`
  - Django tests with `coverage`
  - coverage upload with `coveralls`
- On successful CI, Travis deploys to AWS Elastic Beanstalk (main branch). 