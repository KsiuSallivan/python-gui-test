import pytest
from fixture.application import Application


@pytest.fixture(scope="session")
def app(request):
    fixture = Application("C:\\Users\\ksiu_\\python_training\\AddressBook.exe")
    request.addfinalizer(fixture.destroy)
    return fixture