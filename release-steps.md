# Steps for PyPI release/update

See more details [here].

- Do you have a setup.py?
- Update changelog.txt
- Update version number in documentation
- Update version number in setup.py
- Convert README.md to README.rst
  ```bash
    pandoc --columns=100 --output=README.rst --to rst README.md
  ```
- Add tarball download url to setup.py
  ```python
    setup(
        ...
        url = 'https://github.com/sheriferson/simplestatistics',
        download_url = 'https://github.com/sheriferson/simplestatistics/tarball/0.2.5',
        ...
    )
    ```
- If there are new files that should be included, edit MANIFEST.in
- clear dist folder
  ```bash
  rm -r dist/*
  ```
- generate package
  ```bash
  python setup.py sdist bdist_wheel
  ```
- Commit all those changes. Have a clean repo.
- Add/create a git tag
- Push git tag to remote
  ```bash
  git tag 1.2.3 -m "Adds 1.2.3 tag for PyPI
  ```
- Confirm that GitHub has generated the release file
  ```bash
  git push --tags origin master
  ```
- Release testing
    * `twine upload --repository testpypi dist/*`
    python -m twine upload --repository testpypi dist/*
    * `twine upload --repository-url https://test.pypi.org/legacy/ dist/*`
    * `pip install -i https://testpypi.python.org/pypi simplestatistics`
- Release
    - `python setup.py register -r pypi`
    - `python setup.py sdist upload -r pypi`
    - `pip install simplestatistics`
- Add changelog notes to GitHub release page/tag

[here]: http://sherifsoliman.com/2016/09/30/Python-package-with-GitHub-PyPI/