import os


def test_retry():
    attempt = os.getenv("CI_RETRY_TEST")

    if attempt == "fail":
        raise AssertionError("Échec volontaire pour tester le retry automatique.")

    assert True
